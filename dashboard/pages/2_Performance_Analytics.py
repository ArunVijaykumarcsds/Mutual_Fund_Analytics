import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Performance Analytics",
    layout="wide"
)

st.title("📈 Performance Analytics")

df = pd.read_csv(
    "data/processed/performance_metrics.csv"
)

st.subheader("Performance Dataset")

st.dataframe(
    df,
    width="stretch"
)

# Metrics

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average CAGR",
        round(df["cagr"].mean(), 2)
    )

with col2:
    st.metric(
        "Average Sharpe Ratio",
        round(df["sharpe_ratio"].mean(), 2)
    )

with col3:
    st.metric(
        "Average Volatility",
        round(df["volatility"].mean(), 2)
    )

# Top CAGR Funds

st.subheader("Top 10 Funds by CAGR")

top_cagr = (
    df[
        ["scheme_name", "cagr"]
    ]
    .sort_values(
        by="cagr",
        ascending=False
    )
    .head(10)
)

st.bar_chart(
    top_cagr.set_index(
        "scheme_name"
    )
)

# CAGR vs Volatility

st.subheader(
    "Risk vs Return"
)

st.scatter_chart(
    df,
    x="volatility",
    y="cagr"
)