import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import hashlib

# Page configuration
st.set_page_config(
    page_title="ByStudents - Peer College Consulting",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Revolutionary Modern CSS Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Modern Color Palette */
    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --secondary: #ec4899;
        --accent: #f59e0b;
        --success: #10b981;
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --bg-card: #1e293b;
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --border: #334155;
        --gradient-1: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        --gradient-2: linear-gradient(135deg, #ec4899 0%, #f59e0b 100%);
        --gradient-3: linear-gradient(135deg, #10b981 0%, #3b82f6 100%);
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
        --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
    }
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Keep header visible for sidebar toggle */
    header {visibility: visible !important;}
    header[data-testid="stHeader"] {
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(20px);
    }
    
    /* Main Container */
    .main {
        background: var(--bg-primary);
        padding: 2rem !important;
    }
    
    .block-container {
        padding: 2rem 4rem !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
    }
    
    /* Glassmorphism Card */
    .glass-card {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin-bottom: 1.5rem;
    }
    
    .glass-card:hover {
        transform: translateY(-2px);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 12px 40px rgba(99, 102, 241, 0.2);
    }
    
    /* Modern Navbar */
    .modern-nav {
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid var(--border);
        padding: 1.25rem 3rem;
        position: sticky;
        top: 0;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .logo {
        font-size: 1.75rem;
        font-weight: 800;
        background: var(--gradient-1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
    }
    
    .nav-links {
        display: flex;
        gap: 2.5rem;
        align-items: center;
    }
    
    .nav-link {
        color: var(--text-secondary);
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.2s;
        position: relative;
    }
    
    .nav-link:hover {
        color: var(--text-primary);
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 2px;
        background: var(--gradient-1);
        transition: width 0.3s;
    }
    
    .nav-link:hover::after {
        width: 100%;
    }
    
    .btn-primary {
        background: var(--gradient-1);
        color: white;
        padding: 0.75rem 1.75rem;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        font-size: 0.95rem;
        cursor: pointer;
        transition: all 0.3s;
        box-shadow: 0 4px 12px rgb(99 102 241 / 0.4);
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgb(99 102 241 / 0.6);
    }
    
    /* Hero Section - Dramatic */
    .hero {
        position: relative;
        padding: 8rem 3rem 6rem;
        text-align: center;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
        animation: pulse 8s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1) rotate(0deg); opacity: 0.5; }
        50% { transform: scale(1.1) rotate(180deg); opacity: 0.8; }
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 900px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-size: 4.5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #fff 0%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.03em;
    }
    
    .hero-subtitle {
        font-size: 1.35rem;
        color: var(--text-secondary);
        margin-bottom: 3rem;
        line-height: 1.6;
        font-weight: 400;
    }
    
    .hero-stats {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
        max-width: 800px;
        margin: 4rem auto 0;
    }
    
    .stat-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.5rem;
        transition: all 0.3s;
    }
    
    .stat-card:hover {
        background: rgba(30, 41, 59, 0.8);
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateY(-4px);
    }
    
    .stat-value {
        font-size: 2.5rem;
        font-weight: 800;
        background: var(--gradient-1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    /* Feature Cards - Bento Grid */
    .bento-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.5rem;
        padding: 4rem 3rem;
    }
    
    .feature-bento {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 2rem;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .feature-bento::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: var(--gradient-1);
        opacity: 0;
        transition: opacity 0.4s;
    }
    
    .feature-bento:hover::before {
        opacity: 0.05;
    }
    
    .feature-bento:hover {
        border-color: rgba(99, 102, 241, 0.4);
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgb(99 102 241 / 0.2);
    }
    
    .feature-icon {
        width: 60px;
        height: 60px;
        border-radius: 16px;
        background: var(--gradient-1);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.75rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 16px rgb(99 102 241 / 0.3);
    }
    
    .feature-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.75rem;
        line-height: 1.3;
    }
    
    .feature-desc {
        font-size: 0.95rem;
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    /* Step Cards - Timeline */
    .timeline {
        position: relative;
        padding: 4rem 0;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .step-card {
        display: grid;
        grid-template-columns: 80px 1fr;
        gap: 2rem;
        margin-bottom: 3rem;
        position: relative;
    }
    
    .step-number-wrap {
        position: relative;
    }
    
    .step-number {
        width: 80px;
        height: 80px;
        border-radius: 20px;
        background: var(--gradient-1);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: 800;
        color: white;
        box-shadow: 0 8px 20px rgb(99 102 241 / 0.4);
        position: relative;
        z-index: 2;
    }
    
    .step-line {
        position: absolute;
        top: 80px;
        left: 50%;
        transform: translateX(-50%);
        width: 2px;
        height: calc(100% + 3rem);
        background: linear-gradient(180deg, var(--primary) 0%, transparent 100%);
    }
    
    .step-content {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2.5rem;
        transition: all 0.3s;
    }
    
    .step-content:hover {
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateX(8px);
    }
    
    .step-title {
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    .step-desc {
        font-size: 1.05rem;
        color: var(--text-secondary);
        line-height: 1.7;
    }
    
    /* Pricing Cards - Modern */
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        padding: 4rem 3rem;
    }
    
    .price-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 2.5rem;
        position: relative;
        overflow: hidden;
        transition: all 0.4s;
    }
    
    .price-card.featured {
        border: 2px solid rgba(99, 102, 241, 0.5);
        background: rgba(30, 41, 59, 0.8);
    }
    
    .price-card.featured::before {
        content: 'BEST VALUE';
        position: absolute;
        top: 1.5rem;
        right: -2rem;
        background: var(--gradient-1);
        color: white;
        padding: 0.4rem 3rem;
        transform: rotate(45deg);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.05em;
    }
    
    .price-card:hover {
        transform: translateY(-12px);
        border-color: rgba(99, 102, 241, 0.6);
        box-shadow: 0 20px 40px rgb(99 102 241 / 0.3);
    }
    
    .price-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .price-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    .price-amount {
        font-size: 3.5rem;
        font-weight: 800;
        background: var(--gradient-1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }
    
    .price-period {
        font-size: 0.9rem;
        color: var(--text-secondary);
        margin-top: 0.5rem;
    }
    
    .price-features {
        list-style: none;
        padding: 0;
        margin: 2rem 0;
    }
    
    .price-features li {
        padding: 0.75rem 0;
        color: var(--text-secondary);
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 0.95rem;
    }
    
    .price-features li::before {
        content: '✓';
        color: var(--success);
        font-weight: 700;
        font-size: 1.1rem;
    }
    
    /* Dashboard Styles */
    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        padding: 0;
        margin-bottom: 3rem;
    }
    
    .metric-card-modern {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.3s;
        min-height: 120px;
    }
    
    .metric-card-modern:hover {
        border-color: rgba(99, 102, 241, 0.5);
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(99, 102, 241, 0.2);
    }
    
    .metric-label-modern {
        font-size: 0.875rem;
        color: var(--text-secondary);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 1rem;
    }
    
    .metric-value-modern {
        font-size: 3rem;
        font-weight: 800;
        background: var(--gradient-1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        display: block;
    }
    
    @media (max-width: 1200px) {
        .dashboard-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    @media (max-width: 768px) {
        .dashboard-grid {
            grid-template-columns: 1fr;
        }
    }
    
    /* Section Headers */
    .section-header {
        text-align: center;
        padding: 4rem 3rem 2rem;
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff 0%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    .section-subtitle {
        font-size: 1.15rem;
        color: var(--text-secondary);
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Buttons */
    .stButton>button {
        background: var(--gradient-1) !important;
        color: white !important;
        border: none !important;
        padding: 0.875rem 2rem !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s !important;
        box-shadow: 0 4px 12px rgb(99 102 241 / 0.4) !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgb(99 102 241 / 0.6) !important;
    }
    
    /* Better text visibility */
    p, span, label {
        color: var(--text-primary) !important;
    }
    
    .stMarkdown {
        color: var(--text-primary);
    }
    
    /* Progress bar container */
    .stProgress {
        margin: 0.5rem 0 1rem 0;
    }
    
    /* Form Inputs */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>select,
    .stTextArea>div>div>textarea {
        background: rgba(30, 41, 59, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: var(--text-primary) !important;
        padding: 0.75rem !important;
        font-size: 0.95rem !important;
    }
    
    .stTextInput>div>div>input:focus,
    .stSelectbox>div>div>select:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.98) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid var(--border);
        min-width: 280px !important;
    }
    
    [data-testid="stSidebar"] > div {
        background: transparent !important;
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        display: block !important;
    }
    
    [data-testid="stSidebar"] .stRadio > div {
        gap: 0.5rem;
        display: flex !important;
        flex-direction: column !important;
    }
    
    [data-testid="stSidebar"] [role="radiogroup"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 0.5rem !important;
    }
    
    [data-testid="stSidebar"] [role="radiogroup"] label {
        padding: 0.75rem 1rem !important;
        border-radius: 8px !important;
        transition: all 0.2s !important;
        color: var(--text-secondary) !important;
        cursor: pointer !important;
        display: block !important;
    }
    
    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: rgba(99, 102, 241, 0.1) !important;
        color: var(--text-primary) !important;
    }
    
    [data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] {
        background: rgba(99, 102, 241, 0.2) !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    
    /* Sidebar toggle button */
    [data-testid="collapsedControl"] {
        color: var(--text-primary) !important;
        background: rgba(99, 102, 241, 0.2) !important;
        border-radius: 8px !important;
        padding: 0.5rem !important;
    }
    
    [data-testid="collapsedControl"]:hover {
        background: rgba(99, 102, 241, 0.4) !important;
    }
    
    /* Make sure sidebar buttons work */
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(239, 68, 68, 0.2) !important;
        color: #fca5a5 !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(239, 68, 68, 0.3) !important;
        border-color: rgba(239, 68, 68, 0.5) !important;
    }
    
    /* Progress bars */
    .stProgress > div > div > div {
        background: var(--gradient-1);
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background: rgba(30, 41, 59, 0.6);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        color: var(--text-primary) !important;
        font-weight: 600;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: transparent;
        border-bottom: 1px solid var(--border);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: var(--text-secondary);
        padding: 1rem 1.5rem;
        font-weight: 600;
        border: none;
        border-bottom: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: transparent;
        color: var(--text-primary);
        border-bottom-color: var(--primary);
    }
    
    /* Success/Warning/Info boxes */
    .success-modern {
        background: rgba(16, 185, 129, 0.1);
        border-left: 4px solid var(--success);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        color: var(--text-primary);
        margin: 1rem 0;
    }
    
    .warning-modern {
        background: rgba(245, 158, 11, 0.1);
        border-left: 4px solid var(--accent);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        color: var(--text-primary);
        margin: 1rem 0;
    }
    
    .info-modern {
        background: rgba(99, 102, 241, 0.1);
        border-left: 4px solid var(--primary);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        color: var(--text-primary);
        margin: 1rem 0;
    }
    
    /* Mentor Cards */
    .mentor-modern {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.3s;
        display: grid;
        grid-template-columns: 80px 1fr;
        gap: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    .mentor-modern:hover {
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateY(-4px);
    }
    
    .mentor-avatar-modern {
        width: 80px;
        height: 80px;
        border-radius: 16px;
        background: var(--gradient-1);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: 700;
        color: white;
        box-shadow: 0 8px 16px rgb(99 102 241 / 0.3);
    }
    
    /* Footer */
    .footer-modern {
        background: rgba(15, 23, 42, 0.95);
        border-top: 1px solid var(--border);
        padding: 4rem 3rem;
        text-align: center;
        margin-top: 6rem;
    }
    
    .footer-modern h3 {
        font-size: 1.5rem;
        font-weight: 700;
        background: var(--gradient-1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }
    
    .footer-modern p {
        color: var(--text-secondary);
        font-size: 0.95rem;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 3rem;
        }
        
        .section-title {
            font-size: 2rem;
        }
        
        .modern-nav {
            padding: 1rem;
        }
        
        .bento-grid,
        .pricing-grid {
            grid-template-columns: 1fr;
            padding: 2rem 1rem;
        }
        
        .hero-stats {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .block-container {
            padding: 1rem !important;
        }
    }
    
    /* Streamlit column fixes */
    [data-testid="column"] {
        padding: 0 0.5rem;
    }
    
    /* Remove extra spacing */
    .element-container {
        margin-bottom: 0.5rem;
    }

</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_type' not in st.session_state:
    st.session_state.user_type = None
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'landing'
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'name': 'Alex Johnson',
        'email': '',
        'school': '',
        'graduation_year': 2025,
        'sat_score': 1380,
        'gpa_weighted': 4.1,
        'gpa_unweighted': 3.7,
        'extracurriculars': [],
        'honors': [],
        'essays': [],
        'saved_colleges': [],
        'scholarships': [],
        'meetings': [],
        'messages': [],
        'mentor_matched': False,
        'mentor_info': None
    }

# Sample data functions
@st.cache_data
def load_colleges():
    return pd.DataFrame({
        'name': [
            'Harvard University', 'Stanford University', 'MIT', 'Yale University',
            'Princeton University', 'Columbia University', 'UPenn', 'Duke University',
            'Northwestern University', 'Dartmouth College', 'Brown University',
            'Vanderbilt University', 'Rice University', 'Cornell University',
            'UC Berkeley', 'UCLA', 'USC', 'Carnegie Mellon', 'Emory University',
            'Georgetown University', 'University of Michigan', 'NYU', 'Boston College',
            'UT Austin', 'UNC Chapel Hill'
        ],
        'state': ['MA', 'CA', 'MA', 'CT', 'NJ', 'NY', 'PA', 'NC', 'IL', 'NH',
                 'RI', 'TN', 'TX', 'NY', 'CA', 'CA', 'CA', 'PA', 'GA', 'DC',
                 'MI', 'NY', 'MA', 'TX', 'NC'],
        'acceptance_rate': [3.4, 3.7, 3.9, 4.5, 3.9, 3.7, 5.9, 6.2, 7.0, 6.2,
                           5.1, 6.1, 8.7, 7.3, 11.4, 8.6, 9.9, 11.3, 11.0, 12.0,
                           17.7, 8.0, 16.7, 31.4, 16.8],
        'avg_sat': [1520, 1505, 1540, 1515, 1510, 1520, 1500, 1520, 1490, 1500,
                   1490, 1520, 1520, 1480, 1430, 1405, 1450, 1510, 1450, 1460,
                   1435, 1470, 1420, 1355, 1390],
        'avg_gpa': [4.18, 4.16, 4.17, 4.19, 4.15, 4.15, 4.13, 4.13, 4.09, 4.11,
                   4.10, 4.12, 4.12, 4.07, 3.89, 3.90, 3.79, 3.84, 3.78, 3.90,
                   3.88, 3.69, 3.86, 3.71, 4.00],
        'tuition': [57261, 58416, 57986, 62250, 57410, 66139, 63452, 63054, 63468,
                   62430, 65656, 58130, 54960, 63200, 44115, 43473, 63468, 61344,
                   57120, 62052, 55334, 57532, 64176, 40996, 37552],
        'type': ['Private'] * 14 + ['Public', 'Public', 'Private', 'Private',
                                    'Private', 'Private', 'Public', 'Private',
                                    'Private', 'Public', 'Public']
    })

@st.cache_data
def load_scholarships():
    return pd.DataFrame({
        'name': [
            'Gates Scholarship', 'Coca-Cola Scholars', 'Jack Kent Cooke',
            'Dell Scholars', 'QuestBridge', 'Posse Foundation',
            'Davidson Fellows', 'National Merit', 'Hispanic Scholarship Fund',
            'Ron Brown Scholar', 'Burger King Scholars', 'Equitable Excellence',
            'Horatio Alger', 'Elks National', 'AXA Achievement',
            'Foot Locker Athletes', 'United Negro College Fund',
            'Asian & Pacific Islander', 'Regeneron Science', 'Siemens Competition'
        ],
        'amount': ['Full Tuition', '$20,000', '$55,000', '$20,000', 'Full Tuition',
                  'Full Tuition', '$50,000', '$2,500', '$5,000', '$40,000',
                  '$50,000', '$25,000', '$25,000', '$50,000', '$25,000',
                  '$20,000', '$10,000', '$20,000', '$250,000', '$100,000'],
        'deadline': ['Sep 15', 'Oct 31', 'Nov 14', 'Dec 1', 'Sep 27', 'Dec 1',
                    'Apr 30', 'Oct 15', 'Feb 15', 'Jan 9', 'Dec 15', 'Dec 15',
                    'Oct 25', 'Dec 15', 'Dec 15', 'Jan 12', 'Mar 1', 'Jan 15',
                    'Nov 15', 'Oct 1'],
        'min_gpa': [3.3, 3.0, 3.5, 2.4, 3.5, 3.0, 3.9, 3.5, 3.0, 3.5, 2.5, 3.0,
                   2.0, 3.5, 3.0, 3.0, 3.0, 3.0, 3.8, 3.5],
        'category': ['Need-Based', 'Merit', 'Merit', 'Need-Based', 'Need-Based',
                    'Leadership', 'STEM', 'Merit', 'Minority', 'Minority',
                    'Merit', 'Need-Based', 'Need-Based', 'Merit', 'Merit',
                    'Athletic', 'Minority', 'Minority', 'STEM', 'STEM']
    })

@st.cache_data
def load_mentors():
    return [
        {
            'name': 'Sarah Chen',
            'school': 'Stanford University',
            'major': 'Computer Science',
            'year': 'Junior',
            'specialty': ['Essays', 'STEM Applications', 'Interview Prep'],
            'bio': 'First-gen college student passionate about helping others navigate the admissions process.',
            'rating': 4.9,
            'sessions': 47
        },
        {
            'name': 'Marcus Johnson',
            'school': 'Yale University',
            'major': 'Political Science',
            'year': 'Senior',
            'specialty': ['Liberal Arts Essays', 'School Selection', 'Financial Aid'],
            'bio': 'QuestBridge scholar committed to making college accessible for all students.',
            'rating': 5.0,
            'sessions': 62
        },
        {
            'name': 'Priya Patel',
            'school': 'MIT',
            'major': 'Mechanical Engineering',
            'year': 'Sophomore',
            'specialty': ['STEM Essays', 'Research Applications', 'Resume Building'],
            'bio': 'International student who understands unique challenges in admissions.',
            'rating': 4.8,
            'sessions': 35
        },
        {
            'name': 'James Liu',
            'school': 'Princeton University',
            'major': 'Economics',
            'year': 'Junior',
            'specialty': ['Business Essays', 'Entrepreneurship', 'Leadership'],
            'bio': 'Founded startup in high school, now helping students showcase their achievements.',
            'rating': 4.9,
            'sessions': 51
        }
    ]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(email, password, user_type):
    hashed = hash_password(password)
    st.session_state.authenticated = True
    st.session_state.user_type = user_type
    st.session_state.user_data['email'] = email
    return True

def calculate_admission_chance(college, user_sat, user_gpa):
    sat_diff = (user_sat - college['avg_sat']) / college['avg_sat']
    gpa_diff = user_gpa - college['avg_gpa']
    
    sat_score = 1.0 if sat_diff >= 0.05 else 0.8 if sat_diff >= 0 else 0.6 if sat_diff >= -0.05 else 0.4
    gpa_score = 1.0 if gpa_diff >= 0.2 else 0.8 if gpa_diff >= 0 else 0.6 if gpa_diff >= -0.2 else 0.4
    
    base_chance = (sat_score * 0.5 + gpa_score * 0.5) * 100 * min(1.0, college['acceptance_rate'] / 10.0)
    return max(1, min(95, base_chance))

# Landing Page
def show_landing_page():
    # Modern Navigation
    st.markdown("""
    <div class='modern-nav'>
        <div class='logo'>ByStudents</div>
        <div class='nav-links'>
            <a href='#how-it-works' class='nav-link'>How It Works</a>
            <a href='#services' class='nav-link'>Services</a>
            <a href='#about' class='nav-link'>About</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero Section with Animation
    st.markdown("""
    <div class='hero'>
        <div class='hero-content fade-in-up'>
            <h1 class='hero-title'>Your Dream College Journey Starts Here</h1>
            <p class='hero-subtitle'>Connect with peer mentors from top universities and unlock AI-powered tools to ace your college applications</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Start Your Journey", use_container_width=True, key="hero_cta"):
            st.session_state.current_page = 'signup'
            st.rerun()
    
    # Hero Stats
    st.markdown("""
    <div class='hero-stats'>
        <div class='stat-card'>
            <div class='stat-value'>500+</div>
            <div class='stat-label'>Colleges</div>
        </div>
        <div class='stat-card'>
            <div class='stat-value'>50+</div>
            <div class='stat-label'>Expert Mentors</div>
        </div>
        <div class='stat-card'>
            <div class='stat-value'>$2M+</div>
            <div class='stat-label'>Scholarships</div>
        </div>
        <div class='stat-card'>
            <div class='stat-value'>95%</div>
            <div class='stat-label'>Success Rate</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # How It Works - Timeline with Streamlit
    st.markdown("""
    <div class='section-header'>
        <h2 class='section-title'>How It Works</h2>
        <p class='section-subtitle'>Three simple steps to transform your college application journey</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 1
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown("""
        <div style='text-align: center;'>
            <div class='step-number'>1</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='step-content'>
            <h3 class='step-title'>🎯 Create Your Profile</h3>
            <p class='step-desc'>Tell us about your academic background, interests, and college goals. Our smart algorithm analyzes your profile to provide personalized recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Step 2
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown("""
        <div style='text-align: center;'>
            <div class='step-number'>2</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='step-content'>
            <h3 class='step-title'>🤝 Get Matched with Mentors</h3>
            <p class='step-desc'>Connect with current students at top universities who've been exactly where you are. Our mentors understand your challenges and can guide you through every step.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Step 3
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown("""
        <div style='text-align: center;'>
            <div class='step-number'>3</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='step-content'>
            <h3 class='step-title'>🚀 Access Premium Tools</h3>
            <p class='step-desc'>Use our AI-powered essay editor, college explorer, scholarship finder, and application tracker. Work with your mentor to perfect your applications and get accepted!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Features - Use Streamlit columns
    st.markdown("""
    <div class='section-header'>
        <h2 class='section-title'>Everything You Need to Succeed</h2>
        <p class='section-subtitle'>Comprehensive tools and expert guidance in one platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create features using Streamlit columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='feature-bento'>
            <div class='feature-icon'>👥</div>
            <h3 class='feature-title'>Peer Mentorship</h3>
            <p class='feature-desc'>Connect with current students at your dream schools who've been exactly where you are.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-bento'>
            <div class='feature-icon'>📅</div>
            <h3 class='feature-title'>Application Tracker</h3>
            <p class='feature-desc'>Never miss a deadline with our smart calendar and application management system.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-bento'>
            <div class='feature-icon'>🏛️</div>
            <h3 class='feature-title'>College Explorer</h3>
            <p class='feature-desc'>Search 500+ colleges with detailed information, admission chances, and personalized recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-bento'>
            <div class='feature-icon'>💬</div>
            <h3 class='feature-title'>Direct Messaging</h3>
            <p class='feature-desc'>Chat directly with your mentor, ask questions, and get support whenever you need it.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-bento'>
            <div class='feature-icon'>✍️</div>
            <h3 class='feature-title'>Essay Support</h3>
            <p class='feature-desc'>Get feedback from peers who got into top schools plus AI-powered writing assistance.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-bento'>
            <div class='feature-icon'>💰</div>
            <h3 class='feature-title'>Scholarship Finder</h3>
            <p class='feature-desc'>Discover thousands of scholarships matched to your profile and interests.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Pricing Section
    st.markdown("""
    <div class='section-header' id='services'>
        <h2 class='section-title'>Affordable Pricing</h2>
        <p class='section-subtitle'>Professional guidance at student-friendly prices</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='price-card'>
            <div class='price-header'>
                <h3 class='price-name'>Essay Editing</h3>
                <div class='price-amount'>$35</div>
                <p class='price-period'>2 rounds of edits</p>
            </div>
            <ul class='price-features'>
                <li>Professional feedback</li>
                <li>Grammar & style review</li>
                <li>Structure improvements</li>
                <li>48-hour turnaround</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='price-card'>
            <div class='price-header'>
                <h3 class='price-name'>Essay Complete</h3>
                <div class='price-amount'>$80</div>
                <p class='price-period'>Brainstorm + 2 edits</p>
            </div>
            <ul class='price-features'>
                <li>30-min Zoom session</li>
                <li>Topic brainstorming</li>
                <li>2 rounds of professional edits</li>
                <li>Personalized guidance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='price-card'>
            <div class='price-header'>
                <h3 class='price-name'>Common App</h3>
                <div class='price-amount'>$250</div>
                <p class='price-period'>Full support</p>
            </div>
            <ul class='price-features'>
                <li>Brainstorming session</li>
                <li>Topic development</li>
                <li>Multiple revisions</li>
                <li>Until perfected</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='price-card featured'>
            <div class='price-header'>
                <h3 class='price-name'>All-Inclusive</h3>
                <div class='price-amount'>$1,200</div>
                <p class='price-period'>Everything you need</p>
            </div>
            <ul class='price-features'>
                <li>15 essays edited</li>
                <li>Unlimited brainstorming</li>
                <li>Resume review</li>
                <li>School list strategy</li>
                <li>Interview preparation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # About Section
    st.markdown("""
    <div class='section-header' id='about'>
        <h2 class='section-title'>About ByStudents</h2>
        <p class='section-subtitle'>We're students who've been through the process, now helping you succeed</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='glass-card'>
            <div class='feature-icon' style='margin-bottom: 1.5rem;'>🎯</div>
            <h3 style='font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin-bottom: 1rem;'>Our Mission</h3>
            <p style='color: var(--text-secondary); line-height: 1.7; font-size: 1rem;'>
            We believe every student deserves access to quality college counseling, regardless of their background or resources. 
            ByStudents was created by students who navigated admissions successfully and want to pay it forward.
            </p>
            <p style='color: var(--text-secondary); line-height: 1.7; font-size: 1rem; margin-top: 1rem;'>
            Our peer mentors understand the stress, challenges, and excitement of applying to college because they just went through it themselves.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='glass-card'>
            <div class='feature-icon' style='margin-bottom: 1.5rem;'>⭐</div>
            <h3 style='font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin-bottom: 1rem;'>Why Peer Mentoring Works</h3>
            <ul style='color: var(--text-secondary); line-height: 1.8; font-size: 1rem; list-style: none; padding: 0;'>
                <li style='margin-bottom: 0.75rem;'><strong style='color: var(--text-primary);'>Recent Experience:</strong> Our mentors just completed applications themselves</li>
                <li style='margin-bottom: 0.75rem;'><strong style='color: var(--text-primary);'>Authentic Advice:</strong> Real students, not paid consultants</li>
                <li style='margin-bottom: 0.75rem;'><strong style='color: var(--text-primary);'>Affordable:</strong> High-quality guidance at student-friendly prices</li>
                <li><strong style='color: var(--text-primary);'>Relatable:</strong> Mentors who understand your unique challenges</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Final CTA
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; padding: 6rem 3rem; background: var(--gradient-1); border-radius: 32px; margin: 3rem; box-shadow: 0 20px 40px rgb(99 102 241 / 0.4);'>
        <h2 style='font-size: 3rem; font-weight: 800; color: white; margin-bottom: 1.5rem; line-height: 1.2;'>Ready to Start Your Journey?</h2>
        <p style='font-size: 1.25rem; color: white; opacity: 0.95; max-width: 700px; margin: 0 auto 3rem; line-height: 1.6;'>Join thousands of students who've achieved their college dreams with ByStudents</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Create Free Account", use_container_width=True, type="primary", key="cta_button"):
            st.session_state.current_page = 'signup'
            st.rerun()
    
    # Footer
    st.markdown("""
    <div class='footer-modern'>
        <h3>ByStudents</h3>
        <p style='margin: 1.5rem 0;'>Peer-to-peer college admissions made simple</p>
        <p style='opacity: 0.7;'>© 2025 ByStudents. Made with ❤️ by students, for students.</p>
    </div>
    """, unsafe_allow_html=True)

# Auth pages
def show_signup_page():
    st.markdown("""
    <div class='modern-nav'>
        <div class='logo'>ByStudents</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; color: var(--text-primary); margin-bottom: 2rem; font-size: 2.5rem;'>Create Your Account</h1>", unsafe_allow_html=True)
        
        user_type = st.radio(
            "I am a...",
            ["🎓 Student (looking for mentorship)", "🌟 Mentor (want to help students)"],
            horizontal=False
        )
        
        is_mentor = "Mentor" in user_type
        
        with st.form("signup_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            
            if is_mentor:
                school = st.text_input("Current University")
                major = st.text_input("Major")
                year = st.selectbox("Year", ["Freshman", "Sophomore", "Junior", "Senior"])
            else:
                high_school = st.text_input("High School")
                grad_year = st.selectbox("Expected Graduation Year", [2025, 2026, 2027, 2028])
            
            agree = st.checkbox("I agree to the Terms of Service and Privacy Policy")
            
            submitted = st.form_submit_button("Create Account", use_container_width=True)
            
            if submitted:
                if not all([name, email, password, confirm_password]):
                    st.error("Please fill in all fields")
                elif password != confirm_password:
                    st.error("Passwords don't match")
                elif not agree:
                    st.error("Please agree to the Terms of Service")
                else:
                    st.session_state.authenticated = True
                    st.session_state.user_type = 'mentor' if is_mentor else 'mentee'
                    st.session_state.user_data['name'] = name
                    st.session_state.user_data['email'] = email
                    st.session_state.current_page = 'dashboard'
                    st.success("Account created successfully!")
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("← Back to Home", use_container_width=True):
                st.session_state.current_page = 'landing'
                st.rerun()
        with col_b:
            if st.button("Already have an account? Sign In", use_container_width=True):
                st.session_state.current_page = 'signin'
                st.rerun()

def show_signin_page():
    st.markdown("""
    <div class='modern-nav'>
        <div class='logo'>ByStudents</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; color: var(--text-primary); margin-bottom: 2rem; font-size: 2.5rem;'>Welcome Back!</h1>", unsafe_allow_html=True)
        
        with st.form("signin_form"):
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            
            user_type = st.radio("Sign in as:", ["Student", "Mentor"], horizontal=True)
            
            submitted = st.form_submit_button("Sign In", use_container_width=True)
            
            if submitted:
                if authenticate_user(email, password, user_type.lower()):
                    st.session_state.current_page = 'dashboard'
                    st.success("Signed in successfully!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("← Back to Home", use_container_width=True):
                st.session_state.current_page = 'landing'
                st.rerun()
        with col_b:
            if st.button("Don't have an account? Sign Up", use_container_width=True):
                st.session_state.current_page = 'signup'
                st.rerun()

def show_dashboard():
    with st.sidebar:
        st.markdown(f"""
        <div style='text-align: center; padding: 2rem 1rem; border-bottom: 1px solid var(--border); margin-bottom: 1.5rem;'>
            <h2 class='logo' style='font-size: 1.5rem; margin-bottom: 0.5rem;'>ByStudents</h2>
            <p style='color: var(--text-secondary); font-size: 0.9rem;'>Welcome back, {st.session_state.user_data['name'].split()[0]}!</p>
        </div>
        """, unsafe_allow_html=True)
        
        page_options = [
            "🏠 Home",
            "👥 Find Mentor",
            "🏛️ Colleges",
            "💰 Scholarships",
            "✍️ Essays",
            "📅 Calendar",
            "💬 Messages",
            "⚙️ Settings"
        ]
        
        st.markdown("<p style='color: var(--text-secondary); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; padding: 0 1rem; margin-bottom: 0.5rem; font-weight: 600;'>Navigation</p>", unsafe_allow_html=True)
        
        selected_page = st.radio(
            "Navigation", 
            page_options, 
            label_visibility="collapsed",
            key="sidebar_nav"
        )
        
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
        
        if st.button("🚪 Sign Out", use_container_width=True, key="signout_btn"):
            st.session_state.authenticated = False
            st.session_state.current_page = 'landing'
            st.rerun()
    
    if selected_page == "🏠 Home":
        show_dashboard_home()
    elif selected_page == "👥 Find Mentor":
        show_mentor_matching()
    elif selected_page == "🏛️ Colleges":
        show_college_explorer()
    elif selected_page == "💰 Scholarships":
        show_scholarships()
    elif selected_page == "✍️ Essays":
        show_essays()
    elif selected_page == "📅 Calendar":
        show_calendar()
    elif selected_page == "💬 Messages":
        show_messages()
    elif selected_page == "⚙️ Settings":
        show_settings()

def show_dashboard_home():
    # Header with better spacing
    st.markdown(f"""
    <div style='margin-bottom: 3rem;'>
        <h1 style='font-size: 2.5rem; font-weight: 800; color: var(--text-primary); margin-bottom: 0.5rem;'>
            Hi {st.session_state.user_data['name'].split()[0]} 👋
        </h1>
        <p style='color: var(--text-secondary); font-size: 1.1rem;'>
            Let's get you into your dream college
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar reminder if it might be hidden
    st.info("💡 **Tip:** Use the sidebar on the left to navigate between different sections (Home, Colleges, Essays, etc.)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Metrics using native Streamlit columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card-modern'>
            <div class='metric-label-modern'>SAT Score</div>
            <div class='metric-value-modern'>1380</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card-modern'>
            <div class='metric-label-modern'>GPA (Weighted)</div>
            <div class='metric-value-modern'>{st.session_state.user_data['gpa_weighted']:.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card-modern'>
            <div class='metric-label-modern'>Saved Colleges</div>
            <div class='metric-value-modern'>{len(st.session_state.user_data['saved_colleges'])}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='metric-card-modern'>
            <div class='metric-label-modern'>Essays Started</div>
            <div class='metric-value-modern'>{len(st.session_state.user_data['essays'])}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Main content area
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown("""
        <div class='glass-card' style='margin-bottom: 2rem;'>
            <h3 style='color: var(--text-primary); font-size: 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;'>
                📋 Your Application Progress
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bars with better styling
        progress_items = [
            ("Profile Complete", 85),
            ("College List", 60),
            ("Essays Written", 40),
            ("Applications Submitted", 0)
        ]
        
        for item, progress in progress_items:
            st.markdown(f"<p style='color: var(--text-primary); font-weight: 600; margin-bottom: 0.5rem; margin-top: 1.5rem;'>{item}</p>", unsafe_allow_html=True)
            st.progress(progress / 100)
            st.caption(f"{progress}% complete")
    
    with col_right:
        st.markdown("""
        <div class='glass-card' style='margin-bottom: 2rem;'>
            <h3 style='color: var(--text-primary); font-size: 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;'>
                🎯 Quick Actions
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.user_data.get('mentor_matched'):
            if st.button("👥 Find a Mentor", use_container_width=True, key="find_mentor"):
                st.info("Navigate to 'Find Mentor' from the sidebar!")
        else:
            st.success("✅ Mentor matched!")
            if st.button("💬 Message Mentor", use_container_width=True, key="msg_mentor"):
                st.info("Navigate to 'Messages' from the sidebar!")
        
        st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
        
        if st.button("🏛️ Explore Colleges", use_container_width=True, key="explore_colleges"):
            st.info("Navigate to 'Colleges' from the sidebar!")
        
        st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
        
        if st.button("✍️ Start an Essay", use_container_width=True, key="start_essay"):
            st.info("Navigate to 'Essays' from the sidebar!")

def show_mentor_matching():
    st.markdown("<h1 style='font-size: 2.5rem; font-weight: 800; color: var(--text-primary); margin: 2rem 0;'>Find Your Perfect Mentor 👥</h1>", unsafe_allow_html=True)
    
    mentors = load_mentors()
    
    for mentor in mentors:
        st.markdown(f"""
        <div class='mentor-modern'>
            <div class='mentor-avatar-modern'>{mentor['name'][0]}</div>
            <div>
                <h3 style='color: var(--text-primary); font-size: 1.35rem; margin-bottom: 0.5rem;'>{mentor['name']}</h3>
                <p style='color: var(--text-secondary); margin-bottom: 0.75rem;'><strong>{mentor['school']}</strong> • {mentor['major']} • {mentor['year']}</p>
                <p style='color: var(--text-secondary); margin-bottom: 0.75rem;'>{mentor['bio']}</p>
                <p style='color: var(--text-secondary);'><strong>Specialties:</strong> {', '.join(mentor['specialty'])}</p>
                <p style='color: var(--text-primary); margin-top: 0.5rem;'>⭐ {mentor['rating']}/5.0 ({mentor['sessions']} sessions)</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"💬 Connect with {mentor['name']}", key=f"connect_{mentor['name']}"):
            st.session_state.user_data['mentor_matched'] = True
            st.session_state.user_data['mentor_info'] = mentor
            st.success(f"Connected with {mentor['name']}!")
            st.balloons()

def show_college_explorer():
    st.markdown("<h1 style='font-size: 2.5rem; font-weight: 800; color: var(--text-primary); margin: 2rem 0;'>College Explorer 🏛️</h1>", unsafe_allow_html=True)
    
    colleges_df = load_colleges()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        state_filter = st.multiselect("State", sorted(colleges_df['state'].unique()))
    
    with col2:
        type_filter = st.multiselect("Type", colleges_df['type'].unique())
    
    with col3:
        max_tuition = st.slider("Max Tuition", 0, 70000, 70000, 5000)
    
    filtered = colleges_df.copy()
    if state_filter:
        filtered = filtered[filtered['state'].isin(state_filter)]
    if type_filter:
        filtered = filtered[filtered['type'].isin(type_filter)]
    filtered = filtered[filtered['tuition'] <= max_tuition]
    
    user_sat = st.session_state.user_data['sat_score']
    user_gpa = st.session_state.user_data['gpa_weighted']
    
    filtered['chance'] = filtered.apply(
        lambda row: calculate_admission_chance(row, user_sat, user_gpa),
        axis=1
    )
    
    st.markdown(f"<br><h3 style='color: var(--text-primary);'>Showing {len(filtered)} colleges</h3>", unsafe_allow_html=True)
    
    for _, college in filtered.iterrows():
        with st.expander(f"**{college['name']}** - {college['state']} | {college['chance']:.0f}% chance"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Acceptance Rate", f"{college['acceptance_rate']:.1f}%")
                st.metric("Avg SAT", college['avg_sat'])
            
            with col2:
                st.metric("Avg GPA", f"{college['avg_gpa']:.2f}")
                st.metric("Tuition", f"${college['tuition']:,}")
            
            with col3:
                st.metric("Your Chance", f"{college['chance']:.0f}%")
                st.metric("Type", college['type'])
            
            is_saved = college['name'] in st.session_state.user_data['saved_colleges']
            
            if is_saved:
                if st.button(f"❤️ Saved", key=f"save_{college['name']}"):
                    st.session_state.user_data['saved_colleges'].remove(college['name'])
                    st.rerun()
            else:
                if st.button(f"🤍 Save", key=f"save_{college['name']}"):
                    st.session_state.user_data['saved_colleges'].append(college['name'])
                    st.success(f"Saved {college['name']}!")

def show_scholarships():
    st.markdown("<h1 style='font-size: 2.5rem; font-weight: 800; color: var(--text-primary); margin: 2rem 0;'>Scholarship Finder 💰</h1>", unsafe_allow_html=True)
    
    scholarships_df = load_scholarships()
    user_gpa = st.session_state.user_data['gpa_weighted']
    
    qualified = scholarships_df[scholarships_df['min_gpa'] <= user_gpa].copy()
    
    st.markdown(f"""
    <div class='info-modern'>
        You qualify for <strong>{len(qualified)}</strong> scholarships based on your GPA!
    </div>
    """, unsafe_allow_html=True)
    
    for _, scholarship in qualified.iterrows():
        with st.expander(f"💰 **{scholarship['name']}** | {scholarship['amount']}"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Award", scholarship['amount'])
                st.metric("Category", scholarship['category'])
            
            with col2:
                st.metric("Deadline", scholarship['deadline'])
                st.metric("Min GPA", f"{scholarship['min_gpa']:.1f}")
            
            with col3:
                st.write(f"**Your GPA:** {user_gpa:.2f}")
                st.write(f"**Status:** ✅ Qualified")
            
            if st.button(f"📝 Start Application", key=f"apply_{scholarship['name']}"):
                st.success("Application started! Check your email.")

def show_essays():
    st.markdown("<h1 style='font-size: 2.5rem; font-weight: 800; color: var(--text-primary); margin: 2rem 0;'>Essay Manager ✍️</h1>", unsafe_allow_html=True)
    
    tabs = st.tabs(["📝 My Essays", "➕ New Essay", "🛒 Get Help"])
    
    with tabs[0]:
        if not st.session_state.user_data['essays']:
            st.info("No essays yet. Start writing in the 'New Essay' tab!")
        else:
            for idx, essay in enumerate(st.session_state.user_data['essays']):
                with st.expander(f"📄 {essay['title']}"):
                    st.write(f"**Type:** {essay['type']}")
                    st.write(f"**Status:** {essay['status']}")
                    st.write(f"**Word Count:** {essay['word_count']}")
                    st.text_area("Content", essay['content'], height=200, disabled=True, key=f"essay_view_{idx}")
    
    with tabs[1]:
        st.markdown("### Start a New Essay")
        
        with st.form("new_essay"):
            title = st.text_input("Essay Title")
            essay_type = st.selectbox("Type", ["Common App", "Supplemental", "Scholarship"])
            prompt = st.text_area("Prompt")
            content = st.text_area("Your Essay", height=300)
            
            if st.form_submit_button("Save Draft"):
                if title and content:
                    new_essay = {
                        'title': title,
                        'type': essay_type,
                        'prompt': prompt,
                        'content': content,
                        'word_count': len(content.split()),
                        'status': 'Draft',
                        'date': str(datetime.now())
                    }
                    st.session_state.user_data['essays'].append(new_essay)
                    st.success("Essay saved!")
                    st.rerun()
                else:
                    st.error("Please provide at least a title and content")
    
    with tabs[2]:
        st.markdown("### Professional Essay Services")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='glass-card' style='text-align: center;'>
                <h3 style='color: var(--text-primary);'>Essay Editing</h3>
                <div style='font-size: 3rem; font-weight: 800; background: var(--gradient-1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 1rem 0;'>$35</div>
                <p style='color: var(--text-secondary);'>2 rounds of professional edits</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Purchase Editing", use_container_width=True, key="buy_edit"):
                st.success("Service purchased! Check your email for next steps.")
        
        with col2:
            st.markdown("""
            <div class='glass-card' style='text-align: center;'>
                <h3 style='color: var(--text-primary);'>Full Support</h3>
                <div style='font-size: 3rem; font-weight: 800; background: var(--gradient-1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 1rem 0;'>$80</div>
                <p style='color: var(--text-secondary);'>Brainstorming + 2 edits</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Purchase Full Support", use_container_width=True, key="buy_full"):
                st.success("Service purchased! Check your email for next steps.")

def show_calendar():
    st.markdown("<h1 style='font-size: 2.5rem; font-weight: 800; color: var(--text-primary); margin: 2rem 0;'>Application Calendar 📅</h1>", unsafe_allow_html=True)
    
    events = [
        {"date": "Nov 1, 2025", "title": "Early Decision Deadline", "type": "deadline"},
        {"date": "Nov 5, 2025", "title": "Meeting with Mentor Sarah", "type": "meeting"},
        {"date": "Nov 15, 2025", "title": "Early Action Deadline", "type": "deadline"},
        {"date": "Dec 1, 2025", "title": "Essay Review Session", "type": "meeting"},
        {"date": "Jan 1, 2026", "title": "Regular Decision Deadline", "type": "deadline"},
    ]
    
    for event in events:
        if event['type'] == 'deadline':
            st.warning(f"📌 **{event['title']}** - {event['date']}")
        else:
            st.info(f"📅 **{event['title']}** - {event['date']}")

def show_messages():
    st.markdown("<h1 style='font-size: 2.5rem; font-weight: 800; color: var(--text-primary); margin: 2rem 0;'>Messages 💬</h1>", unsafe_allow_html=True)
    
    if not st.session_state.user_data.get('mentor_matched'):
        st.info("👥 You haven't been matched with a mentor yet. Visit the 'Find Mentor' page to connect!")
        return
    
    mentor = st.session_state.user_data['mentor_info']
    
    st.markdown(f"""
    <div class='glass-card'>
        <h3 style='color: var(--text-primary);'>Chat with {mentor['name']}</h3>
        <p style='color: var(--text-secondary);'>{mentor['school']} • {mentor['major']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([5, 1])
    with col1:
        new_message = st.text_input("Type a message...", label_visibility="collapsed", key="msg_input")
    with col2:
        if st.button("Send", use_container_width=True):
            if new_message:
                st.success("Message sent!")
                st.rerun()

def show_settings():
    st.markdown("<h1 style='font-size: 2.5rem; font-weight: 800; color: var(--text-primary); margin: 2rem 0;'>Settings ⚙️</h1>", unsafe_allow_html=True)
    
    tabs = st.tabs(["👤 Profile", "🔔 Notifications", "💳 Billing"])
    
    with tabs[0]:
        st.markdown("### Your Profile")
        
        with st.form("profile_form"):
            name = st.text_input("Name", value=st.session_state.user_data.get('name', ''))
            email = st.text_input("Email", value=st.session_state.user_data.get('email', ''))
            
            col1, col2 = st.columns(2)
            with col1:
                sat = st.number_input("SAT Score", 400, 1600, st.session_state.user_data['sat_score'])
            with col2:
                gpa = st.number_input("GPA (Weighted)", 0.0, 5.0, st.session_state.user_data['gpa_weighted'], 0.01)
            
            if st.form_submit_button("Save Changes"):
                st.session_state.user_data['name'] = name
                st.session_state.user_data['email'] = email
                st.session_state.user_data['sat_score'] = sat
                st.session_state.user_data['gpa_weighted'] = gpa
                st.success("Profile updated!")
    
    with tabs[1]:
        st.markdown("### Notification Preferences")
        
        st.checkbox("Email notifications for deadlines", value=True)
        st.checkbox("SMS reminders for meetings", value=True)
        st.checkbox("Weekly progress reports", value=True)
        st.checkbox("New scholarship matches", value=True)
    
    with tabs[2]:
        st.markdown("### Billing Information")
        st.info("💡 You haven't purchased any services yet.")

def main():
    if not st.session_state.authenticated:
        if st.session_state.current_page == 'landing':
            show_landing_page()
        elif st.session_state.current_page == 'signup':
            show_signup_page()
        elif st.session_state.current_page == 'signin':
            show_signin_page()
    else:
        show_dashboard()

if __name__ == "__main__":
    main()