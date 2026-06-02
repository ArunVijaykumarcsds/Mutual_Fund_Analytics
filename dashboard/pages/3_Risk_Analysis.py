import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Risk Analysis",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Risk Analysis")

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    "data/processed/performance_metrics.csv"
)

# ==================================================
# SUMMARY METRICS
# ==================================================

avg_volatility = round(
    df["volatility"].mean(),
    2
)

avg_drawdown = round(
    df["max_drawdown"].mean(),
    2
)

avg_var = round(
    df["var_95"].mean(),
    2
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Volatility",
        avg_volatility
    )

with col2:
    st.metric(
        "Average Max Drawdown",
        avg_drawdown
    )

with col3:
    st.metric(
        "Average VaR (95%)",
        avg_var
    )

# ==================================================
# HIGHEST RISK FUND
# ==================================================

most_risky = df.loc[
    df["volatility"].idxmax(),
    "scheme_name"
]

st.info(
    f"⚠️ Highest Risk Fund: {most_risky}"
)

# ==================================================
# TOP VOLATILE FUNDS
# ==================================================

st.subheader("Top 10 Most Volatile Funds")

volatile_df = (
    df.sort_values(
        by="volatility",
        ascending=False
    )
    .head(10)
    .copy()
)

volatile_df["short_name"] = (
    volatile_df["scheme_name"]
    .str.slice(0, 30)
)

fig1 = px.bar(
    volatile_df,
    x="short_name",
    y="volatility",
    color="volatility",
    color_continuous_scale="Blues",
    title="Top 10 Most Volatile Funds"
)

fig1.update_layout(
    xaxis_title="Fund",
    yaxis_title="Volatility",
    xaxis_tickangle=-45,
    height=500
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# ==================================================
# MAXIMUM DRAWDOWN DISTRIBUTION
# ==================================================

st.subheader("Maximum Drawdown Distribution")

fig2 = px.histogram(
    df,
    x="max_drawdown",
    nbins=20,
    title="Distribution of Maximum Drawdown"
)

fig2.update_layout(
    xaxis_title="Max Drawdown",
    yaxis_title="Count",
    height=500
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# ==================================================
# RISK VS RETURN
# ==================================================

st.subheader("Risk vs Return Analysis")

fig3 = px.scatter(
    df,
    x="volatility",
    y="cagr",
    color="sharpe_ratio",
    hover_name="scheme_name",
    size="volatility",
    color_continuous_scale="RdYlGn",
    title="Risk vs Return"
)

fig3.update_layout(
    xaxis_title="Volatility",
    yaxis_title="CAGR",
    height=600
)

st.plotly_chart(
    fig3,
    width="stretch"
)

# ==================================================
# RISK METRICS TABLE
# ==================================================

st.subheader("Risk Metrics")

risk_df = df[
    [
        "scheme_name",
        "volatility",
        "sharpe_ratio",
        "sortino_ratio",
        "max_drawdown",
        "var_95"
    ]
].copy()

risk_df = risk_df.sort_values(
    by="volatility",
    ascending=False
).reset_index(drop=True)

numeric_cols = [
    "volatility",
    "sharpe_ratio",
    "sortino_ratio",
    "max_drawdown",
    "var_95"
]

risk_df[numeric_cols] = (
    risk_df[numeric_cols]
    .round(2)
)

st.dataframe(
    risk_df,
    width="stretch",
    hide_index=True
)

# ==================================================
# DOWNLOAD OPTION
# ==================================================

csv = risk_df.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Risk Report",
    data=csv,
    file_name="risk_metrics.csv",
    mime="text/csv"
)