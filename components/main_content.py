import streamlit as st
from utils.license_analyzer import LicenseAnalyzer
from utils.pdf_generator import generate_pdf

def render_main_content(license_analyzer: LicenseAnalyzer):
    """Render the main content area for license analysis"""
    
    # First, set the label separately
    st.write("Select a license to analyze")
    
    # Create a container with custom CSS for horizontal layout
    container = st.container()
    
    # Use columns within the container
    with container:
        col1, col2 = st.columns([4, 1])
        
        with col1:
            selected_license = st.selectbox(
                label=" ",  # Empty label since we already have one above
                options=license_analyzer.common_licenses,
                label_visibility="collapsed"  # Hide the label
            )
        
        with col2:
            analyze_button = st.button("Analyze", key="analyze_license_button", use_container_width=True)
    
    # Only perform analysis when button is clicked
    if analyze_button and selected_license:
        # Store analysis in session state so it persists between interactions
        st.session_state.current_analysis = license_analyzer.analyze_license(selected_license)
        
        # Display the analysis
        st.markdown(st.session_state.current_analysis)
        
        # Export button
        if st.button("Export Analysis"):
            pdf_file = generate_pdf(st.session_state.current_analysis)
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name=f"{selected_license}_analysis.pdf",
                mime="application/pdf"
            )
    # Show previous analysis if it exists
    elif 'current_analysis' in st.session_state and selected_license:
        st.markdown(st.session_state.current_analysis)
        
        # Export button for previous analysis
        if st.button("Export Analysis"):
            pdf_file = generate_pdf(st.session_state.current_analysis)
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name=f"{selected_license}_analysis.pdf",
                mime="application/pdf"
            ) 