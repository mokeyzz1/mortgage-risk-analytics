# Mortgage Risk Analytics Platform

Enterprise-grade analytics for mortgage risk assessment using Freddie Mac loan data (2023-2024)

**[Live Dashboard](https://mokeyzz1-mortgage-risk-dashboardsmortgage-risk-dashboard-6nzvum.streamlit.app)** | [Analysis Notebook](notebooks/01_mortgage_risk_analysis.ipynb) | [GitHub Repository](https://github.com/mokeyzz1/mortgage-risk-analytics)

---

## Overview

This platform provides advanced analytics to identify high-risk loans before delinquency occurs. Built with real Freddie Mac data spanning 2023-2024, the system processes over 2 million loan records to deliver actionable insights for risk management and underwriting decisions.

**Target Users:** Mortgage lenders, credit policy teams, underwriters, risk managers, financial analysts

## Key Features

**Interactive Dashboard**
- Real-time portfolio monitoring across 2M+ loans
- Interactive risk calculator for loan-level assessment
- Geographic risk mapping and state-level analysis

**Risk Modeling**
- Automated loan classification (High/Medium/Low Risk)
- Multi-factor assessment using credit scores, DTI ratios, and LTV ratios
- Performance validation and accuracy tracking

**Technical Performance**
- High-speed caching system (30-60s → 1-3s loading time)
- Cloud deployment with zero-downtime updates
- Scalable architecture handling millions of records

## Technical Architecture

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Data Processing** | Python, pandas, SQLite | ETL pipelines and data transformation |
| **Analytics Engine** | Jupyter, NumPy, Statistical modeling | Risk analysis and model development |
| **Visualization** | Plotly, Streamlit | Interactive charts and dashboard |
| **Database** | SQLite, optimized queries | Data storage and retrieval |
| **Deployment** | Streamlit Cloud, GitHub | Cloud hosting and version control |
| **Performance** | Parquet, caching | Optimized data loading |

## Project Structure

```
mortgage-risk-analytics/
├── dashboards/
│   └── mortgage_risk_dashboard.py      # Main Streamlit dashboard (1,300+ lines)
├── data/
│   ├── dashboard_cache/                # Optimized cache files (275KB)
│   │   ├── main_dashboard_data.parquet
│   │   ├── geographic_data.parquet
│   │   ├── credit_distribution.pkl
│   │   ├── risk_summary.pkl
│   │   └── summary_stats.json
│   ├── processed/
│   │   └── mortgage_analytics.db       # Main database (4.5GB)
│   └── raw/                           # Freddie Mac source data (2.4GB)
├── notebooks/
│   └── 01_mortgage_risk_analysis.ipynb # Complete analysis workflow
├── src/
│   ├── database/
│   │   ├── schema.sql                  # Database schema design
│   │   ├── queries.sql                 # Reusable analytical queries
│   │   └── db_manager.py               # Database connection wrapper
│   ├── optimize_dashboard_data.py      # Performance optimization
│   └── config.py                       # Configuration management
├── streamlit_app.py                    # Alternative entry point
└── requirements.txt                    # Python dependencies
```
## Results

**Key Metrics:**
- 42.1% recall rate for identifying high-risk loans
- 2000% performance improvement in dashboard loading
- 2M+ loans analyzed across 8 quarters (2023-2024)
- Coverage across all 50 US states

## Quick Start

**[View Live Dashboard](https://mokeyzz1-mortgage-risk-dashboardsmortgage-risk-dashboard-6nzvum.streamlit.app)** - Instant access with pre-loaded data

**Local Setup:**
```bash
git clone https://github.com/mokeyzz1/mortgage-risk-analytics.git
cd mortgage-risk-analytics
pip install -r requirements.txt
streamlit run dashboards/mortgage_risk_dashboard.py
```

## Dataset Information

**Source:** Freddie Mac Single-Family Loan-Level Dataset (2023-2024)
- 2M+ loans with 26M+ monthly performance updates across 8 quarters
- Geographic coverage: All 50 US states
- 32+ data fields per loan (FICO, LTV, geography, performance metrics)
- Free for research and educational use

*Note: Raw data files are not included due to size. The dashboard uses optimized cache files for demonstration.*

## Technologies

**Data & Analytics:** Python, pandas, NumPy, SQLite, Jupyter
**Visualization:** Plotly, Streamlit 
**Deployment:** Streamlit Cloud, GitHub, Git LFS
**Performance:** Caching, Parquet optimization

---

## Links

- **Live Dashboard:** https://mokeyzz1-mortgage-risk-dashboardsmortgage-risk-dashboard-6nzvum.streamlit.app
- **GitHub Repository:** https://github.com/mokeyzz1/mortgage-risk-analytics
- **Data Source:** [Freddie Mac Historical Loan Performance Data](https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset)

---