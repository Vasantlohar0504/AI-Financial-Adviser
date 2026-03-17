# 💰 AI Financial Adviser
---
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Model-green)
![AI Chatbot](https://img.shields.io/badge/AI-Chatbot-orange)
![Ollama](https://img.shields.io/badge/Ollama-LLM-black)
![LLaMA3](https://img.shields.io/badge/LLaMA3-Local%20Model-purple)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-blueviolet)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

An AI-powered financial advisory web application that provides **risk analysis, portfolio recommendations, investment simulations, and chatbot-based financial guidance**.

---

## 🚀 Features

* 📊 **Financial Risk Prediction (ML Model)**
* 💯 **Financial Health Score Calculation**
* 📈 **Portfolio Optimization**
* 💡 **Rule-Based Financial Advice**
* 🤖 **AI Chatbot (LLM - Ollama / LLaMA3)**
* 📉 **Investment Growth Simulator**
* 🎨 **Modern Fintech Dashboard UI (Streamlit)**

---

## 🏗️ Project Architecture

```
AI-FINANCIAL-ADVISER
│
├── app/
│   └── app.py                  # Main Streamlit Web App
│
├── assets/
│   ├── architecture.png       # Project architecture diagram
│   ├── dashboard.png          # UI preview
│   └── demo.gif               # Demo animation
│
├── data/
│   ├── financial_data.csv     # Raw dataset
│   ├── processed_financial_*.csv  # Cleaned dataset
│   ├── final_financial_*.csv  # Final dataset for training
│   └── generate_dataset.py    # Generates synthetic financial data
│
├── models/
│   └── (trained ML models)    # Saved ML models
│
├── notebooks/
│   ├── 01_eda_analysis.ipynb      # Data analysis & visualization
│   └── 02_model_building.ipynb    # Model training experiments
│
├── src/
│   ├── predictor.py          # Risk prediction model
│   ├── recommendation.py     # Score + financial advice logic
│   ├── portfolio_optimizer.py # Portfolio allocation + growth
│   ├── llm_advisor.py        # AI chatbot (Ollama API)
│   ├── preprocessing.py      # Data cleaning & feature engineering
│   ├── train_model.py        # Model training script
│   └── clustering.py         # User segmentation (optional)
│
├── .env                      # API keys 
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ How the Project Works (Pipeline)

### Step 1: Data Generation

* `generate_dataset.py` creates synthetic financial data

### Step 2: Data Processing

* `preprocessing.py` cleans and prepares data

### Step 3: EDA (Exploration)

* Done in `notebooks/01_eda_analysis.ipynb`

### Step 4: Model Training

* `train_model.py` trains ML model
* Model saved in `models/`

### Step 5: Prediction + Logic

* `predictor.py` → predicts risk
* `recommendation.py` → score + advice
* `portfolio_optimizer.py` → investment plan

### Step 6: Web App

* `app/app.py` → Streamlit dashboard

### Step 7: AI Chatbot

* `llm_advisor.py` → connects to local LLM (Ollama)

---

## 📂 File Explanation

### 🟢 app/

**app.py**

* Main application
* Handles UI, navigation, and integration of all modules

---

### 🟡 data/

**generate_dataset.py**

* Creates random financial dataset for training

**financial_data.csv**

* Raw generated data

**processed_financial_*.csv**

* Cleaned dataset after preprocessing

**final_financial_*.csv**

* Final dataset used for ML model

---

### 🔵 src/

**predictor.py**

* Uses trained ML model to classify risk:

  * Low / Medium / High

**recommendation.py**

* Calculates:

  * Financial Score
  * Rule-based financial advice

**portfolio_optimizer.py**

* Suggests asset allocation
* Simulates investment growth

**llm_advisor.py**

* Connects to Ollama (LLaMA3)
* Acts like ChatGPT for finance questions

**preprocessing.py**

* Cleans dataset
* Feature engineering

**train_model.py**

* Trains ML model and saves it

**clustering.py (optional)**

* Groups users based on financial behavior

---

### 🟣 notebooks/

**01_eda_analysis.ipynb**

* Data visualization
* Pattern analysis

**02_model_building.ipynb**

* ML experimentation

---

### ⚫ models/

* Stores trained ML models

---

### ⚙️ Other Files

**requirements.txt**

* Python dependencies

**.env**

* Stores API keys 

---

## 🖥️ Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Run Streamlit App

```bash
streamlit run app/app.py
```

---

### 3️⃣ Run AI Chatbot (Ollama)

Install Ollama → https://ollama.com

```bash
ollama run llama3
```

---

## 🤖 AI Chatbot Setup

Make sure Ollama is running locally:

```
http://localhost:11434
```

Used in:

```python
llm_advisor.py
```


## 🚀 Live Demo

👉 Click here to use the app:  
🔗 https://ai-financial-adviser.streamlit.app

---
## 📸 Screenshots

### Dashboard

![Dashboard](assets/dashboard.png)

### Architecture

![Architecture](assets/architecture.png)

---

## 👨‍💻 Author
Vasant Lohar
**AI Financial Adviser Project**
