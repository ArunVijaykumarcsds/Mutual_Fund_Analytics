# Mutual Fund Analytics Dashboard

## Project Overview

The Mutual Fund Analytics Dashboard is an end-to-end data analytics project developed to analyze, evaluate, and recommend mutual funds based on performance and risk metrics.

The project combines data engineering, exploratory data analysis, financial analytics, database management, and dashboard development into a single integrated system.

The dashboard enables users to:

- Explore mutual fund schemes
- Analyze fund performance
- Evaluate risk characteristics
- Generate investor-specific recommendations
- Download filtered results for further analysis

The solution was developed using Python, SQLite, Streamlit, Pandas, NumPy, Scikit-Learn, Plotly, and Matplotlib.

---

## Project Objectives

The primary objectives of the project are:

1. Build a structured mutual fund dataset.
2. Perform data validation and quality assessment.
3. Analyze fund performance metrics.
4. Calculate risk-related indicators.
5. Create an investor recommendation engine.
6. Develop an interactive dashboard for end users.
7. Demonstrate an end-to-end analytics workflow suitable for real-world deployment.

---

## Problem Statement

Investors often struggle to compare mutual funds because fund performance depends on multiple factors such as returns, volatility, drawdown, and risk-adjusted measures.

Most publicly available platforms focus on raw returns without providing a unified analytical framework.

This project aims to create a centralized analytics platform that:

- Collects and organizes mutual fund information.
- Computes performance metrics.
- Evaluates risk characteristics.
- Generates recommendations based on investor profiles.
- Presents insights through an interactive dashboard.

The goal is to support informed investment decisions through data-driven analysis.

---

## Dataset Description

The project utilizes mutual fund datasets collected from publicly available financial sources and processed into structured analytical tables.

### Primary Dataset Components

1. Fund Master Data
   - AMFI Code
   - Scheme Name
   - Fund House
   - Category
   - Sub Category
   - Plan Type
   - Benchmark

2. Performance Dataset
   - CAGR
   - Sharpe Ratio
   - Sortino Ratio
   - Volatility
   - Maximum Drawdown
   - Value at Risk (VaR)

3. Recommendation Dataset
   - Recommendation Score
   - Investor Profile Mapping
   - Risk Classification

### Dataset Size

- Total Funds Analyzed: 40
- Multiple Categories Included
- Equity Funds
- Debt Funds
- Hybrid Funds

The processed datasets are stored in CSV format and SQLite database tables for efficient querying and dashboard integration.

---

## Data Pipeline

The project follows a structured analytics pipeline:

### Step 1: Data Collection

Raw mutual fund datasets are collected and stored inside the raw data directory.

### Step 2: Data Validation

Validation scripts verify:

- Missing values
- Duplicate records
- Invalid AMFI codes
- Incorrect data types

### Step 3: Data Cleaning

Data cleaning operations include:

- Handling missing values
- Standardizing column names
- Formatting dates
- Removing duplicates

### Step 4: Database Storage

Cleaned datasets are loaded into SQLite for efficient access and querying.

### Step 5: Analytics Layer

Performance and risk metrics are calculated using Python analytical scripts.

### Step 6: Recommendation Engine

Funds are scored based on:

- Return potential
- Risk characteristics
- Investor profile suitability

### Step 7: Dashboard Visualization

The Streamlit dashboard presents all analytics through interactive visualizations and downloadable reports.

---

## Database Design

SQLite is used as the central storage layer.

### Database Tables

#### fund_master

Stores basic mutual fund information.

| Column |
|----------|
| amfi_code |
| scheme_name |
| fund_house |
| category |
| sub_category |
| plan |

#### performance_metrics

Stores calculated performance indicators.

| Column |
|----------|
| amfi_code |
| cagr |
| sharpe_ratio |
| sortino_ratio |

#### risk_metrics

Stores risk measurements.

| Column |
|----------|
| volatility |
| max_drawdown |
| var_95 |

### Benefits of SQLite

- Lightweight
- Easy deployment
- Fast querying
- Suitable for analytical dashboards
- No external database server required

---

## Analytics Methodology

The analytical framework combines performance analysis, risk evaluation, and recommendation scoring.

### Performance Metrics

#### CAGR (Compound Annual Growth Rate)

CAGR measures the average annual growth rate of a mutual fund over a specified period.

Benefits:

