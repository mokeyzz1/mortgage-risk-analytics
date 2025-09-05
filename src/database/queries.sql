-- Mortgage Risk Analytics - Reusable SQL Queries
-- Extracted from working notebook analysis

-- ===========================================
-- DATA QUALITY ASSESSMENT QUERIES
-- ===========================================

-- Check data completeness for key risk variables
-- Data Quality Assessment Query
SELECT 
    'Credit Score' as variable,
    COUNT(*) as records_with_data,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as completeness_pct
FROM origination_data 
WHERE borrower_credit_score IS NOT NULL

UNION ALL

SELECT 
    'LTV Ratio' as variable,
    COUNT(*) as records_with_data,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as completeness_pct
FROM origination_data 
WHERE original_loan_to_value IS NOT NULL

UNION ALL

SELECT 
    'DTI Ratio' as variable,
    COUNT(*) as records_with_data,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as completeness_pct
FROM origination_data 
WHERE debt_to_income_ratio IS NOT NULL

UNION ALL

SELECT 
    'Interest Rate' as variable,
    COUNT(*) as records_with_data,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as completeness_pct
FROM origination_data 
WHERE original_interest_rate IS NOT NULL;

-- ===========================================
-- DATABASE SUMMARY QUERIES
-- ===========================================

-- Get record counts
SELECT COUNT(*) as origination_count FROM origination_data;
SELECT COUNT(*) as performance_count FROM performance_data;
SELECT COUNT(DISTINCT loan_sequence_number) as unique_loans FROM origination_data;

-- Get date range
SELECT MIN(monthly_reporting_period) as start_date, MAX(monthly_reporting_period) as end_date 
FROM performance_data;

-- ===========================================
-- RISK ANALYSIS QUERIES
-- ===========================================

-- Credit Score Distribution Analysis
SELECT 
    CASE 
        WHEN borrower_credit_score >= 800 THEN '800+'
        WHEN borrower_credit_score >= 740 THEN '740-799'
        WHEN borrower_credit_score >= 680 THEN '680-739'
        WHEN borrower_credit_score >= 620 THEN '620-679'
        ELSE 'Below 620'
    END as credit_tier,
    COUNT(*) as loan_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as percentage
FROM origination_data
WHERE borrower_credit_score IS NOT NULL
GROUP BY credit_tier
ORDER BY MIN(borrower_credit_score) DESC;

-- LTV Ratio Risk Analysis
SELECT 
    CASE 
        WHEN original_loan_to_value <= 60 THEN '≤60%'
        WHEN original_loan_to_value <= 70 THEN '61-70%'
        WHEN original_loan_to_value <= 80 THEN '71-80%'
        WHEN original_loan_to_value <= 90 THEN '81-90%'
        WHEN original_loan_to_value <= 95 THEN '91-95%'
        ELSE '>95%'
    END as ltv_tier,
    COUNT(*) as loan_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as percentage
FROM origination_data
WHERE original_loan_to_value IS NOT NULL
GROUP BY ltv_tier
ORDER BY MIN(original_loan_to_value);

-- Geographic Risk Distribution (Top 10 States)
SELECT 
    property_state,
    COUNT(*) as loan_count,
    ROUND(AVG(borrower_credit_score), 0) as avg_credit_score,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as portfolio_percentage
FROM origination_data
WHERE property_state IS NOT NULL
GROUP BY property_state
ORDER BY loan_count DESC
LIMIT 10;

-- First-Time Buyer Analysis
SELECT 
    first_time_buyer_flag,
    COUNT(*) as loan_count,
    ROUND(AVG(borrower_credit_score), 0) as avg_credit_score,
    ROUND(AVG(original_loan_to_value), 1) as avg_ltv,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as percentage
FROM origination_data
WHERE first_time_buyer_flag IS NOT NULL
GROUP BY first_time_buyer_flag;

-- ===========================================
-- DELINQUENCY ANALYSIS QUERIES
-- ===========================================

-- Current Delinquency Status Distribution
SELECT 
    CASE 
        WHEN current_loan_delinquency_status IN ('0', '1') THEN 'Current'
        WHEN current_loan_delinquency_status = '2' THEN '30-59 Days'
        WHEN current_loan_delinquency_status = '3' THEN '60-89 Days'
        WHEN current_loan_delinquency_status = '4' THEN '90-119 Days'
        WHEN current_loan_delinquency_status >= '5' THEN '120+ Days'
        ELSE 'Other'
    END as delinquency_status,
    COUNT(DISTINCT loan_sequence_number) as unique_loans,
    ROUND(COUNT(DISTINCT loan_sequence_number) * 100.0 / 
          (SELECT COUNT(DISTINCT loan_sequence_number) FROM performance_data), 1) as percentage
FROM performance_data
WHERE current_loan_delinquency_status IS NOT NULL
GROUP BY delinquency_status
ORDER BY MIN(CAST(current_loan_delinquency_status AS INTEGER));

-- ===========================================
-- MODEL FEATURE QUERIES
-- ===========================================

-- Extract features for machine learning model
SELECT 
    o.loan_sequence_number,
    o.borrower_credit_score,
    o.original_loan_to_value,
    o.debt_to_income_ratio,
    o.original_interest_rate,
    o.original_upb,
    o.first_time_buyer_flag,
    o.occupancy_status,
    o.property_type,
    o.property_state,
    p.loan_age,
    p.current_interest_rate,
    p.current_actual_upb,
    p.remaining_months_to_legal_maturity,
    p.current_loan_delinquency_status,
    CASE 
        WHEN p.current_loan_delinquency_status IN ('2', '3', '4', '5', '6', '7', '8', '9') 
        THEN 1 ELSE 0 
    END as serious_delinquency_flag
FROM origination_data o
JOIN performance_data p ON o.loan_sequence_number = p.loan_sequence_number
WHERE o.borrower_credit_score IS NOT NULL
    AND o.original_loan_to_value IS NOT NULL
    AND o.debt_to_income_ratio IS NOT NULL
    AND p.current_loan_delinquency_status IS NOT NULL;
