"""
Database Manager for Mortgage Risk Analytics
Extracted functionality from working notebook without modifications
"""

import sqlite3
import pandas as pd
from pathlib import Path
import sys

# Add src to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT / 'src'))

from config import DATABASE_PATH, ORIGINATION_COLUMNS, PERFORMANCE_COLUMNS

class MortgageDB:
    """Database manager for mortgage analytics data"""
    
    def __init__(self, db_path=None):
        self.db_path = db_path or DATABASE_PATH
        
    def get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_path)
    
    def execute_query(self, query, params=None):
        """Execute a query and return results as DataFrame"""
        with self.get_connection() as conn:
            if params:
                return pd.read_sql(query, conn, params=params)
            else:
                return pd.read_sql(query, conn)
    
    def get_table_info(self):
        """Get basic table information"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            try:
                # Get origination count
                cursor.execute("SELECT COUNT(*) FROM origination_data")
                origination_count = cursor.fetchone()[0]
                
                # Get performance count
                cursor.execute("SELECT COUNT(*) FROM performance_data")
                performance_count = cursor.fetchone()[0]
                
                # Get unique loans
                cursor.execute("SELECT COUNT(DISTINCT loan_sequence_number) FROM origination_data")
                unique_loans = cursor.fetchone()[0]
                
                # Get date range
                cursor.execute("SELECT MIN(monthly_reporting_period), MAX(monthly_reporting_period) FROM performance_data")
                date_range = cursor.fetchone()
                
                return {
                    'origination_records': origination_count,
                    'performance_records': performance_count,
                    'unique_loans': unique_loans,
                    'date_range': date_range,
                    'avg_records_per_loan': round(performance_count / unique_loans, 1) if unique_loans > 0 else 0
                }
                
            except sqlite3.OperationalError as e:
                return {'error': f"Database error: {e}"}
    
    def check_data_quality(self):
        """Check data quality for key variables"""
        quality_query = """
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
        """
        
        return self.execute_query(quality_query)
    
    def get_credit_distribution(self):
        """Get credit score distribution"""
        query = """
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
        """
        
        return self.execute_query(query)
    
    def get_geographic_distribution(self, limit=10):
        """Get geographic distribution of loans"""
        query = """
        SELECT 
            property_state,
            COUNT(*) as loan_count,
            ROUND(AVG(borrower_credit_score), 0) as avg_credit_score,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM origination_data), 1) as portfolio_percentage
        FROM origination_data
        WHERE property_state IS NOT NULL
        GROUP BY property_state
        ORDER BY loan_count DESC
        LIMIT ?;
        """
        
        return self.execute_query(query, params=[limit])
    
    def get_model_features(self):
        """Extract features for machine learning model"""
        query = """
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
        """
        
        return self.execute_query(query)

# Convenience functions that match the notebook style
def get_database_connection():
    """Get database connection - matches notebook function"""
    return sqlite3.connect(DATABASE_PATH)

def execute_sql_query(query, params=None):
    """Execute SQL query - matches notebook usage"""
    db = MortgageDB()
    return db.execute_query(query, params)

def get_database_summary():
    """Get database summary - matches notebook function"""
    db = MortgageDB()
    return db.get_table_info()
