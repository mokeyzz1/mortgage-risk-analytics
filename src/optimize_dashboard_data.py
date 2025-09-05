#!/usr/bin/env python3
"""
Dashboard Data Optimization Script
Creates pre-computed datasets for fast dashboard loading
"""

import pandas as pd
import sqlite3
import pickle
from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).parent.parent

def create_optimized_datasets():
    """Create pre-computed datasets for dashboard"""
    print(" Creating optimized dashboard datasets...")
    
    database_path = PROJECT_ROOT / 'data' / 'processed' / 'mortgage_analytics.db'
    output_dir = PROJECT_ROOT / 'data' / 'dashboard_cache'
    output_dir.mkdir(exist_ok=True)
    
    conn = sqlite3.connect(database_path)
    
    # 1. Create main dashboard dataset (smaller sample)
    print("Creating main dashboard dataset...")
    main_query = """
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
    AND (CAST(substr(o.loan_sequence_number, -2) AS INTEGER) % 20) < 3  -- Smaller sample
    GROUP BY o.loan_sequence_number
    LIMIT 50000  -- Cap at 50K records for fast loading
    """
    
    df_main = pd.read_sql_query(main_query, conn)
    
    # Add risk calculations
    df_main['risk_tier'] = 'Low Risk'
    df_main.loc[(df_main['credit_score'] < 680) | (df_main['dti'] > 0.43) | (df_main['ltv'] > 85), 'risk_tier'] = 'Medium Risk'
    df_main.loc[(df_main['credit_score'] < 620) | (df_main['dti'] > 0.50) | (df_main['ltv'] > 95), 'risk_tier'] = 'High Risk'
    
    # Save as parquet (much faster than CSV)
    df_main.to_parquet(output_dir / 'main_dashboard_data.parquet')
    print(f"✅ Main dataset saved: {len(df_main):,} records")
    
    # 2. Create pre-computed summary statistics
    print(" Creating summary statistics...")
    summary_stats = {
        'total_loans': len(df_main),
        'avg_credit_score': float(df_main['credit_score'].mean()),
        'delinquency_rate': float(df_main['serious_delinquency_flag'].mean() * 100),
        'avg_ltv': float(df_main['ltv'].mean()),
        'high_risk_count': len(df_main[df_main['risk_tier'] == 'High Risk']),
        'medium_risk_count': len(df_main[df_main['risk_tier'] == 'Medium Risk']),
        'low_risk_count': len(df_main[df_main['risk_tier'] == 'Low Risk'])
    }
    
    with open(output_dir / 'summary_stats.json', 'w') as f:
        json.dump(summary_stats, f, indent=2)
    
    # 3. Create geographic aggregations
    print("🗺️ Creating geographic aggregations...")
    geo_data = df_main.groupby('state').agg({
        'serious_delinquency_flag': ['count', 'mean'],
        'credit_score': 'mean',
        'ltv': 'mean'
    }).round(2)
    
    geo_data.columns = ['loan_count', 'delinquency_rate', 'avg_credit_score', 'avg_ltv']
    geo_data['delinquency_rate'] *= 100
    geo_data.to_parquet(output_dir / 'geographic_data.parquet')
    
    # 4. Create pre-computed charts data
    print("📊 Creating chart datasets...")
    
    # Credit score distribution
    credit_dist = df_main['credit_score'].value_counts().sort_index()
    credit_dist.to_pickle(output_dir / 'credit_distribution.pkl')
    
    # Risk tier summary
    risk_summary = df_main['risk_tier'].value_counts()
    risk_summary.to_pickle(output_dir / 'risk_summary.pkl')
    
    conn.close()
    
    print("🎉 Optimization complete!")
    print(f"📁 Files saved to: {output_dir}")
    print(f"📊 Main dataset: {len(df_main):,} records")
    print("⚡ Dashboard should now load much faster!")

if __name__ == "__main__":
    create_optimized_datasets()
