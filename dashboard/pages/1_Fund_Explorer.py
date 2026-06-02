import streamlit as st
import pandas as pd
import sqlite3

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(page_title="Fund Explorer", layout="wide")

st.title("🔍 Fund Explorer")

# --------------------------------------------------
# Database Connection
# --------------------------------------------------

conn = sqlite3.connect("data/db/bluestock_mf.db")

# Change table name if needed after checking tables
query = """
SELECT *
FROM fund_master
"""

df = pd.read_sql(query, conn)

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("Filters")

# Category Filter
if "category" in df.columns:
    categories = ["All"] + sorted(df["category"].dropna().unique().tolist())

    selected_category = st.sidebar.selectbox(
        "Select Category",
        categories
    )
else:
    selected_category = "All"

# Fund House Filter
if "fund_house" in df.columns:
    fund_houses = ["All"] + sorted(
        df["fund_house"].dropna().unique().tolist()
    )

    selected_fund_house = st.sidebar.selectbox(
        "Select Fund House",
        fund_houses
    )
else:
    selected_fund_house = "All"

# --------------------------------------------------
# Apply Filters
# --------------------------------------------------

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

if selected_fund_house != "All":
    filtered_df = filtered_df[
        filtered_df["fund_house"] == selected_fund_house
    ]

# --------------------------------------------------
# Search
# --------------------------------------------------

search_text = st.text_input(
    "Search Scheme Name"
)

if search_text:
    filtered_df = filtered_df[
        filtered_df["scheme_name"]
        .astype(str)
        .str.contains(search_text, case=False, na=False)
    ]

# --------------------------------------------------
# Metrics
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Funds Found",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Total Funds",
        len(df)
    )

# --------------------------------------------------
# Display Data
# --------------------------------------------------

st.dataframe(
    filtered_df,
    use_container_width=True
)

# --------------------------------------------------
# Download CSV
# --------------------------------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_funds.csv",
    mime="text/csv"
)

conn.close()