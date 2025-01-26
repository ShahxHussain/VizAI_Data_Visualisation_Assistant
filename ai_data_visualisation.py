import os
import json
import re
import sys
import io
import contextlib
import warnings
from typing import Optional, List, Any, Tuple
from PIL import Image
import streamlit as st
import pandas as pd
import base64
from io import BytesIO
from together import Together
from e2b_code_interpreter import Sandbox

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

# Regular expression for matching Python code blocks
pattern = re.compile(r"```python\n(.*?)\n```", re.DOTALL)

def code_interpret(e2b_code_interpreter: Sandbox, code: str) -> Optional[List[Any]]:
    """Run code in the E2B sandbox."""
    with st.spinner('Executing code in E2B sandbox...'):
        try:
            exec = e2b_code_interpreter.run_code(code)
            if exec.error:
                st.error(f"Error in code execution: {exec.error}")
                return None
            return exec.results
        except Exception as e:
            st.error(f"An exception occurred: {e}")
            return None

def match_code_blocks(llm_response: str) -> str:
    """Extract Python code blocks from LLM response."""
    match = pattern.search(llm_response)
    if match:
        return match.group(1)
    return ""

def chat_with_llm(e2b_code_interpreter: Sandbox, user_message: str, dataset_path: str) -> Tuple[Optional[List[Any]], str]:
    """Communicate with Together AI LLM and execute code."""
    system_prompt = f"""You're a Python data scientist. Analyze the dataset at '{dataset_path}' and answer user queries by generating Python code."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    with st.spinner('Getting response from Together AI LLM model...'):
        client = Together(api_key=st.session_state.together_api_key)
        response = client.chat.completions.create(
            model=st.session_state.model_name,
            messages=messages,
        )

        response_message = response.choices[0].message.content
        python_code = match_code_blocks(response_message)
        
        if python_code:
            code_interpreter_results = code_interpret(e2b_code_interpreter, python_code)
            return code_interpreter_results, response_message
        else:
            st.warning("No Python code found in LLM response.")
            return None, response_message

def upload_dataset(code_interpreter: Sandbox, uploaded_file) -> str:
    """Upload dataset to E2B sandbox."""
    dataset_path = f"./{uploaded_file.name}"
    code_interpreter.files.write(dataset_path, uploaded_file.read())
    return dataset_path

def main():
    """Main Streamlit application."""
    st.title("📊 VizAI: Data Visualization Assistant")
    st.write("Upload your dataset, ask questions, and get insights with visualizations!")

    # Initialize session state variables
    if 'together_api_key' not in st.session_state:
        st.session_state.together_api_key = ''
    if 'e2b_api_key' not in st.session_state:
        st.session_state.e2b_api_key = ''
    if 'model_name' not in st.session_state:
        st.session_state.model_name = ''

    with st.sidebar:
        st.sidebar.image("./Extras/Logo-removebg-preview.png", width=200) 
        st.header("API Keys and Model Configuration")
        st.session_state.together_api_key = st.text_input("Together AI API Key", type="password")
        st.sidebar.markdown("[Get Together AI API Key](https://api.together.ai/signin)")

        st.session_state.e2b_api_key = st.text_input("E2B API Key", type="password")
        st.sidebar.markdown("[Get E2B API Key](https://e2b.dev/docs/legacy/getting-started/api-key)")
        
        # Model selection dropdown
        model_options = {
            "Meta-Llama 3.1 405B": "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
            "DeepSeek V3": "deepseek-ai/DeepSeek-V3",
            "Qwen 2.5 7B": "Qwen/Qwen2.5-7B-Instruct-Turbo",
            "Meta-Llama 3.3 70B": "meta-llama/Llama-3.3-70B-Instruct-Turbo"
        }
        st.session_state.model_name = st.selectbox("Select Model", list(model_options.keys()))
        st.session_state.model_name = model_options[st.session_state.model_name]

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Dataset Preview:")
        st.dataframe(df.head())

        query = st.text_area("Ask a question about your data", "Example: Compare sales by region.")
        
        if st.button("Analyze"):
            if not st.session_state.together_api_key or not st.session_state.e2b_api_key:
                st.error("Please provide API keys in the sidebar.")
            else:
                with Sandbox(api_key=st.session_state.e2b_api_key) as code_interpreter:
                    dataset_path = upload_dataset(code_interpreter, uploaded_file)
                    code_results, llm_response = chat_with_llm(code_interpreter, query, dataset_path)
                    
                    st.write("AI Response:")
                    st.write(llm_response)
                    
                    if code_results:
                        for result in code_results:
                            if isinstance(result, (pd.DataFrame, pd.Series)):
                                st.dataframe(result)
                            elif hasattr(result, 'show'):  # For Plotly visualizations
                                st.plotly_chart(result)
                            elif hasattr(result, 'figure'):  # For Matplotlib visualizations
                                st.pyplot(result.figure)
                            else:
                                st.write(result)

if __name__ == "__main__":
    main()
