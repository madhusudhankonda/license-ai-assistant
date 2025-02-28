import streamlit as st
from pathlib import Path
from utils.license_analyzer import LicenseAnalyzer
from utils.pdf_generator import generate_pdf
from components.sidebar import render_sidebar
from components.main_content import render_main_content
from components.license_comparison import render_license_comparison
from components.custom_styling import apply_custom_styling

def init_session_state():
    """Initialize session state variables"""
    if 'current_license' not in st.session_state:
        st.session_state.current_license = None
    if 'comparison_mode' not in st.session_state:
        st.session_state.comparison_mode = False
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = []

def main():
    st.set_page_config(
        page_title="Software Licensing AI Assistant",
        page_icon="📜",
        layout="wide"
    )
    
    # Apply custom styling
    apply_custom_styling()
    
    init_session_state()
    
    # Initialize LicenseAnalyzer
    license_analyzer = LicenseAnalyzer()
    
    # Render sidebar
    render_sidebar()
    
    # Add logo and title with custom HTML to center it properly
    st.markdown("""
    <div class="logo-container">
        <img src="https://cdn-icons-png.flaticon.com/512/1548/1548611.png" class="logo-image" alt="License Logo">
        <h1 class="app-title">Software Licensing AI Assistant</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for different features
    tab1, tab2, tab3, tab4 = st.tabs([
        "License Analysis", 
        "License Comparison", 
        "Upload License",
        "General Questions"
    ])
    
    with tab1:
        render_main_content(license_analyzer)
    
    with tab2:
        render_license_comparison(license_analyzer)
    
    with tab3:
        # st.subheader("Upload License Document")
        uploaded_file = st.file_uploader("Upload a license file", type=["txt", "md"])
        
        if uploaded_file:
            content = uploaded_file.read().decode()
            analyze_upload_button = st.button("Analyze Upload", key="analyze_upload_button")
            
            if analyze_upload_button:
                st.session_state.uploaded_analysis = license_analyzer.analyze_uploaded_license(content)
                st.markdown(st.session_state.uploaded_analysis)
            elif 'uploaded_analysis' in st.session_state:
                st.markdown(st.session_state.uploaded_analysis)
    
    with tab4:
        # st.subheader("Ask about Software Licensing")
        question = st.text_input("Enter your licensing question:")
        
        if question:
            ask_button = st.button("Ask Question", key="ask_question_button")
            
            if ask_button:
                st.session_state.question_response = license_analyzer.get_general_guidance(question)
                st.markdown(st.session_state.question_response)
            elif 'question_response' in st.session_state:
                st.markdown(st.session_state.question_response)

if __name__ == "__main__":
    main() 