import streamlit as st
from utils.license_analyzer import LicenseAnalyzer
from utils.pdf_generator import generate_pdf

def render_main_content(license_analyzer: LicenseAnalyzer):
    """Render the main content area for license analysis"""
    
    # License selection
    selected_license = st.selectbox(
        "Select a license to analyze",
        license_analyzer.common_licenses
    )
    
    if selected_license:
        analysis = license_analyzer.analyze_license(selected_license)
        st.markdown(analysis)
        
        # Export button
        if st.button("Export Analysis"):
            pdf_file = generate_pdf(analysis)
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name=f"{selected_license}_analysis.pdf",
                mime="application/pdf"
            ) 