- Measures long-term growth
- Smooths short-term fluctuations
- Allows fund comparison

#### Sharpe Ratio

Sharpe Ratio evaluates risk-adjusted returns.

Interpretation:

- Higher Sharpe Ratio indicates better risk-adjusted performance.
- Positive values indicate favorable returns relative to risk.

#### Sortino Ratio

Sortino Ratio focuses only on downside volatility.

Advantages:

- Penalizes harmful volatility only.
- More suitable for investment analysis than standard volatility measures.

---

### Risk Metrics

#### Volatility

Measures the dispersion of returns.

Higher volatility indicates higher uncertainty.

#### Maximum Drawdown

Measures the largest decline from peak value.

Used to estimate downside risk.

#### Value at Risk (VaR)

Estimates the maximum expected loss within a confidence interval.

The project uses VaR at 95% confidence level.

---

### Recommendation Engine

Funds are ranked using a weighted scoring approach.

Factors considered:

- CAGR
- Sharpe Ratio
- Sortino Ratio
- Volatility
- Maximum Drawdown

The engine generates recommendations for:

- Conservative Investors
- Moderate Investors
- Aggressive Investors

---

## Dashboard Modules

The Streamlit dashboard contains four primary modules.

### 1. Fund Explorer

Features:

- Search mutual funds
- Category filtering
- Fund house filtering
- Dataset download

### 2. Performance Analytics

Features:

- Performance dataset visualization
- CAGR analysis
- Sharpe Ratio analysis
- Summary statistics

### 3. Risk Analysis

Features:

- Volatility visualization
- Maximum Drawdown analysis
- Value at Risk metrics
- Risk ranking charts

### 4. Recommendation Engine

Features:

- Investor profile selection
- Fund ranking
- Recommendation score generation
- CSV export

---

## Dashboard Screenshots

### Home Dashboard

![Home Dashboard](screenshots/home.png)

### Fund Explorer

![Fund Explorer](screenshots/explorer.png)

### Performance Analytics

![Performance Analytics](screenshots/performance.png)

### Risk Analysis

![Risk Analysis](screenshots/risk.png)

### Recommendation Engine

![Recommendation Engine](screenshots/recommendations.png)

---

## Results and Findings

The developed analytics platform successfully analyzed 40 mutual fund schemes.

Key findings include:

- Average CAGR observed: 16.07%
- Average Sharpe Ratio observed: 0.69
- Average Volatility observed: 14.94
- Highest risk fund identified through volatility ranking.
- Recommendation engine successfully generated profile-based fund recommendations.

The dashboard provides a unified environment for performance evaluation and risk assessment.

Benefits achieved:

- Faster fund comparison
- Improved decision support
- Interactive analytics
- Downloadable recommendations

---

## Conclusion

The Mutual Fund Analytics Dashboard successfully demonstrates an end-to-end data analytics workflow for financial data analysis.

The project integrates:

- Data ingestion
- Data validation
- Database management
- Performance analytics
- Risk assessment
- Recommendation generation
- Interactive dashboard development

The dashboard provides investors with a centralized platform for evaluating mutual funds using both return-based and risk-adjusted metrics.

The project highlights the practical application of Python-based analytics tools in solving real-world financial analysis problems.

---

## Future Enhancements

The following enhancements can be implemented in future versions:

1. Live NAV integration using MFAPI.
2. Real-time fund performance monitoring.
3. Portfolio optimization module.
4. Machine Learning-based return prediction.
5. Fund clustering using unsupervised learning.
6. Sentiment analysis using financial news.
7. User authentication and profile management.
8. Cloud deployment using AWS or Azure.
9. Mobile-friendly dashboard interface.
10. Automated report generation in PDF format.

---

## References

1. AMFI India
   https://www.amfiindia.com

2. MFAPI
   https://www.mfapi.in

3. Streamlit Documentation
   https://docs.streamlit.io

4. Pandas Documentation
   https://pandas.pydata.org

5. NumPy Documentation
   https://numpy.org

6. Scikit-Learn Documentation
   https://scikit-learn.org

7. Plotly Documentation
   https://plotly.com/python

8. SQLite Documentation
   https://www.sqlite.org

9. Python Documentation
   https://docs.python.org

10. Financial Risk Management Literature
    Sharpe Ratio, Sortino Ratio, Maximum Drawdown and Value at Risk methodologies.

---

