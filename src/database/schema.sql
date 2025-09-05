-- Mortgage Risk Analytics Database Schema
-- Extracted from working notebook analysis
-- Source: Freddie Mac Single Family Loan-Level Dataset

-- Drop existing tables if they exist
DROP TABLE IF EXISTS performance_data;
DROP TABLE IF EXISTS origination_data;

-- Create origination data table
CREATE TABLE origination_data (
    borrower_credit_score INTEGER,
    first_payment_date TEXT,
    first_time_buyer_flag TEXT,
    maturity_date TEXT,
    metropolitan_statistical_area TEXT,
    mortgage_insurance_percentage REAL,
    number_of_units INTEGER,
    occupancy_status TEXT,
    original_combined_loan_to_value REAL,
    debt_to_income_ratio REAL,
    original_upb REAL,
    original_loan_to_value REAL,
    original_interest_rate REAL,
    channel TEXT,
    prepayment_penalty_mortgage_flag TEXT,
    product_type TEXT,
    property_state TEXT,
    property_type TEXT,
    postal_code TEXT,
    loan_sequence_number TEXT,
    loan_purpose TEXT,
    original_loan_term INTEGER,
    number_of_borrowers INTEGER,
    seller_name TEXT,
    servicer_name TEXT,
    super_conforming_flag TEXT,
    pre_harp_loan_sequence_number TEXT,
    program_indicator TEXT,
    harp_indicator TEXT,
    property_valuation_method TEXT,
    interest_only_indicator TEXT,
    mortgage_insurance_cancellation_indicator TEXT
);

-- Create performance data table
CREATE TABLE performance_data (
    loan_sequence_number TEXT,
    monthly_reporting_period TEXT,
    current_actual_upb REAL,
    current_loan_delinquency_status TEXT,
    loan_age INTEGER,
    remaining_months_to_legal_maturity INTEGER,
    adjusted_months_to_maturity INTEGER,
    maturity_date TEXT,
    metropolitan_statistical_area TEXT,
    current_interest_rate REAL,
    current_deferred_upb REAL,
    due_date_of_last_paid_installment TEXT,
    mortgage_insurance_recoveries REAL,
    net_sales_proceeds REAL,
    non_mortgage_insurance_recoveries REAL,
    expenses REAL,
    legal_costs REAL,
    maintenance_and_preservation_costs REAL,
    taxes_and_insurance REAL,
    miscellaneous_expenses REAL,
    actual_loss_calculation REAL,
    modification_cost REAL,
    step_modification_flag TEXT,
    deferred_payment_plan TEXT,
    estimated_loan_to_value REAL,
    zero_balance_code TEXT,
    zero_balance_effective_date TEXT,
    upb_at_the_time_of_removal REAL,
    repurchase_date TEXT,
    foreclosure_date TEXT,
    disposition_date TEXT,
    foreclosure_costs REAL
);

-- Create indexes for better performance
CREATE INDEX idx_origination_loan_id ON origination_data(loan_sequence_number);
CREATE INDEX idx_performance_loan_id ON performance_data(loan_sequence_number);
CREATE INDEX idx_performance_date ON performance_data(monthly_reporting_period);
CREATE INDEX idx_origination_credit_score ON origination_data(borrower_credit_score);
CREATE INDEX idx_performance_delinquency ON performance_data(current_loan_delinquency_status);
