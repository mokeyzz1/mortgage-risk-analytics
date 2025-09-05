# Mortgage Risk Analytics Platform

**An end-to-end data analytics platform for mortgage risk assessment using real Freddie Mac loan data (2023-2024)**

[Live Dashboard](your-dashboard-url) | [Analysis Notebook](notebooks/01_mortgage_risk_analysis.ipynb)

## Problem Statement

Mortgage lenders need to identify loans likely to become delinquent before it happens. This platform analyzes borrower characteristics, loan features, and geographic factors to predict risk and improve underwriting decisions.

**Target Users:** Mortgage lenders, credit policy teams, underwriters, risk managers

## Key Features

- **Interactive Dashboard** - Real-time portfolio monitoring and risk analytics
- **Risk Classification** - Automated loan risk tier assignment (High/Medium/Low)
- **Geographic Analysis** - State-level risk mapping and trends
- **Performance Metrics** - Model validation and business impact tracking
- **SQL Database Layer** - Organized schema and reusable queries for data analysis

## Technical Stack

- **Data Processing:** Python, pandas, SQLite
- **Analytics:** Jupyter notebooks, statistical modeling
- **Visualization:** Plotly, Streamlit
- **Deployment:** Streamlit Cloud, optimized performance

## Project Structure

```
mortgage-risk-analytics/
├── dashboards/
│   └── mortgage_risk_dashboard.py    # Main dashboard
├── data/
│   ├── dashboard_cache/              # Optimized data (275KB)
│   └── processed/                    # Database files
├── notebooks/
│   └── 01_mortgage_risk_analysis.ipynb
├── src/
│   ├── database/
│   │   ├── schema.sql                # Database schema
│   │   ├── queries.sql               # Analysis queries
│   │   └── db_manager.py             # Database wrapper
│   ├── optimize_dashboard_data.py
│   └── config.py
└── requirements.txt
```

## Results

- **Risk Detection:** 42.1% recall rate for identifying high-risk loans
- **Efficiency:** Reduces manual review workload to 11.3% of portfolio
- **Performance:** Optimized loading from 30-60s to 1-3s (2000% improvement)
- **Data Scale:** Processed 2.4GB of real mortgage data covering millions of loans

## Quick Start

### Option 1: Demo Mode (Immediate)
```bash
git clone https://github.com/mokeyzz1/mortgage-risk-analytics.git
cd mortgage-risk-analytics
pip install -r requirements.txt
streamlit run dashboards/mortgage_risk_dashboard.py
```
*Uses pre-computed cache files (275KB) - runs instantly!*

### Option 2: Full Analysis (Complete Dataset)

1. **Clone Repository**
   ```bash
   git clone https://github.com/mokeyzz1/mortgage-risk-analytics.git
   cd mortgage-risk-analytics
   pip install -r requirements.txt
   ```

2. **Download Freddie Mac Data**
   - Visit [Freddie Mac Historical Loan Performance Data](https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset)
   - Create free account and accept terms
   - Download **Historical Data 2023** and **Historical Data 2024** (8 quarters)
   - Extract files to: `data/raw/historical_data_YYYY/historical_data_YYYYQX/`

3. **Data Structure (After Download)**
   ```
   data/raw/
   ├── historical_data_2023/
   │   ├── historical_data_2023Q1/
   │   │   ├── historical_data_2023Q1.txt
   │   │   └── historical_data_time_2023Q1.txt
   │   └── ... (Q2, Q3, Q4)
   └── historical_data_2024/
       └── ... (Q1, Q2, Q3, Q4)
   ```

4. **Process Data**
   ```bash
   python data_assessment.py  # Validate data structure
   jupyter notebook notebooks/01_mortgage_risk_analysis.ipynb  # Run full analysis
   ```

5. **Run Dashboard**
   ```bash
   streamlit run dashboards/mortgage_risk_dashboard.py
   ```

## Data Information

**Source:** Freddie Mac Single-Family Loan-Level Dataset (2023-2024)
- **Size:** ~2.4GB compressed, ~7GB processed
- **Records:** 2M+ loans with 26M+ monthly performance updates  
- **Fields:** 32+ data points per loan (credit score, LTV, geography, etc.)
- **License:** Free for research and educational use
- **Update Frequency:** Quarterly releases

**Note:** Raw data files are not included in this repository due to size (7GB total). The dashboard runs on optimized cache files (275KB) that provide full functionality for demonstration purposes.

## Skills Demonstrated

- **Data Engineering:** ETL pipelines, database optimization, performance tuning
- **Data Science:** Statistical analysis, risk modeling, feature engineering
- **Business Intelligence:** Dashboard development, KPI design, stakeholder communication
- **Software Development:** Python programming, version control, deployment optimization