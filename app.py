# 2. Custom CSS & High-Contrast Visual Enhancement
st.markdown("""
    <style>
    /* Full Dark Background Base */
    .stAppViewContainer, .stApp {
        background-color: #0b0f19 !important;
        color: #ffffff !important;
    }
    
    /* Global Typography */
    h1, h2, h3, h4, h5, h6, p, label, span, div, li {
        color: #f8fafc !important;
    }

    /* FIX: Force Dropdown Input Box Text Dark */
    div[data-baseweb="select"] * {
        color: #0f172a !important;
    }

    /* FIX: Dropdown Popover List Styling (Dark Background + Bright White Text) */
    ul[data-baseweb="menu"], 
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] div {
        background-color: #0f172a !important;
    }

    li[data-baseweb="option"], 
    div[data-baseweb="popover"] li,
    div[data-baseweb="popover"] span {
        background-color: #0f172a !important;
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Hover state for dropdown options */
    li[data-baseweb="option"]:hover,
    li[aria-selected="true"] {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
    }
    
    /* Header Container */
    .main-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 30px;
        border-radius: 16px;
        color: #ffffff !important;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px -5px rgba(56, 189, 248, 0.15);
        border: 1px solid #334155;
    }
    .main-header h1 {
        color: #38bdf8 !important;
        font-size: 2.3rem;
        margin-bottom: 6px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    .slogan-tag {
        font-style: italic;
        color: #fbbf24 !important;
        font-size: 1.05rem;
        font-weight: 600;
    }
    
    /* About Me Box */
    .about-me-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid #38bdf8;
        padding: 20px 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        color: #f8fafc !important;
        font-size: 0.95rem;
        line-height: 1.6;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .about-me-box strong {
        color: #38bdf8 !important;
    }

    /* Intro Banner Box */
    .info-banner {
        background-color: #1e293b;
        border-left: 4px solid #38bdf8;
        padding: 18px 22px;
        border-radius: 12px;
        margin-bottom: 24px;
        color: #ffffff !important;
        font-size: 0.95rem;
        line-height: 1.6;
        border-top: 1px solid #334155;
        border-right: 1px solid #334155;
        border-bottom: 1px solid #334155;
    }

    /* Modern Retrofit Cards */
    .rec-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-left: 5px solid #38bdf8;
        padding: 20px 24px;
        border-radius: 12px;
        margin-bottom: 16px;
        font-size: 0.98rem;
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    .rec-card strong {
        color: #38bdf8 !important;
    }

    /* Risk Badges */
    .badge {
        display: inline-block;
        padding: 8px 18px;
        border-radius: 20px;
        font-weight: 800;
        font-size: 0.95rem;
        text-align: center;
        margin-top: 6px;
        letter-spacing: 0.5px;
    }
    .badge-high {
        background-color: rgba(239, 68, 68, 0.2);
        color: #fca5a5 !important;
        border: 1px solid #ef4444;
        box-shadow: 0 0 10px rgba(239, 68, 68, 0.2);
    }
    .badge-medium {
        background-color: rgba(245, 158, 11, 0.2);
        color: #fde047 !important;
        border: 1px solid #f59e0b;
        box-shadow: 0 0 10px rgba(245, 158, 11, 0.2);
    }
    .badge-low {
        background-color: rgba(16, 185, 129, 0.2);
        color: #6ee7b7 !important;
        border: 1px solid #10b981;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.2);
    }

    /* Expander & Footer Text Contrast Fixes */
    .stExpander {
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
    }
    .stExpander p, .stExpander span, .stExpander li, .stExpander div {
        color: #ffffff !important;
    }
    .stExpander strong {
        color: #38bdf8 !important;
    }
    .footer-text {
        color: #94a3b8 !important;
        font-size: 0.85rem;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)
