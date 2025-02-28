import streamlit as st
from utils.license_analyzer import LicenseAnalyzer

def render_license_comparison(license_analyzer: LicenseAnalyzer):
    """Render the license comparison interface"""
    
    # Create row with column headers
    header_cols = st.columns([2, 2, 1])
    with header_cols[0]:
        st.write("Select first license")
    with header_cols[1]:
        st.write("Select second license")
    
    # Create container for the dropdown row
    container = st.container()
    
    # Create three columns in a single row
    with container:
        col1, col2, col3 = st.columns([2, 2, 1])
        
        # First license dropdown
        with col1:
            license1 = st.selectbox(
                label="",
                options=license_analyzer.common_licenses,
                key="license1",
                label_visibility="collapsed"
            )
        
        # Second license dropdown
        with col2:
            license2 = st.selectbox(
                label="",
                options=license_analyzer.common_licenses,
                key="license2",
                label_visibility="collapsed"
            )
        
        # Compare button
        with col3:
            compare_button = st.button("Compare", key="compare_licenses_button", use_container_width=True)
    
    # Only perform comparison when button is clicked
    if compare_button and license1 and license2:
        # Store comparison in session state
        st.session_state.current_comparison = license_analyzer.compare_licenses(license1, license2)
        
        # Display the comparison
        st.markdown(st.session_state.current_comparison)
    # Show previous comparison if it exists
    elif 'current_comparison' in st.session_state and license1 and license2:
        st.markdown(st.session_state.current_comparison) 