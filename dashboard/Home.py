import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mutual Fund Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Mutual Fund Analytics Dashboard")

st.markdown("""
Welcome to the Mutual Fund Analytics Dashboard.

This project includes:

- Fund Explorer
- Performance Analytics
- Risk Analysis
- Recommendation Engine
""")

# Load data
performance = pd.read_csv(
    "data/processed/performance_metrics.csv"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Funds",
        performance["amfi_code"].nunique()
    )

with col2:
    st.metric(
        "Average CAGR",
        round(performance["cagr"].mean(), 2)
    )

with col3:
    st.metric(
        "Average Sharpe Ratio",
        round(performance["sharpe_ratio"].mean(), 2)
    )

st.subheader("Performance Metrics Preview")
st.dataframe(performance.head())