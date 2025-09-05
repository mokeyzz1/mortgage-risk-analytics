#!/usr/bin/env python3
"""
Phase 1: Raw Data Assessment and Profiling
Freddie Mac Single-Family Loan Data Analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src to path
sys.path.append(str(Path(__file__).parent / 'src'))
from config import HISTORICAL_DATA_DIRS, ORIGINATION_COLUMNS, PERFORMANCE_COLUMNS

def assess_file_structure():
    """Assess the structure and size of our data files"""
    print("=== DATA FILE ASSESSMENT ===\n")
    
    total_files = 0
    total_size_mb = 0
    
    for year_dir in HISTORICAL_DATA_DIRS:
        if year_dir.exists():
            print(f"📁 {year_dir.name}/")
            quarters = sorted([d for d in year_dir.iterdir() if d.is_dir()])
            
            for quarter_dir in quarters:
                orig_file = quarter_dir / f"{quarter_dir.name}.txt"
                perf_file = quarter_dir / f"{quarter_dir.name.replace('historical_data', 'historical_data_time')}.txt"
                
                print(f"  📊 {quarter_dir.name}/")
                
                if orig_file.exists():
                    size_mb = orig_file.stat().st_size / (1024*1024)
                    total_size_mb += size_mb
                    total_files += 1
                    print(f"    ✅ Origination: {size_mb:.1f} MB")
                else:
                    print(f"    ❌ Origination: MISSING")
                
                if perf_file.exists():
                    size_mb = perf_file.stat().st_size / (1024*1024)
                    total_size_mb += size_mb
                    total_files += 1
                    print(f"    ✅ Performance: {size_mb:.1f} MB")
                else:
                    print(f"    ❌ Performance: MISSING")
                print()
    
    print(f"📈 SUMMARY:")
    print(f"Total files: {total_files}")
    print(f"Total size: {total_size_mb:.1f} MB ({total_size_mb/1024:.2f} GB)")
    return total_files, total_size_mb

def sample_data_structure():
    """Examine the structure of our data files"""
    print("\n=== DATA STRUCTURE ANALYSIS ===\n")
    
    # Get first available origination file
    sample_orig = None
    sample_perf = None
    
    for year_dir in HISTORICAL_DATA_DIRS:
        if year_dir.exists():
            for quarter_dir in year_dir.iterdir():
                if quarter_dir.is_dir():
                    orig_file = quarter_dir / f"{quarter_dir.name}.txt"
                    perf_file = quarter_dir / f"{quarter_dir.name.replace('historical_data', 'historical_data_time')}.txt"
                    
                    if orig_file.exists() and sample_orig is None:
                        sample_orig = orig_file
                    if perf_file.exists() and sample_perf is None:
                        sample_perf = perf_file
                    
                    if sample_orig and sample_perf:
                        break
            if sample_orig and sample_perf:
                break
    
    # Analyze origination data
    if sample_orig:
        print(f"📋 ORIGINATION DATA SAMPLE: {sample_orig.name}")
        try:
            # Read first few rows
            df_orig = pd.read_csv(sample_orig, sep='|', names=ORIGINATION_COLUMNS, nrows=1000)
            
            print(f"Columns: {len(df_orig.columns)}")
            print(f"Sample rows: {len(df_orig)}")
            print("\nFirst few rows:")
            print(df_orig.head(3))
            print(f"\nData types:")
            print(df_orig.dtypes.value_counts())
            
            # Check for missing data
            missing_pct = (df_orig.isnull().sum() / len(df_orig) * 100).sort_values(ascending=False)
            print(f"\nColumns with missing data:")
            print(missing_pct[missing_pct > 0].head(10))
            
        except Exception as e:
            print(f"Error reading origination file: {e}")
    
    # Analyze performance data
    if sample_perf:
        print(f"\n📊 PERFORMANCE DATA SAMPLE: {sample_perf.name}")
        try:
            # Read first few rows
            df_perf = pd.read_csv(sample_perf, sep='|', names=PERFORMANCE_COLUMNS, nrows=1000)
            
            print(f"Columns: {len(df_perf.columns)}")
            print(f"Sample rows: {len(df_perf)}")
            print("\nFirst few rows:")
            print(df_perf.head(3))
            
            # Check delinquency status distribution
            if 'current_loan_delinquency_status' in df_perf.columns:
                delinq_dist = df_perf['current_loan_delinquency_status'].value_counts()
                print(f"\nDelinquency Status Distribution:")
                print(delinq_dist.head(10))
                
        except Exception as e:
            print(f"Error reading performance file: {e}")

def estimate_record_counts():
    """Estimate total records across all files"""
    print("\n=== RECORD COUNT ESTIMATION ===\n")
    
    total_orig_records = 0
    total_perf_records = 0
    
    for year_dir in HISTORICAL_DATA_DIRS:
        if year_dir.exists():
            print(f"📅 {year_dir.name}:")
            for quarter_dir in sorted(year_dir.iterdir()):
                if quarter_dir.is_dir():
                    orig_file = quarter_dir / f"{quarter_dir.name}.txt"
                    perf_file = quarter_dir / f"{quarter_dir.name.replace('historical_data', 'historical_data_time')}.txt"
                    
                    quarter_orig = 0
                    quarter_perf = 0
                    
                    if orig_file.exists():
                        # Count lines (approximate)
                        result = Path(orig_file).read_text().count('\n')
                        quarter_orig = result
                        total_orig_records += quarter_orig
                    
                    if perf_file.exists():
                        result = Path(perf_file).read_text().count('\n')
                        quarter_perf = result
                        total_perf_records += quarter_perf
                    
                    print(f"  {quarter_dir.name}: {quarter_orig:,} orig, {quarter_perf:,} perf")
    
    print(f"\n📊 TOTAL ESTIMATED RECORDS:")
    print(f"Origination: {total_orig_records:,}")
    print(f"Performance: {total_perf_records:,}")
    print(f"Combined: {total_orig_records + total_perf_records:,}")
    
    return total_orig_records, total_perf_records

def main():
    print("🏠 FREDDIE MAC DATA ASSESSMENT")
    print("=" * 50)
    
    # Step 1: File structure
    assess_file_structure()
    
    # Step 2: Data structure
    sample_data_structure()
    
    # Step 3: Record counts (this might take a moment)
    print("\n⏳ Counting records (this may take a moment)...")
    estimate_record_counts()
    
    print("\n✅ Data assessment complete!")
    print("\nNext steps:")
    print("1. Design ETL pipeline based on findings")
    print("2. Set up PostgreSQL database schema")
    print("3. Implement data quality controls")

if __name__ == "__main__":
    main()