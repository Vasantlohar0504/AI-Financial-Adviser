
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from streamlit_option_menu import option_menu

from src.predictor import predict_risk
from src.recommendation import financial_score, generate_advice
from src.portfolio_optimizer import portfolio_allocation, investment_growth
from src.llm_advisor import ask_financial_llm


# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="AI Financial Adviser",
    page_icon="💰",
    layout="wide"
)

# -------------------------------
# CUSTOM CSS
# -------------------------------

st.markdown("""
<style>

body {
background-color: #0E1117;
color: white;
}

.big-title{
font-size:80px;
font-weight:900;
color:#00c6ff;
text-align:center;
margin-bottom:10px;
letter-spacing:1px;

background: linear-gradient(90deg,#ff4b4b,#ff0000);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}

.metric-card {
background: linear-gradient(135deg,#1f77b4,#00c6ff);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
font-weight:bold;
box-shadow:0px 4px 15px rgba(0,0,0,0.4);
}

.section-title{
font-size:28px;
font-weight:600;
margin-top:30px;
}

</style>
""", unsafe_allow_html=True)


# ✅ FIXED TITLE (emoji separated)
st.markdown("""
<h1 class="big-title">
<span style="color:#00c6ff; -webkit-text-fill-color:initial;">💰</span>
 AI Financial Adviser
</h1>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------

st.write("AI powered financial insights and smart investment recommendations.")

# -------------------------------
# NAVBAR
# -------------------------------

selected = option_menu(
    menu_title=None,
    options=["Dashboard","Portfolio","Investment Simulator","AI Advisor"],
    icons=["bar-chart","pie-chart","graph-up","robot"],
    orientation="horizontal"
)

# -------------------------------
# SIDEBAR INPUT
# -------------------------------

st.sidebar.header("📥 Enter Your Financial Data")

age = st.sidebar.number_input("Age", 18, 70)
income = st.sidebar.number_input("Monthly Income", 0.0)
expenses = st.sidebar.number_input("Monthly Expenses", 0.0)
savings = st.sidebar.number_input("Total Savings", 0.0)
debt = st.sidebar.number_input("Total Debt", 0.0)

goal = st.sidebar.selectbox(
    "Investment Goal",
    ["Wealth Growth","Retirement Planning","Emergency Fund"]
)

analyze = st.sidebar.button("Run AI Analysis")

# -------------------------------
# CALCULATE DATA
# -------------------------------

if analyze:

    if income <= 0:
        st.error("Income must be greater than zero.")
        st.stop()

    savings_rate = savings / income
    expense_ratio = expenses / income
    debt_ratio = debt / income

    data = {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "debt": debt,
        "savings_rate": savings_rate,
        "expense_ratio": expense_ratio,
        "debt_ratio": debt_ratio
    }

    risk = predict_risk(data)
    score = financial_score(savings_rate, debt_ratio)
    advice = generate_advice(risk)
    portfolio = portfolio_allocation(risk)

    st.session_state.profile = f"""
Income: {income}
Expenses: {expenses}
Savings: {savings}
Debt: {debt}
Risk Profile: {risk}
"""

    st.session_state.risk = risk
    st.session_state.score = score
    st.session_state.portfolio = portfolio
    st.session_state.advice = advice
    st.session_state.savings_rate = savings_rate

# -------------------------------
# DASHBOARD PAGE
# -------------------------------

if selected == "Dashboard":

    if "risk" not in st.session_state:
        st.info("Enter financial data and click **Run AI Analysis**.")
    else:

        st.markdown("### 📊 Financial Overview")

        col1, col2, col3 = st.columns([1,1,1], gap="small")

        col1.markdown(f"""
        <div class="metric-card">
        <h3>Risk Profile</h3>
        <h1>{st.session_state.risk}</h1>
        </div>
        """, unsafe_allow_html=True)

        col2.markdown(f"""
        <div class="metric-card">
        <h3>Financial Score</h3>
        <h1>{st.session_state.score}</h1>
        </div>
        """, unsafe_allow_html=True)

        col3.markdown(f"""
        <div class="metric-card">
        <h3>Savings Rate</h3>
        <h1>{round(st.session_state.savings_rate*100,1)}%</h1>
        </div>
        """, unsafe_allow_html=True)

        # -------------------------------
        # FINANCIAL HEALTH GAUGE
        # -------------------------------

        st.markdown("### 📈 Financial Health Indicator")

        current_score = st.session_state.get("score", 0)

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=current_score,
            title={'text': "Financial Health Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "green"},
                'steps': [
                    {'range': [0, 40], 'color': "red"},
                    {'range': [40, 70], 'color': "orange"},
                    {'range': [70, 100], 'color': "lightgreen"}
                    ]
                }
            ))

        gauge.update_layout(height=380)

        left, center, right = st.columns([2,3,2])
        with center:
            st.plotly_chart(gauge, use_container_width=True)

# -------------------------------
# PORTFOLIO PAGE
# -------------------------------

if selected == "Portfolio":

    if "portfolio" not in st.session_state:
        st.info("Run AI Analysis first.")
    else:

        st.markdown("### 📊 Recommended Portfolio")

        portfolio_df = pd.DataFrame(
            list(st.session_state.portfolio.items()),
            columns=["Asset","Allocation"]
        )

        fig = px.bar(
            portfolio_df,
            x="Asset",
            y="Allocation",
            color="Asset",
            title="Portfolio Allocation"
        )

        st.plotly_chart(fig,width="stretch")
        st.success(st.session_state.advice)

# -------------------------------
# INVESTMENT SIMULATOR PAGE
# -------------------------------

if selected == "Investment Simulator":

    st.markdown("### 📈 Investment Growth Simulator")

    initial = st.number_input("Initial Investment",1000)
    monthly = st.number_input("Monthly Investment",500)
    years = st.slider("Investment Period (Years)",1,30,10)

    growth_df = investment_growth(initial,monthly,years)

    st.line_chart(growth_df.set_index("Month"))

# -------------------------------
# AI ADVISOR PAGE
# -------------------------------

if selected == "AI Advisor":

    st.markdown("### 🤖 AI Financial Advisor")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_question = st.chat_input("Ask financial advice...")

    if user_question:

        profile = st.session_state.get("profile","No financial profile available.")

        answer = ask_financial_llm(user_question,profile)

        st.session_state.messages.append({"role":"user","content":user_question})
        st.session_state.messages.append({"role":"assistant","content":answer})

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

