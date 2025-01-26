# VizAI-DataInsights_Assistant

VizAI-DataInsights_Assistant is an AI-powered data visualization and analysis tool designed to simplify complex data analysis tasks. Users can upload datasets, ask questions in natural language, and receive insights, visualizations, or even Python code to analyze their data. The tool ensures a user-friendly experience by leveraging AI and safe code execution environments.

---

## 🌟 Inspiration

The inspiration for **VizAI-DataInsights_Assistant** stems from the challenges faced by individuals—technical and non-technical alike—in understanding complex datasets. The goal was to bridge the gap by creating a tool that combines AI's power with user-friendly interfaces, making data analysis accessible to everyone.

---

## ✨ What It Does

1. **Natural Language Querying**: Users can ask questions in plain English.
2. **Data Analysis & Insights**: AI processes the dataset and provides meaningful insights.
3. **Dynamic Visualizations**: Generates visualizations from user queries.
4. **Code Generation**: AI creates Python code to analyze the dataset and executes it safely in a sandbox environment (E2B).
5. **User-Friendly Interface**: Built with Streamlit for easy interaction, even for non-technical users.

---

## 🛠️ How We Built It

### **Technologies Used**
- **Frontend**: [Streamlit](https://streamlit.io/) for a clean and interactive user interface.
- **Backend**: 
  - [Together AI](https://together.ai) for natural language processing and query interpretation.
  - [E2B](https://e2b.dev) sandbox for executing AI-generated Python code securely.
- **Data Processing**:
  - **pandas** for data manipulation.
  - **Matplotlib** and **Plotly** for generating visualizations.
- **Development Tools**:
  - VSCode for coding.
  - Python for backend scripting.
- **Additional Libraries**: `re`, `warnings`.

---

## 🚀 Challenges We Ran Into

1. **Dynamic Visualization Generation**: Enabling AI to generate relevant Python code dynamically based on user queries.
2. **Code Execution in E2B**: Ensuring the AI-generated code runs smoothly and securely in the sandbox environment.
3. **Seamless Integration**: Connecting Together AI for query interpretation with E2B for executing code while maintaining real-time responses.

---

## 🏆 Accomplishments We're Proud Of

- Successfully created an intuitive system capable of transforming complex data tasks into simple queries.
- Developed dynamic visualizations that respond to user input.
- Built a user-friendly interface accessible to individuals without technical expertise.

---

## 📚 What We Learned

- **E2B Sandbox**: Discovered and integrated E2B for executing AI-generated code securely.
- **AI Integration**: Learned how to combine AI and data processing pipelines effectively.
- Enhanced our skills in designing user-centric applications with minimal friction.

---

## 🔮 What's Next for VizAI-DataInsights_Assistant

1. **Module 2: Insights & PDF Reports**  
   - Generate detailed data insights with downloadable PDFs.
   - Include trends, actionable recommendations, and visual summaries.

2. **Module 3: Real-Time Database Insights**  
   - Enable users to query live databases for real-time insights.
   - Automate visualizations and generate instant reports.

---

## 💻 Built With

- [E2B](https://e2b.dev)
- [GitHub](https://github.com)
- [Matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Together AI](https://together.ai)
- [VSCode](https://code.visualstudio.com/)

---

## 📝 Installation

```bash
# Installation and Setup Guide  

## **Step 1: Prerequisites**  

Ensure you have the following installed on your system:  

- **Python**  
- **Git** (for cloning the repository)  
```
---

## **Step 2: Clone the Repository**  

Clone the project repository from GitHub:  
```bash
git clone https://github.com/yourusername/yourproject.git
```

## **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

## **Step 4: Run code locally **

```bash
streamlit run ai_data_visualisation.py
```

## **Step 5: Get Together.ai and E2B Apis**

- Get Together api [here](https://api.together.ai/)
- Get E2B api [here](https://e2b.dev/)
1. Sigup
2. Proceed To Dashboard
3. Get your api key at keys section


## **Step 5: **

