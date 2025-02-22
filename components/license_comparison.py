import streamlit as st
from utils.license_analyzer import LicenseAnalyzer

def render_license_comparison(license_analyzer: LicenseAnalyzer):
    """Render the license comparison interface"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        license1 = st.selectbox(
            "Select first license",
            license_analyzer.common_licenses,
            key="license1"
        )
    
    with col2:
        license2 = st.selectbox(
            "Select second license",
            license_analyzer.common_licenses,
            key="license2"
        )
    
    if license1 and license2:
        comparison = license_analyzer.compare_licenses(license1, license2)
        st.markdown(comparison) 