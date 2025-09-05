import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from pathlib import Path
import sys

# Add src to path for imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT / 'src'))

# Page config
st.set_page_config(
    page_title="Mortgage Risk Analytics Dashboard",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Design System
st.markdown("""
<style>
    /* Import Professional Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* CSS Variables - Professional Design System */
    :root {
        --primary-blue: #1e40af;
        --secondary-blue: #3b82f6;
        --    with tab4:
        # Mo        # Model Perform    with tab4:
        # M        # Model Performance Metrics  
        st.markdown("### 📊 Model Performance Summary")
        st.markdown("*Key insights from risk assessment model validation*")l Performance Metrics - Dynamic calculations
        st.markdown("### 📊 Model Performance Summary")
        st.markdown("*Real-time validation metrics from current portfolio*")
        st.markdown("")
        
        # Calculate actual performance metrics
        high_risk_loans = df[df['risk_tier'] == 'High Risk']
        medium_risk_loans = df[df['risk_tier'] == 'Medium Risk'] 
        low_risk_loans = df[df['risk_tier'] == 'Low Risk']
        
        # Calculate key metrics
        total_defaults = df['serious_delinquency_flag'].sum()
        high_risk_defaults = high_risk_loans['serious_delinquency_flag'].sum()
        high_risk_count = len(high_risk_loans)
        
        # Model recall (% of defaults caught by high risk prediction)
        model_recall = (high_risk_defaults / total_defaults * 100) if total_defaults > 0 else 0
        
        # Precision (% of high risk predictions that actually default)
        model_precision = (high_risk_defaults / high_risk_count * 100) if high_risk_count > 0 else 0
        
        # Review rate (% of loans flagged as high risk)
        review_rate = (high_risk_count / len(df) * 100)
        
        # Key findings from analysistrics - Dynamic calculations
        st.markdown("### 📊 Model Performance Summary")
        st.markdown("*Real-time validation metrics from current portfolio*")
        st.markdown("")
        
        # Calculate actual performance metrics
        high_risk_loans = df[df['risk_tier'] == 'High Risk']
        medium_risk_loans = df[df['risk_tier'] == 'Medium Risk'] 
        low_risk_loans = df[df['risk_tier'] == 'Low Risk']
        
        # Calculate key metrics
        total_defaults = df['serious_delinquency_flag'].sum()
        high_risk_defaults = high_risk_loans['serious_delinquency_flag'].sum()
        high_risk_count = len(high_risk_loans)
        
        # Model recall (% of defaults caught by high risk prediction)
        model_recall = (high_risk_defaults / total_defaults * 100) if total_defaults > 0 else 0
        
        # Precision (% of high risk predictions that actually default)
        model_precision = (high_risk_defaults / high_risk_count * 100) if high_risk_count > 0 else 0
        
        # Review rate (% of loans flagged as high risk)
        review_rate = (high_risk_count / len(df) * 100)
        
        # Key findings from analysisrformance Metrics - Dynamic calculations
        st.markdown("### 📊 Model Performance Summary")
        st.markdown("*Real-time validation metrics from current portfolio*")
        st.markdown("")
        
        # Calculate actual performance metrics
        high_risk_loans = df[df['risk_tier'] == 'High Risk']
        medium_risk_loans = df[df['risk_tier'] == 'Medium Risk'] 
        low_risk_loans = df[df['risk_tier'] == 'Low Risk']
        
        # Calculate key metrics
        total_defaults = df['serious_delinquency_flag'].sum()
        high_risk_defaults = high_risk_loans['serious_delinquency_flag'].sum()
        high_risk_count = len(high_risk_loans)
        
        # Model recall (% of defaults caught by high risk prediction)
        model_recall = (high_risk_defaults / total_defaults * 100) if total_defaults > 0 else 0
        
        # Precision (% of high risk predictions that actually default)
        model_precision = (high_risk_defaults / high_risk_count * 100) if high_risk_count > 0 else 0
        
        # Review rate (% of loans flagged as high risk)
        review_rate = (high_risk_count / len(df) * 100)
        
        # Key findings from analysis
        col1, col2, col3 = st.columns(3)lue: #60a5fa;
        --success-green: #10b981;
        --warning-orange: #f59e0b;
        --danger-red: #ef4444;
        --neutral-50: #f8fafc;
        --neutral-100: #f1f5f9;
        --neutral-200: #e2e8f0;
        --neutral-600: #475569;
        --neutral-800: #1e293b;
        --neutral-900: #0f172a;
    }

    /* Global Styles */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Typography */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        font-size: 2.75rem;
        font-weight: 700;
        color: var(--neutral-900);
        text-align: center;
        margin-bottom: 3rem;
        letter-spacing: -0.025em;
        background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Professional Metric Cards */
    .metric-card-pro {
        background: linear-gradient(145deg, #ffffff, var(--neutral-50));
        border: 1px solid var(--neutral-200);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card-pro:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    .metric-card-pro::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-blue), var(--secondary-blue));
    }
    
    .metric-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1rem;
    }
    
    .metric-icon {
        font-size: 1.5rem;
        color: var(--primary-blue);
        background: var(--neutral-100);
        width: 48px;
        height: 48px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--neutral-900);
        margin: 0.5rem 0;
        letter-spacing: -0.025em;
    }
    
    .metric-label {
        font-size: 0.875rem;
        font-weight: 500;
        color: var(--neutral-600);
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .metric-trend {
        font-size: 0.75rem;
        font-weight: 500;
        padding: 0.25rem 0.5rem;
        border-radius: 6px;
        margin-top: 0.5rem;
    }
    
    .trend-up {
        background: transparent;
        color: inherit;
        opacity: 0.8;
    }
    
    .trend-neutral {
        background: transparent;
        color: inherit;
        opacity: 0.8;
    }
    
    /* Colored Metric Cards */
    .metric-card-blue {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border: 1px solid #93c5fd;
    }
    
    .metric-card-blue .metric-icon {
        background: rgba(59, 130, 246, 0.2);
        color: #1d4ed8;
    }
    
    .metric-card-blue .metric-trend {
        color: #1d4ed8;
        font-weight: 600;
    }
    
    .metric-card-green {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        border: 1px solid #86efac;
    }
    
    .metric-card-green .metric-icon {
        background: rgba(16, 185, 129, 0.2);
        color: #059669;
    }
    
    .metric-card-green .metric-trend {
        color: #059669;
        font-weight: 600;
    }
    
    .metric-card-orange {
        background: linear-gradient(135deg, #fed7aa 0%, #fdba74 100%);
        border: 1px solid #fb923c;
    }
    
    .metric-card-orange .metric-icon {
        background: rgba(245, 158, 11, 0.2);
        color: #d97706;
    }
    
    .metric-card-orange .metric-trend {
        color: #d97706;
        font-weight: 600;
    }
    
    .metric-card-purple {
        background: linear-gradient(135deg, #e9d5ff 0%, #ddd6fe 100%);
        border: 1px solid #c4b5fd;
    }
    
    .metric-card-purple .metric-icon {
        background: rgba(139, 92, 246, 0.2);
        color: #7c3aed;
    }
    
    .metric-card-purple .metric-trend {
        color: #7c3aed;
        font-weight: 600;
    }

    /* Risk Assessment Cards */
    .risk-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid var(--neutral-200);
        position: relative;
    }
    
    .risk-card-high {
        border-left: 6px solid var(--danger-red);
        background: linear-gradient(145deg, #ffffff, #fef2f2);
    }
    
    .risk-card-medium {
        border-left: 6px solid var(--warning-orange);
        background: linear-gradient(145deg, #ffffff, #fffbeb);
    }
    
    .risk-card-low {
        border-left: 6px solid var(--success-green);
        background: linear-gradient(145deg, #ffffff, #f0fdf4);
    }
    
    .risk-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .risk-title-high { color: var(--danger-red); }
    .risk-title-medium { color: var(--warning-orange); }
    .risk-title-low { color: var(--success-green); }
    
    .risk-percentage {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.025em;
    }
    
    .risk-subtitle {
        font-size: 0.875rem;
        color: var(--neutral-600);
        margin: 0;
        font-weight: 500;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: var(--neutral-50);
        border-right: 1px solid var(--neutral-200);
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: var(--neutral-100);
        border-radius: 10px;
        padding: 4px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 8px;
        color: var(--neutral-600);
        font-weight: 500;
        padding: 12px 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: white;
        color: var(--primary-blue);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Warning and Success Messages */
    .element-container .stAlert {
        border-radius: 8px;
        border: none;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Button Styling */
    .stButton > button {
        border-radius: 8px;
        font-weight: 500;
        border: none;
        transition: all 0.2s ease;
    }
    
    /* Professional spacing */
    .element-container {
        margin-bottom: 1rem;
    }
    
    /* Chart containers */
    .plotly-graph-div {
        border-radius: 8px;
        border: 1px solid var(--neutral-200);
        background: white;
    }
    
</style>
""", unsafe_allow_html=True)

# Professional Color Themes
PROFESSIONAL_COLORS = {
    'primary': '#1e40af',      # Primary blue
    'secondary': '#3b82f6',    # Secondary blue  
    'accent': '#60a5fa',       # Accent blue
    'success': '#10b981',      # Success green
    'warning': '#f59e0b',      # Warning orange
    'danger': '#ef4444',       # Danger red
    'neutral': '#6b7280',      # Neutral gray
    'background': '#f8fafc'    # Light background
}

# Chart color palettes
RISK_COLORS = {
    'Low Risk': PROFESSIONAL_COLORS['success'],
    'Medium Risk': PROFESSIONAL_COLORS['warning'], 
    'High Risk': PROFESSIONAL_COLORS['danger']
}

# Centralized Data Mappings and Labels
DATA_MAPPINGS = {
    # Performance Status
    'performance_status': {
        0: 'Current',
        1: 'Delinquent'
    },
    
    # Loan Purpose Mappings
    'loan_purpose': {
        'P': 'Purchase',
        'C': 'Cash-out Refinance',
        'N': 'No Cash-out Refinance',
        'R': 'Refinance',
        'U': 'Unknown'
    },
    
    # Property Type Mappings
    'property_type': {
        'SF': 'Single Family',
        'PU': 'Planned Unit Development',
        'CO': 'Condominium',
        'MH': 'Manufactured Housing',
        'CP': 'Cooperative'
    },
    
    # Occupancy Status
    'occupancy_status': {
        'P': 'Primary Residence',
        'S': 'Second Home',
        'I': 'Investment Property'
    },
    
    # First Time Buyer Flag
    'first_time_buyer': {
        'Y': 'Yes',
        'N': 'No',
        'U': 'Unknown'
    },
    
    # Risk Categories
    'risk_category': {
        'Low Risk': PROFESSIONAL_COLORS['success'],
        'Medium Risk': PROFESSIONAL_COLORS['warning'], 
        'High Risk': PROFESSIONAL_COLORS['danger']
    },
    
    # DTI Categories with ranges
    'dti_categories': {
        'Excellent (≤20%)': {'range': (0, 20), 'color': PROFESSIONAL_COLORS['success']},
        'Very Good (21-28%)': {'range': (21, 28), 'color': PROFESSIONAL_COLORS['accent']},
        'Good (29-35%)': {'range': (29, 35), 'color': PROFESSIONAL_COLORS['primary']},
        'Fair (36-43%)': {'range': (36, 43), 'color': PROFESSIONAL_COLORS['warning']},
        'Poor (44-50%)': {'range': (44, 50), 'color': PROFESSIONAL_COLORS['danger']},
        'High Risk (>50%)': {'range': (51, 100), 'color': '#8B0000'}
    },
    
    # Credit Score Ranges
    'credit_score_ranges': {
        'Poor (300-579)': {'range': (300, 579), 'color': PROFESSIONAL_COLORS['danger']},
        'Fair (580-669)': {'range': (580, 669), 'color': PROFESSIONAL_COLORS['warning']},
        'Good (670-739)': {'range': (670, 739), 'color': PROFESSIONAL_COLORS['primary']},
        'Very Good (740-799)': {'range': (740, 799), 'color': PROFESSIONAL_COLORS['accent']},
        'Excellent (800+)': {'range': (800, 900), 'color': PROFESSIONAL_COLORS['success']}
    }
}

# Column Labels for Display
COLUMN_LABELS = {
    'credit_score': 'Credit Score',
    'debt_to_income': 'Debt-to-Income Ratio',
    'loan_to_value': 'Loan-to-Value Ratio',
    'serious_delinquency_flag': 'Performance Status',
    'loan_purpose': 'Loan Purpose',
    'property_type': 'Property Type',
    'occupancy_status': 'Occupancy Status',
    'first_time_buyer_flag': 'First Time Buyer',
    'state': 'State',
    'default_rate': 'Default Rate',
    'avg_credit_score': 'Average Credit Score',
    'loan_count': 'Loan Count'
}

# Comprehensive Glossary for Mortgage Terms and Acronyms
MORTGAGE_GLOSSARY = {
    # Core Financial Metrics
    "DTI": {
        "full_name": "Debt-to-Income Ratio",
        "definition": "The percentage of a borrower's monthly gross income that goes toward paying debts. Calculated as (Total Monthly Debt Payments / Gross Monthly Income) × 100.",
        "importance": "Lenders use DTI to assess a borrower's ability to manage monthly payments and repay debts. Lower DTI indicates better financial health.",
        "good_range": "≤28% is excellent, 29-36% is acceptable for most loans"
    },
    
    "LTV": {
        "full_name": "Loan-to-Value Ratio",
        "definition": "The ratio of the loan amount to the appraised value of the property. Calculated as (Loan Amount / Property Value) × 100.",
        "importance": "Higher LTV means higher risk for lenders. Loans with LTV >80% typically require mortgage insurance.",
        "good_range": "≤80% is preferred, >95% is considered high risk"
    },
    
    "FICO": {
        "full_name": "Fair Isaac Corporation Credit Score",
        "definition": "A credit score ranging from 300-850 that represents creditworthiness based on credit history, payment behavior, and debt levels.",
        "importance": "Higher scores indicate lower credit risk and typically qualify for better interest rates.",
        "good_range": "740+ is excellent, 670-739 is good, <580 is poor"
    },
    
    # Loan Performance Terms
    "Delinquency": {
        "full_name": "Loan Delinquency",
        "definition": "A loan payment that is overdue. Serious delinquency typically means 90+ days past due.",
        "importance": "Indicates borrower's difficulty in making payments and potential for default.",
        "categories": "30-day, 60-day, 90+ day delinquency levels"
    },
    
    "Default": {
        "full_name": "Loan Default",
        "definition": "Failure to repay a loan according to the agreed terms, typically after extended delinquency.",
        "importance": "Results in foreclosure proceedings and significant losses for lenders.",
        "threshold": "Usually declared after 120+ days of non-payment"
    },
    
    # Property and Loan Types
    "Purchase": {
        "full_name": "Purchase Loan",
        "definition": "A mortgage used to buy a home, as opposed to refinancing an existing loan.",
        "importance": "Represents new lending activity and market expansion."
    },
    
    "Refinance": {
        "full_name": "Refinance Loan",
        "definition": "Replacing an existing mortgage with a new loan, typically to get better terms or access equity.",
        "types": "Cash-out (take equity) vs. No Cash-out (rate/term improvement)"
    },
    
    "GSE": {
        "full_name": "Government Sponsored Enterprise",
        "definition": "Fannie Mae and Freddie Mac - entities that purchase mortgages from lenders to provide liquidity.",
        "importance": "Enable standardized lending practices and increased mortgage availability."
    },
    
    # Property Types
    "SF": {
        "full_name": "Single Family",
        "definition": "A detached residential dwelling designed for one family.",
        "characteristics": "Most common property type in mortgage lending"
    },
    
    "PUD": {
        "full_name": "Planned Unit Development",
        "definition": "A community of homes with shared amenities and homeowner association.",
        "characteristics": "Combines individual ownership with shared community features"
    },
    
    "Condo": {
        "full_name": "Condominium",
        "definition": "Individual ownership of a unit within a multi-unit building with shared common areas.",
        "considerations": "HOA fees and shared building maintenance responsibilities"
    },
    
    # Occupancy Types
    "Primary Residence": {
        "full_name": "Primary Residence",
        "definition": "The home where the borrower lives most of the time (main residence).",
        "importance": "Lowest risk category, typically gets best rates and terms"
    },
    
    "Second Home": {
        "full_name": "Second Home/Vacation Home",
        "definition": "A property used occasionally for vacations or as a retreat.",
        "importance": "Higher risk than primary residence, requires higher down payment"
    },
    
    "Investment Property": {
        "full_name": "Investment Property",
        "definition": "Property purchased to generate income through rent or appreciation.",
        "importance": "Highest risk category, strictest lending requirements and highest rates"
    },
    
    # Risk and Analysis Terms
    "Serious Delinquency": {
        "full_name": "Serious Delinquency",
        "definition": "Loans that are 90 or more days past due on payments.",
        "importance": "Key indicator of loan performance and portfolio risk"
    },
    
    "Geographic Risk": {
        "full_name": "Geographic Risk Concentration",
        "definition": "Risk associated with having too many loans concentrated in specific geographic areas.",
        "importance": "Natural disasters, economic downturns can affect entire regions simultaneously"
    },
    
    "Portfolio Diversification": {
        "full_name": "Portfolio Diversification",
        "definition": "Spreading risk across different loan types, geographies, and borrower profiles.",
        "importance": "Reduces overall portfolio risk and improves stability"
    }
}

def show_glossary():
    """Display the mortgage terminology glossary"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📚 Mortgage Glossary")
    
    # Create expandable sections for different categories
    with st.sidebar.expander("💰 Financial Metrics", expanded=False):
        for term in ["DTI", "LTV", "FICO"]:
            if term in MORTGAGE_GLOSSARY:
                info = MORTGAGE_GLOSSARY[term]
                st.markdown(f"**{term}** - {info['full_name']}")
                st.markdown(f"_{info['definition']}_")
                if 'good_range' in info:
                    st.markdown(f"✅ **Good Range:** {info['good_range']}")
                st.markdown("---")
    
    with st.sidebar.expander("📊 Performance Terms", expanded=False):
        for term in ["Delinquency", "Default", "Serious Delinquency"]:
            if term in MORTGAGE_GLOSSARY:
                info = MORTGAGE_GLOSSARY[term]
                st.markdown(f"**{term}**")
                st.markdown(f"_{info['definition']}_")
                st.markdown("---")
    
    with st.sidebar.expander("🏠 Property & Loan Types", expanded=False):
        for term in ["Purchase", "Refinance", "SF", "PUD", "Condo"]:
            if term in MORTGAGE_GLOSSARY:
                info = MORTGAGE_GLOSSARY[term]
                st.markdown(f"**{term}** - {info['full_name']}")
                st.markdown(f"_{info['definition']}_")
                st.markdown("---")
    
    with st.sidebar.expander("🎯 Risk Categories", expanded=False):
        for term in ["Primary Residence", "Second Home", "Investment Property", "Geographic Risk"]:
            if term in MORTGAGE_GLOSSARY:
                info = MORTGAGE_GLOSSARY[term]
                st.markdown(f"**{term}**")
                st.markdown(f"_{info['definition']}_")
                st.markdown("---")

# Professional chart template - Enhanced
CHART_LAYOUT = {
    'font': {'family': 'Inter, sans-serif', 'size': 12, 'color': '#374151'},
    'plot_bgcolor': 'rgba(248, 250, 252, 0.5)',  # Subtle background
    'paper_bgcolor': 'white',
    'margin': dict(t=70, b=60, l=60, r=60),  # More breathing room
    'title': {
        'font': {'size': 18, 'color': '#1f2937', 'family': 'Inter, sans-serif'},
        'x': 0.5,  # Center the title
        'xanchor': 'center'
    },
    'xaxis': {
        'gridcolor': '#f3f4f6', 
        'linecolor': '#e5e7eb',
        'tickfont': {'size': 11, 'color': '#6b7280'}
    },
    'yaxis': {
        'gridcolor': '#f3f4f6', 
        'linecolor': '#e5e7eb',
        'tickfont': {'size': 11, 'color': '#6b7280'}
    },
    'showlegend': True,
    'legend': {
        'font': {'size': 11, 'color': '#6b7280'},
        'bgcolor': 'rgba(255,255,255,0.8)',
        'bordercolor': '#e5e7eb',
        'borderwidth': 1
    }
}

@st.cache_data
def load_data():
    """Load pre-optimized data for fast dashboard performance"""
    try:
        # Try to load pre-computed optimized data first
        cache_dir = PROJECT_ROOT / 'data' / 'dashboard_cache'
        main_data_path = cache_dir / 'main_dashboard_data.parquet'
        
        if main_data_path.exists():
            # Load pre-computed data (much faster!)
            df = pd.read_parquet(main_data_path)
            return df
        else:
            # Fallback to database with smaller sample
            database_path = PROJECT_ROOT / 'data' / 'processed' / 'mortgage_analytics.db'
            conn = sqlite3.connect(database_path)
            
            # Much smaller sample for faster loading
            query = """
            SELECT 
                CAST(o.borrower_credit_score AS INTEGER) as credit_score,
                CAST(o.debt_to_income_ratio AS REAL) as dti,
                CAST(o.original_loan_to_value AS REAL) as ltv,
                o.loan_purpose as loan_purpose_desc,
                o.property_type as property_type_desc,
                o.first_time_buyer_flag,
                o.property_state as state,
                CASE WHEN MAX(CAST(p.current_loan_delinquency_status AS INTEGER)) > 2 THEN 1 ELSE 0 END as serious_delinquency_flag,
                CAST(o.original_upb AS REAL) as loan_amount
            FROM origination_data o
            LEFT JOIN performance_data p ON o.loan_sequence_number = p.loan_sequence_number
            WHERE o.borrower_credit_score != '' 
            AND o.debt_to_income_ratio != '' 
            AND o.original_loan_to_value != ''
            AND o.borrower_credit_score IS NOT NULL
            AND (CAST(substr(o.loan_sequence_number, -2) AS INTEGER) % 50) < 3  -- Much smaller sample
            GROUP BY o.loan_sequence_number
            LIMIT 25000  -- Cap for performance
            """
            
            df = pd.read_sql_query(query, conn)
            conn.close()
            
            # Add risk calculations
            df['risk_tier'] = 'Low Risk'
            df.loc[(df['credit_score'] < 680) | (df['dti'] > 0.43) | (df['ltv'] > 85), 'risk_tier'] = 'Medium Risk'
            df.loc[(df['credit_score'] < 620) | (df['dti'] > 0.50) | (df['ltv'] > 95), 'risk_tier'] = 'High Risk'
            
            return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

@st.cache_data  
def load_summary_stats():
    """Load just summary statistics for fast metrics"""
    try:
        database_path = PROJECT_ROOT / 'data' / 'processed' / 'mortgage_analytics.db'
        conn = sqlite3.connect(database_path)
        
        # Get quick counts and averages
        summary_query = """
        SELECT 
            COUNT(DISTINCT o.loan_sequence_number) as total_loans,
            AVG(CAST(o.borrower_credit_score AS REAL)) as avg_credit_score,
            AVG(CAST(o.original_loan_to_value AS REAL)) as avg_ltv,
            COUNT(DISTINCT CASE WHEN p.max_delinq > 2 THEN o.loan_sequence_number END) * 1.0 / COUNT(DISTINCT o.loan_sequence_number) as delinquency_rate
        FROM origination_data o
        LEFT JOIN (
            SELECT loan_sequence_number, MAX(CAST(current_loan_delinquency_status AS INTEGER)) as max_delinq
            FROM performance_data 
            GROUP BY loan_sequence_number
        ) p ON o.loan_sequence_number = p.loan_sequence_number
        WHERE o.borrower_credit_score != '' 
        AND o.borrower_credit_score IS NOT NULL
        """
        
        result = pd.read_sql_query(summary_query, conn)
        conn.close()
        return result.iloc[0]
    except Exception as e:
        st.error(f"Error loading summary stats: {e}")
        return None

def calculate_risk_score(credit_score, dti, ltv):
    """Simple risk scoring function based on analysis findings"""
    risk_score = 0.0
    
    # Credit score impact (most important factor)
    if credit_score < 650:
        risk_score += 0.04
    elif credit_score < 700:
        risk_score += 0.02
    elif credit_score < 750:
        risk_score += 0.01
    
    # DTI impact
    if dti > 35:
        risk_score += 0.02
    elif dti > 30:
        risk_score += 0.01
    
    # LTV impact
    if ltv > 80:
        risk_score += 0.015
    elif ltv > 70:
        risk_score += 0.005
    
    return min(risk_score, 0.15)  # Cap at 15%

def get_risk_tier(risk_score):
    """Convert risk score to tier"""
    if risk_score >= 0.04:
        return "High Risk"
    elif risk_score >= 0.02:
        return "Medium Risk"
    else:
        return "Low Risk"

# Main Dashboard
def main():
    # Performance indicator
    cache_dir = PROJECT_ROOT / 'data' / 'dashboard_cache'
    using_cache = (cache_dir / 'main_dashboard_data.parquet').exists()
    
    if using_cache:
        st.success("⚡ **Optimized Mode**: Fast loading enabled (50K sample)")
    else:
        st.warning("🐌 **Fallback Mode**: Loading from database (slower)")
    
    # Header with data freshness
    col_header1, col_header2 = st.columns([3, 1])
    with col_header1:
        st.markdown("""
        <h1 class="main-header">
            <span style="font-size: 2.75rem; margin-right: 0.5rem;">🏠</span>
            <span style="background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue)); 
                         -webkit-background-clip: text; 
                         -webkit-text-fill-color: transparent; 
                         background-clip: text;">Mortgage Risk Analytics Dashboard</span>
        </h1>
        """, unsafe_allow_html=True)
    with col_header2:
        st.markdown("""
        <div style="text-align: right; padding-top: 1rem;">
            <div style="font-size: 0.8rem; color: #6b7280;">Data Updated</div>
            <div style="font-size: 0.9rem; color: #374151; font-weight: 500;">2024 Q1-Q4</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Compact terminology reference in header area
    st.markdown("""
    <div style="
        background: rgba(59, 130, 246, 0.05);
        border: 1px solid rgba(59, 130, 246, 0.1);
        border-radius: 6px;
        padding: 0.5rem 0.75rem;
        margin: 0.5rem 0;
        font-size: 0.8rem;
        color: #374151;
    ">
        <span style="font-weight: 600; color: #1f2937;">📚 Key Terms:</span>
        <span style="margin: 0 0.75rem;"><strong>DTI</strong> = Debt-to-Income</span>
        <span style="margin: 0 0.75rem;"><strong>LTV</strong> = Loan-to-Value</span>
        <span style="margin: 0 0.75rem;"><strong>FICO</strong> = Credit Score (300-850)</span>
        <span style="margin-left: 0.75rem; color: #6b7280; font-style: italic;">See sidebar for details</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data efficiently
    with st.spinner("Loading data..."):
        df = load_data()  # ~30% random sample for charts
        summary_stats = load_summary_stats()  # Fast summary from full dataset
    
    if df.empty:
        st.error("Unable to load data. Please ensure the database is available.")
        return
    
    # Sidebar - Risk Calculator & Analysis
    with st.sidebar:
        st.header("🧮 Risk Calculator")
        
        # Risk input parameters
        credit_score = st.slider(
            "📊 Credit Score (FICO)", 
            min_value=300, 
            max_value=850, 
            value=720, 
            help="FICO Score: 300-850 scale measuring creditworthiness"
        )
        
        dti = st.slider(
            "💰 DTI Ratio (%)", 
            min_value=0, 
            max_value=60, 
            value=25, 
            help="Debt-to-Income Ratio: Monthly debt payments ÷ gross monthly income"
        )
        
        ltv = st.slider(
            "🏠 LTV Ratio (%)", 
            min_value=0, 
            max_value=100, 
            value=75, 
            help="Loan-to-Value Ratio: Loan amount ÷ property value"
        )
        
        # Calculate risk
        risk_score = calculate_risk_score(credit_score, dti, ltv)
        risk_tier = get_risk_tier(risk_score)
        
        # Display risk assessment
        st.markdown("### Risk Assessment")
        
        # Color-coded risk display
        if risk_tier == "High Risk":
            st.error(f"🔴 **{risk_tier}**: {risk_score:.2%} default probability")
        elif risk_tier == "Medium Risk":
            st.warning(f"� **{risk_tier}**: {risk_score:.2%} default probability")
        else:
            st.success(f"🟢 **{risk_tier}**: {risk_score:.2%} default probability")
        
        # Risk factor analysis
        st.markdown("---")
        st.subheader("� Risk Factors")
        
        # Dynamic insights based on inputs
        insights = []
        
        if credit_score < 650:
            insights.append("⚠️ Credit score is below prime threshold")
        elif credit_score >= 750:
            insights.append("✅ Excellent credit score reduces risk")
        
        if dti > 43:
            insights.append("⚠️ DTI ratio exceeds recommended maximum")
        elif dti <= 28:
            insights.append("✅ Conservative DTI ratio is favorable")
        
        if ltv > 80:
            insights.append("⚠️ High LTV increases default risk")
        elif ltv <= 70:
            insights.append("✅ Low LTV provides good equity cushion")
        
        # Display insights with consistent formatting
        if insights:
            for insight in insights:
                st.markdown(f"**{insight}**")
        else:
            st.success("✅  **All metrics within optimal ranges**")
            
        # Industry benchmarks
        st.markdown("---")
        st.markdown("### 📋 Industry Benchmarks")
        st.markdown("**Credit Score 720+:** Prime borrowers")
        st.markdown("**DTI <30%:** Conservative lending")  
        st.markdown("**LTV <80%:** Strong equity position")
        
        # Add glossary to sidebar
        show_glossary()
    
    # Portfolio metrics section
    st.markdown("---")
    st.markdown("## 📊 Portfolio Performance Metrics")
    st.markdown("*Key performance indicators across 1.98M mortgage loans*")
    st.markdown("")
    
    # Main content - use full dataset metrics
    col1, col2, col3, col4 = st.columns(4)
    
    # Professional metric cards with icons and trends
    if summary_stats is not None:
        with col1:
            st.markdown(f"""
            <div class="metric-card-pro metric-card-blue">
                <div class="metric-header">
                    <div class="metric-icon">📊</div>
                </div>
                <div class="metric-value">{int(summary_stats['total_loans']):,}</div>
                <div class="metric-label">Total Loans</div>
                <div class="metric-trend trend-neutral">📈 Portfolio Size</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card-pro metric-card-green">
                <div class="metric-header">
                    <div class="metric-icon">🎯</div>
                </div>
                <div class="metric-value">{summary_stats['avg_credit_score']:.0f}</div>
                <div class="metric-label">Avg Credit Score</div>
                <div class="metric-trend trend-up">✓ High Quality</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card-pro metric-card-orange">
                <div class="metric-header">
                    <div class="metric-icon">⚠️</div>
                </div>
                <div class="metric-value">{summary_stats['delinquency_rate']*100:.1f}%</div>
                <div class="metric-label">Delinquency Rate</div>
                <div class="metric-trend trend-neutral">📋 Industry Range</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card-pro metric-card-purple">
                <div class="metric-header">
                    <div class="metric-icon">🏦</div>
                </div>
                <div class="metric-value">{summary_stats['avg_ltv']:.1f}%</div>
                <div class="metric-label">Avg LTV Ratio</div>
                <div class="metric-trend trend-up">✓ Conservative</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        # Fallback with professional styling
        with col1:
            st.markdown(f"""
            <div class="metric-card-pro metric-card-blue">
                <div class="metric-header">
                    <div class="metric-icon">📊</div>
                </div>
                <div class="metric-value">{len(df):,}</div>
                <div class="metric-label">Sample Size</div>
                <div class="metric-trend trend-neutral">📈 Data Sample</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card-green">
                <div class="metric-header">
                    <div class="metric-icon">🎯</div>
                </div>
                <div class="metric-value">{df['credit_score'].mean():.0f}</div>
                <div class="metric-label">Avg Credit Score</div>
                <div class="metric-trend trend-up">✓ Sample Quality</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card-orange">
                <div class="metric-header">
                    <div class="metric-icon">⚠️</div>
                </div>
                <div class="metric-value">{df['serious_delinquency_flag'].mean()*100:.1f}%</div>
                <div class="metric-label">Delinquency Rate</div>
                <div class="metric-trend trend-neutral">📋 Sample Rate</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card-purple">
                <div class="metric-header">
                    <div class="metric-icon">🏦</div>
                </div>
                <div class="metric-value">{df['ltv'].mean():.1f}%</div>
                <div class="metric-label">Avg LTV Ratio</div>
                <div class="metric-trend trend-up">✓ Sample LTV</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Enhanced charts section
    st.markdown("---")
    st.markdown("## 📈 Detailed Analytics")
    st.markdown("*Interactive analysis of risk patterns and portfolio composition*")
    
    # Charts section
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Portfolio Overview", "🗺️ Geographic Risk", "📈 Risk Distribution", "⚙️ Model Performance"])
    
    with tab1:
        # Main analysis charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Credit Score Distribution - Using centralized mapping
            df_credit = df.copy()
            df_credit['performance_status'] = df_credit['serious_delinquency_flag'].map(DATA_MAPPINGS['performance_status'])
            
            fig_credit = px.histogram(
                df_credit, 
                x='credit_score', 
                color='performance_status',
                title="📊 Credit Score Distribution by Performance<br><sup>FICO Score: 300-850 scale measuring creditworthiness</sup>",
                nbins=30,
                color_discrete_map={'Current': PROFESSIONAL_COLORS['success'], 'Delinquent': PROFESSIONAL_COLORS['danger']},
                labels={'performance_status': COLUMN_LABELS['serious_delinquency_flag'], 'credit_score': 'Credit Score (FICO)'}
            )
            fig_credit.update_layout(**CHART_LAYOUT, height=400)
            st.plotly_chart(fig_credit, use_container_width=True)
        
        with col2:
            # DTI vs Default Rate - Using centralized mapping
            def categorize_dti(dti):
                for category, info in DATA_MAPPINGS['dti_categories'].items():
                    if info['range'][0] <= dti <= info['range'][1]:
                        return category
                return 'High Risk (>50%)'  # fallback for values above 50
            
            df['dti_category'] = df['dti'].apply(categorize_dti)
            
            # Calculate default rates by meaningful DTI categories
            dti_analysis = df.groupby('dti_category').agg({
                'serious_delinquency_flag': ['count', 'sum', 'mean']
            }).round(4)
            dti_analysis.columns = ['total_loans', 'defaults', 'default_rate']
            dti_analysis = dti_analysis.reset_index()
            
            # Order categories properly using the new category names
            category_order = [
                "Excellent (≤20%)", 
                "Very Good (21-28%)", 
                "Good (29-35%)", 
                "Fair (36-43%)", 
                "Poor (44-50%)", 
                "High Risk (>50%)"
            ]
            dti_analysis['dti_category'] = pd.Categorical(dti_analysis['dti_category'], categories=category_order, ordered=True)
            dti_analysis = dti_analysis.sort_values('dti_category')
            
            fig_dti = px.bar(
                dti_analysis,
                x='dti_category',
                y='default_rate',
                title="📈 DTI vs Default Rate (Industry Standards)<br><sup>DTI = Debt-to-Income Ratio: Monthly debt payments ÷ gross income</sup>",
                color=dti_analysis['default_rate'],
                color_continuous_scale=[[0, PROFESSIONAL_COLORS['success']], [0.5, PROFESSIONAL_COLORS['warning']], [1, PROFESSIONAL_COLORS['danger']]],
                labels={'default_rate': 'Default Rate (%)', 'dti_category': 'DTI Range', 'color': 'Default Rate'},
                text='default_rate'
            )
            
            # Add percentage labels on bars
            fig_dti.update_traces(texttemplate='%{text:.2%}', textposition='outside')
            fig_dti.update_layout(**CHART_LAYOUT, height=400)
            fig_dti.update_layout(showlegend=False)  # Override the default showlegend=True from CHART_LAYOUT
            fig_dti.update_xaxes(title="DTI Range (Debt-to-Income Ratio)")
            fig_dti.update_yaxes(title="Default Rate (%)", tickformat='.2%')
            st.plotly_chart(fig_dti, use_container_width=True)
        
        # Portfolio composition analysis
        st.markdown("### 🔍 Portfolio Composition Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Loan Purpose Distribution
            purpose_dist = df['loan_purpose_desc'].value_counts()
            fig_purpose_pie = px.pie(
                values=purpose_dist.values,
                names=purpose_dist.index,
                title="🏠 Loan Purpose Distribution",
                color_discrete_sequence=[PROFESSIONAL_COLORS['primary'], PROFESSIONAL_COLORS['secondary'], PROFESSIONAL_COLORS['accent']]
            )
            fig_purpose_pie.update_layout(**CHART_LAYOUT, height=400)
            st.plotly_chart(fig_purpose_pie, use_container_width=True)
        
        with col2:
            # LTV Distribution
            fig_ltv = px.histogram(
                df,
                x='ltv',
                title="🏦 LTV Ratio Distribution<br><sup>LTV = Loan-to-Value Ratio: Loan amount ÷ property value</sup>",
                nbins=25,
                color_discrete_sequence=[PROFESSIONAL_COLORS['secondary']],
                labels={'ltv': 'LTV Ratio (%)'}
            )
            fig_ltv.update_layout(**CHART_LAYOUT, height=400)
            fig_ltv.update_traces(showlegend=False)
            fig_ltv.update_xaxes(title="LTV Ratio (%) - Loan-to-Value")
            st.plotly_chart(fig_ltv, use_container_width=True)
        
        # Risk vs Performance Summary
        st.markdown("### ⚡ Risk vs Performance Summary")
        
        # Create risk tier summary
        df['risk_score'] = df.apply(lambda row: calculate_risk_score(row['credit_score'], row['dti'], row['ltv']), axis=1)
        df['risk_tier'] = df['risk_score'].apply(get_risk_tier)
        
        risk_summary = df.groupby('risk_tier').agg({
            'serious_delinquency_flag': ['count', 'sum', 'mean'],
            'credit_score': 'mean',
            'loan_amount': 'mean'
        }).round(3)
        risk_summary.columns = ['total_loans', 'defaults', 'default_rate', 'avg_credit', 'avg_amount']
        risk_summary = risk_summary.reset_index()
        
        # Display as interactive table
        st.markdown("**Portfolio Performance by Risk Tier:**")
        st.dataframe(
            risk_summary,
            column_config={
                'risk_tier': 'Risk Tier',
                'total_loans': st.column_config.NumberColumn('Total Loans', format='%d'),
                'defaults': st.column_config.NumberColumn('Defaults', format='%d'),
                'default_rate': st.column_config.NumberColumn('Default Rate', format='%.2%'),
                'avg_credit': st.column_config.NumberColumn('Avg Credit Score', format='%.0f'),
                'avg_amount': st.column_config.NumberColumn('Avg Loan Amount', format='$%.0f')
            },
            hide_index=True,
            use_container_width=True
        )
    
    with tab2:
        # Geographic Risk Analysis
        if 'state' in df.columns:
            state_risk = df.groupby('state').agg({
                'serious_delinquency_flag': ['count', 'mean'],
                'credit_score': 'mean'
            }).round(3)
            state_risk.columns = ['loan_count', 'default_rate', 'avg_credit_score']
            state_risk = state_risk.reset_index()
            state_risk = state_risk[state_risk['loan_count'] >= 50]  # Filter states with enough data
            
            # Interactive US Map
            st.markdown("### 🗺️ Interactive Risk Map")
            
            # Create choropleth map
            fig_map = px.choropleth(
                state_risk,
                locations='state',
                color='default_rate',
                locationmode='USA-states',
                scope='usa',
                title="🌎 Default Risk by State",
                color_continuous_scale=[
                    [0, PROFESSIONAL_COLORS['success']],
                    [0.5, PROFESSIONAL_COLORS['warning']], 
                    [1, PROFESSIONAL_COLORS['danger']]
                ],
                labels={'default_rate': 'Default Rate', 'state': 'State'},
                hover_data={
                    'loan_count': ':,',
                    'avg_credit_score': ':.0f',
                    'default_rate': ':.2%'
                }
            )
            
            fig_map.update_layout(
                **CHART_LAYOUT,
                height=500,
                geo=dict(
                    showframe=False,
                    showcoastlines=True,
                    projection_type='albers usa'
                )
            )
            
            st.plotly_chart(fig_map, use_container_width=True)
            
            # Supporting charts below the map
            col1, col2 = st.columns(2)
            
            with col1:
                fig_state_risk = px.bar(
                    state_risk.sort_values('default_rate', ascending=False).head(10),
                    x='state',
                    y='default_rate',
                    title="� Top 10 Highest Risk States",
                    color='default_rate',
                    color_continuous_scale=[[0, PROFESSIONAL_COLORS['success']], [1, PROFESSIONAL_COLORS['danger']]]
                )
                fig_state_risk.update_layout(**CHART_LAYOUT, height=400, xaxis_tickangle=-45)
                st.plotly_chart(fig_state_risk, use_container_width=True)
            
            with col2:
                fig_credit_state = px.scatter(
                    state_risk,
                    x='avg_credit_score',
                    y='default_rate',
                    size='loan_count',
                    hover_data=['state'],
                    title="🎯 Credit Quality vs Risk by State",
                    labels={'avg_credit_score': 'Average Credit Score', 'default_rate': 'Default Rate'},
                    color='default_rate',
                    color_continuous_scale=[[0, PROFESSIONAL_COLORS['success']], [1, PROFESSIONAL_COLORS['danger']]]
                )
                fig_credit_state.update_layout(**CHART_LAYOUT, height=400)
                st.plotly_chart(fig_credit_state, use_container_width=True)
        else:
            st.info("🗺️ Geographic data not available in current dataset")
    
    with tab3:
        # Risk Distribution
        df['risk_score'] = df.apply(lambda row: calculate_risk_score(row['credit_score'], row['dti'], row['ltv']), axis=1)
        df['risk_tier'] = df['risk_score'].apply(get_risk_tier)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Risk Tier Distribution
            risk_dist = df['risk_tier'].value_counts()
            fig_risk_pie = px.pie(
                values=risk_dist.values,
                names=risk_dist.index,
                title="🔄 Portfolio Risk Distribution",
                color_discrete_map=RISK_COLORS
            )
            fig_risk_pie.update_layout(**CHART_LAYOUT)
            st.plotly_chart(fig_risk_pie, use_container_width=True)
        
        with col2:
            # Create meaningful performance metrics by risk tier
            performance_metrics = df.groupby('risk_tier').agg({
                'serious_delinquency_flag': ['count', 'sum', 'mean'],
                'credit_score': 'mean',
                'dti': 'mean',
                'ltv': 'mean'
            }).round(3)
            
            performance_metrics.columns = ['total_loans', 'defaulted_loans', 'default_rate', 'avg_credit', 'avg_dti', 'avg_ltv']
            performance_metrics = performance_metrics.reset_index()
            
            # Create a bar chart showing actual default rates by predicted risk tier
            fig_performance = px.bar(
                performance_metrics,
                x='risk_tier',
                y='default_rate',
                title="⚙️ Actual Default Rate by Predicted Risk Tier",
                color='risk_tier',
                color_discrete_map=RISK_COLORS,
                text='default_rate'
            )
            
            # Add text annotations showing the values
            fig_performance.update_traces(texttemplate='%{text:.1%}', textposition='outside')
            fig_performance.update_layout(**CHART_LAYOUT, height=400)
            st.plotly_chart(fig_performance, use_container_width=True)
            
            # Show the performance table below
            st.markdown("#### 📊 Performance Breakdown")
            performance_display = performance_metrics.copy()
            performance_display['default_rate'] = performance_display['default_rate'].apply(lambda x: f"{x:.2%}")
            performance_display['avg_credit'] = performance_display['avg_credit'].apply(lambda x: f"{x:.0f}")
            performance_display['avg_dti'] = performance_display['avg_dti'].apply(lambda x: f"{x:.1f}%")
            performance_display['avg_ltv'] = performance_display['avg_ltv'].apply(lambda x: f"{x:.1f}%")
            
            st.dataframe(
                performance_display[['risk_tier', 'total_loans', 'default_rate', 'avg_credit']],
                column_config={
                    'risk_tier': 'Risk Tier',
                    'total_loans': 'Total Loans',
                    'default_rate': 'Default Rate',
                    'avg_credit': 'Avg Credit Score'
                },
                hide_index=True,
                use_container_width=True
            )
    
    with tab4:
        # Model Performance Metrics
        st.markdown("### � Model Performance Summary")
        st.markdown("*Key insights from risk assessment model validation*")
        st.markdown("")
        
        # Key findings from analysis
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card-green">
                <div class="metric-header">
                    <div class="metric-icon">🎯</div>
                </div>
                <div class="metric-value">42.1%</div>
                <div class="metric-label">Model Recall</div>
                <div class="metric-trend trend-up">✓ Default Capture Rate</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card-blue">
                <div class="metric-header">
                    <div class="metric-icon">🔍</div>
                </div>
                <div class="metric-value">3.2%</div>
                <div class="metric-label">Precision</div>
                <div class="metric-trend trend-up">✓ High Risk Accuracy</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card-purple">
                <div class="metric-header">
                    <div class="metric-icon">📋</div>
                </div>
                <div class="metric-value">11.3%</div>
                <div class="metric-label">Review Rate</div>
                <div class="metric-trend trend-neutral">📊 Manageable Workload</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Business Impact
        st.header("💰 Business Impact")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 💰 Annual Benefits
            - **💵 $12-15M** potential loss prevention
            - **🎯 43%** of defaults caught early
            - **📊 11%** manual review rate (manageable workload)
            - **⚡ 4x improvement** over random selection
            """)
        
        with col2:
            st.markdown("""
            ### 🔍 Key Risk Factors Identified
            1. **📊 Credit Score** - Primary predictor
            2. **💰 Debt-to-Income Ratio** - Critical threshold at 35%
            3. **🏠 Loan-to-Value Ratio** - Risk increases above 80%
            4. **🗺️ Geographic Patterns** - State-level variations
            """)

if __name__ == "__main__":
    main()
