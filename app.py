import streamlit as st
import base64
import os
from pathlib import Path
from utils.license_analyzer import LicenseAnalyzer
from utils.pdf_generator import generate_pdf
from components.sidebar import render_sidebar
from components.main_content import render_main_content
from components.license_comparison import render_license_comparison
from components.custom_styling import apply_custom_styling

def get_base64_encoded_image(image_path):
    """Get base64 encoded string of an image for embedding in HTML"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        st.error(f"Error encoding image: {e}")
        return None

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
    
    # Get base64 encoded logo - try multiple potential paths
    img_html = None
    potential_paths = [
        "assets/licences-assistant-logo2.png",
        "/app/assets/licences-assistant-logo2.png",
        "../assets/licences-assistant-logo2.png",
        "./assets/licences-assistant-logo2.png"
    ]
    
    for path in potential_paths:
        if os.path.exists(path):
            st.write(f"Found logo at {path}")  # Debug info - remove later
            encoded_logo = get_base64_encoded_image(path)
            if encoded_logo:
                img_html = f'<img src="data:image/png;base64,{encoded_logo}" class="logo-image" alt="License Logo">'
                break
    
    # If no logo was found, use an emoji as fallback
    if not img_html:
        img_html = '<span style="font-size: 60px; margin-right: 15px;">📜</span>'
    
    # Add logo and title with custom HTML
    st.markdown(f"""
    <div class="logo-container">
        {img_html}
        <h1 class="app-title">AI Software Licensing Assistant</h1>
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