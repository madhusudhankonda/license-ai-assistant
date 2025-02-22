import streamlit as st
from pathlib import Path

def render_sidebar():
    """Render the application sidebar"""
    
    with st.sidebar:
        # Display logo
        logo_path = Path("assets/licences-assistant-logo.png")
        if logo_path.exists():
            st.image(logo_path, width=200)
        
        st.title("📜 AI License Assistant")
        st.markdown("""
        AI License Assistant is a tool that helps you understand and compare software licenses.
        ### Features
        - License Analysis
        - License Comparison
        - Compliance Guidance
        - Custom License Analysis
        - General Questions
                    
        ### How to Use
        1. Select a license or upload your own
        2. View the analysis
        3. Compare licenses
        4. Ask general questions
                    
        Disclaimer: This tool is not a legal advisor. It provides general information and cannot replace professional legal advice.
        
        Contact: [Madhusudhan Konda](https://www.linkedin.com/in/madhusudhankonda/)
        """) 