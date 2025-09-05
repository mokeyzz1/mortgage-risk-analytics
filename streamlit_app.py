#!/usr/bin/env python3
"""
Streamlit app entry point for Mortgage Risk Analytics Dashboard
"""

import sys
import os

# Add the dashboards directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'dashboards'))

# Import and run the main dashboard
from mortgage_risk_dashboard import *

if __name__ == "__main__":
    # The dashboard will run automatically when imported
    pass
