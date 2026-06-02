import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Fund Recommendations",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Fund Recommendations")

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    "data/processed/performance_metrics.csv"
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("Investor Profile")

profile = st.sidebar.selectbox(
    "Select Profile",
    [
        "Conservative",
        "Moderate",
        "Aggressive"
    ]
)

# ==================================================
# FILTER FUNDS
# ==================================================

filtered_df = df.copy()

if profile == "Conservative":

    filtered_df = filtered_df[
        filtered_df["volatility"] < 10
    ]

elif profile == "Moderate":

    filtered_df = filtered_df[
        (filtered_df["volatility"] >= 10)
        &
        (filtered_df["volatility"] <= 18)
    ]

else:

    filtered_df = filtered_df[
        filtered_df["volatility"] > 18
    ]

# ==================================================
# HANDLE EMPTY RESULTS
# ==================================================

if len(filtered_df) == 0:

    st.warning(
        "No funds available for selected profile."
    )

    st.stop()

# ==================================================
# RECOMMENDATION SCORE
# ==================================================

filtered_df = filtered_df.copy()

filtered_df["recommendation_score"] = (
    filtered_df["cagr"] * 0.50
    +
    filtered_df["sharpe_ratio"] * 30
    +
    filtered_df["sortino_ratio"] * 10
    -
    filtered_df["volatility"] * 0.20
    +
    filtered_df["var_95"].abs() * (-2)
)

recommended = (
    filtered_df
    .sort_values(
        by="recommendation_score",
        ascending=False
    )
    .reset_index(drop=True)
)

# ==================================================
# SUMMARY METRICS
# ==================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Eligible Funds",
        len(recommended)
    )

with col2:

    st.metric(
        "Average CAGR",
        round(
            recommended["cagr"].mean(),
            2
        )
    )

with col3:

    st.metric(
        "Average Sharpe Ratio",
        round(
            recommended["sharpe_ratio"].mean(),
            2
        )
    )

# ==================================================
# BEST FUND
# ==================================================

st.divider()

best_fund = recommended.iloc[0]

st.success(
    f"""
🏆 BEST RECOMMENDED FUND

{best_fund['scheme_name']}

Recommendation Score: {best_fund['recommendation_score']:.2f}

CAGR: {best_fund['cagr']:.2f}%

Volatility: {best_fund['volatility']:.2f}

Sharpe Ratio: {best_fund['sharpe_ratio']:.2f}

Sortino Ratio: {best_fund['sortino_ratio']:.2f}
"""
)

# ==================================================
# TOP RECOMMENDATIONS TABLE
# ==================================================

st.divider()

st.subheader("Top Recommended Funds")

top10 = recommended.head(min(10, len(recommended)))

display_df = top10[
    [
        "scheme_name",
        "cagr",
        "volatility",
        "sharpe_ratio",
        "sortino_ratio",
        "recommendation_score"
    ]
].copy()

display_df = display_df.round(2)

st.dataframe(
    display_df,
    width="stretch",
    hide_index=True
)

# ==================================================
# RECOMMENDATION CHART
# ==================================================

st.divider()

fig = px.bar(
    top10,
    x="scheme_name",
    y="recommendation_score",
    color="recommendation_score",
    title="Top Recommended Funds"
)

fig.update_layout(
    height=600,
    xaxis_title="Fund",
    yaxis_title="Recommendation Score",
    xaxis_tickangle=-45
)

st.plotly_chart(
    fig,
    width="stretch",
    key="recommendation_bar_chart"
)

# ==================================================
# RISK VS RETURN
# ==================================================

st.divider()

st.subheader("Risk vs Return")

fig2 = px.scatter(
    recommended,
    x="volatility",
    y="cagr",
    color="recommendation_score",
    hover_name="scheme_name",
    title="Risk vs Return Analysis"
)

fig2.update_layout(
    height=600,
    xaxis_title="Volatility",
    yaxis_title="CAGR"
)

st.plotly_chart(
    fig2,
    width="stretch",
    key="risk_return_chart"
)

# ==================================================
# DOWNLOAD
# ==================================================

st.divider()

csv = recommended.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Recommendations",
    data=csv,
    file_name=f"{profile.lower()}_recommendations.csv",
    mime="text/csv"
)