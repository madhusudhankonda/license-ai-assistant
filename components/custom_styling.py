import streamlit as st

def apply_custom_styling():
    """Apply additional custom styling beyond the theme config"""
    
    # Custom CSS
    st.markdown("""
    <style>
        /* Remove top spacing */
        .stApp header {
            background-color: transparent;
            height: 0;
        }
        
        /* Remove top padding from main container */
        .stApp .main .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 1rem;
        }
        
        /* Center align the logo and title */
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }
        
        .logo-image {
            height: 80px;
            margin-right: 15px;
            object-fit: contain;
        }
        
        .app-title {
            text-align: center;
            color: #FFC857;
            font-size: 2.5rem;
            font-weight: 600;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
            margin: 0;
        }
        
        /* Body/Background styling */
        .stApp {
            background: linear-gradient(135deg, #1D3557 0%, #2E4A6B 50%, #253B59 100%);
        }
        
        /* Remove unwanted containers */
        div[data-testid="stVerticalBlock"] > div:not([data-baseweb]) {
            background-color: transparent !important;
            border: none !important;
            padding: 0 !important;
            margin-bottom: 0 !important;
        }
        
        /* Only style specific containers like metrics or dataframes */
        [data-testid="stMetric"], [data-testid="stDataFrame"] {
            background-color: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            padding: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        /* Overall spacing and layout */
        .main .block-container {
            padding: 2rem 3rem;
        }
        
        /* Headers styling */
        h1, h2, h3 {
            color: #FFC857 !important;
            font-weight: 600;
        }
        
        h1 {
            font-size: 2.5rem !important;
            margin-bottom: 1.5rem !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(to bottom, #334866, #2A4A73);
            color: #F1FAEE;
            border: 1px solid rgba(255, 200, 87, 0.5);
            border-radius: 4px;
            padding: 0.5rem 1rem;
            transition: all 0.3s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .stButton>button:hover {
            background: linear-gradient(to bottom, #FFC857, #E0AC3E);
            color: #1D3557;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background: linear-gradient(160deg, #1D3557 0%, #253B59 100%);
            border-right: 1px solid rgba(255,200,87,0.2);
            padding: 1rem;
        }
        
        section[data-testid="stSidebar"] .block-container {
            margin-top: 1rem;
        }
        
        /* Tab container styling - add padding instead of borders */
        .stTabs {
            background-color: rgba(255, 255, 255, 0.02);
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 4px;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid rgba(255,200,87,0.15);
        }
        
        .stTabs [data-baseweb="tab"] {
            background: linear-gradient(to bottom, #3A5270, #334866);
            border-radius: 4px 4px 0 0;
            padding: 0.5rem 1rem;
            color: #F1FAEE;
            font-weight: 400;
            border: none;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(to bottom, #FFC857, #E0AC3E) !important;
            color: #1D3557 !important;
            font-weight: 600;
        }
        
        /* Form elements */
        .stSelectbox label, .stTextInput label {
            color: #FFC857 !important;
            font-weight: 500;
        }
        
        /* Make selectbox stand out */
        .stSelectbox > div > div {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 4px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Clean up markdowns */
        .stMarkdown {
            line-height: 1.6;
        }
        
        /* Table styling */
        thead th {
            background-color: rgba(255, 200, 87, 0.15) !important;
            color: #FFC857 !important;
        }
        
        tbody tr:nth-child(even) {
            background-color: rgba(255, 255, 255, 0.03) !important;
        }
        
        table {
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
        }
        
        /* Improve list readability */
        ol, ul {
            margin-left: 2rem;
        }
        
        li {
            margin-bottom: 0.5rem;
        }
        
        /* Selection highlight */
        ::selection {
            background-color: rgba(255,200,87,0.4);
            color: #F1FAEE;
        }
        
        /* Make sure the header is responsive */
        @media (max-width: 768px) {
            .logo-container {
                flex-direction: column;
                text-align: center;
            }
            
            .logo-image {
                margin-right: 0;
                margin-bottom: 15px;
            }
            
            .app-title {
                font-size: 2rem !important;
            }
        }
    </style>
    """, unsafe_allow_html=True) 