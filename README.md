# Mortgage Risk Analytics Platform

Analytics platform for early detection of mortgage delinquency risk, built using Freddie Mac loan-level data (2023–2024).

**[Live Dashboard](https://mokeyzz1-mortgage-risk-dashboardsmortgage-risk-dashboard-6nzvum.streamlit.app)** | [Analysis Notebook](notebooks/01_mortgage_risk_analysis.ipynb) | [GitHub Repository](https://github.com/mokeyzz1/mortgage-risk-analytics)

---

## Overview

This project provides data-driven insights to identify high-risk loans before serious delinquency occurs. Using real Freddie Mac data from 2023–2024, the system processes more than 2 million loans and 26 million monthly performance records to support proactive risk management and underwriting decisions.  

**Target Users:** Mortgage lenders, credit policy teams, underwriters, risk managers, financial analysts  

---

## Key Features

**Interactive Dashboard**
- Real-time portfolio monitoring across 2M+ loans  
- Loan-level risk calculator with adjustable parameters  
- Geographic risk mapping and state-level delinquency analysis  

**Risk Modeling**
- Automated loan classification (High / Medium / Low risk)  
- Multi-factor risk assessment using credit scores, DTI ratios, and LTV ratios  
- Model validation with performance tracking  

**Technical Performance**
- Optimized caching: dashboard load times reduced from 30–60s → 1–3s  
- Scalable cloud deployment with zero downtime  
- Efficient architecture capable of handling millions of records  

---

## Technical Architecture

| Component            | Technology                  | Purpose                                  |
|----------------------|-----------------------------|------------------------------------------|
| **Data Processing**  | Python, pandas, SQLite      | ETL pipelines and data transformation    |
| **Analytics Engine** | Jupyter, NumPy, statistical modeling | Risk analysis and model development |
| **Visualization**    | Plotly, Streamlit           | Interactive charts and dashboards        |
| **Database**         | SQLite, optimized queries   | Structured storage and retrieval         |
| **Deployment**       | Streamlit Cloud, GitHub     | Hosting, version control, and CI/CD      |
| **Performance**      | Parquet, caching            | Optimized data access and load speed     |

---

## Project Structure


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

**Key Outcomes:**  
- **Risk Detection:** Achieved **42.1% recall**, meaning the framework correctly identifies 42% of true high-risk loans — a **5× improvement** compared to random selection.  
- **Operational Efficiency:** By focusing on only ~3.6% of loans, the system reduces review workload by **95%**, enabling lenders to reallocate resources more effectively.  
- **Business Value:** Early identification of at-risk loans supports proactive borrower outreach and loss prevention, with the potential to save **millions in foreclosure costs annually**.  
- **Performance Optimization:** Dashboard loading time improved from **30–60 seconds to 1–3 seconds** (over **2000% faster**) through caching and Parquet optimization.  
- **Coverage:** Analysis spans **2M+ loans across 8 quarters (2023–2024)** with full coverage across all 50 U.S. states.  

---

## Quick Start

**[View Live Dashboard](https://mokeyzz1-mortgage-risk-dashboardsmortgage-risk-dashboard-6nzvum.streamlit.app)** — instant access with preloaded data.  

**Run Locally:**  
```bash
git clone https://github.com/mokeyzz1/mortgage-risk-analytics.git
cd mortgage-risk-analytics
pip install -r requirements.txt
streamlit run dashboards/mortgage_risk_dashboard.py

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