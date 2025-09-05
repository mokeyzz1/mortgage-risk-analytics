import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DASHBOARDS_DIR = PROJECT_ROOT / "dashboards"

# Data source directories - organized under proper data engineering structure
HISTORICAL_DATA_DIRS = [
    RAW_DATA_DIR / "historical_data_2023",
    RAW_DATA_DIR / "historical_data_2024"
]

# Column definitions for Freddie Mac Single Family Loan-Level Dataset
# Based on SF LLD File Layout Release 44 - Official Documentation
ORIGINATION_COLUMNS = [
    'borrower_credit_score', 'first_payment_date', 'first_time_buyer_flag', 'maturity_date',
    'metropolitan_statistical_area', 'mortgage_insurance_percentage', 'number_of_units', 
    'occupancy_status', 'original_combined_loan_to_value', 'debt_to_income_ratio',
    'original_upb', 'original_loan_to_value', 'original_interest_rate', 'channel', 
    'prepayment_penalty_mortgage_flag', 'product_type', 'property_state', 'property_type', 
    'postal_code', 'loan_sequence_number', 'loan_purpose', 'original_loan_term', 
    'number_of_borrowers', 'seller_name', 'servicer_name', 'super_conforming_flag', 
    'pre_harp_loan_sequence_number', 'program_indicator', 'harp_indicator', 
    'property_valuation_method', 'interest_only_indicator', 'mortgage_insurance_cancellation_indicator'
]

PERFORMANCE_COLUMNS = [
    'loan_sequence_number', 'monthly_reporting_period', 'current_actual_upb',
    'current_loan_delinquency_status', 'loan_age', 'remaining_months_to_legal_maturity',
    'adjusted_months_to_maturity', 'maturity_date', 'metropolitan_statistical_area',
    'current_interest_rate', 'current_deferred_upb', 'due_date_of_last_paid_installment',
    'mortgage_insurance_recoveries', 'net_sales_proceeds', 'non_mortgage_insurance_recoveries',
    'expenses', 'legal_costs', 'maintenance_and_preservation_costs', 'taxes_and_insurance',
    'miscellaneous_expenses', 'actual_loss_calculation', 'modification_cost', 
    'step_modification_flag', 'deferred_payment_plan', 'estimated_loan_to_value',
    'zero_balance_code', 'zero_balance_effective_date', 'upb_at_the_time_of_removal',
    'repurchase_date', 'foreclosure_date', 'disposition_date', 'foreclosure_costs'
]

# Database configuration - Processed data storage
DATABASE_PATH = PROCESSED_DATA_DIR / "mortgage_analytics.db"

# Model configuration - Key risk factors for mortgage delinquency prediction
MODEL_FEATURES = [
    'borrower_credit_score', 'original_loan_to_value', 'debt_to_income_ratio', 
    'original_interest_rate', 'original_upb', 'loan_age', 'current_interest_rate',
    'current_actual_upb', 'remaining_months_to_legal_maturity'
]

TARGET_VARIABLE = 'current_loan_delinquency_status'

# Dashboard configuration
DASHBOARD_PORT = 8501
DASHBOARD_HOST = 'localhost'