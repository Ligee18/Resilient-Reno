import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ResilientReno | Home Resilience Engine",
    page_icon="🛡️",
    layout="centered"
)

# 2. Custom Styling & Visual "Aura"
st.markdown("""
    <style>
    /* Gradient Header Background */
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 24px;
        border-radius: 12px;
        color: #ffffff;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .main-header h1 {
        color: #38bdf8 !important;
        margin-bottom: 4px;
    }
    .slogan-tag {
        font-style: italic;
        color: #94a3b8;
        font-size: 1rem;
    }
    
    /* Clean Recommendation Cards */
    .rec-card {
        background-color: #1e293b;
        border-left: 5px solid #38bdf8;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 12px;
        font-size: 0.98rem;
        color: #f8fafc;
    }
    
    /* Risk Badge Highlights */
    .risk-high { color: #ef4444; font-weight: bold; }
    .risk-med { color: #f59e0b; font-weight: bold; }
    .risk-low { color: #10b981; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. Header & Slogan Setup
st.markdown("""
    <div class="main-header">
        <h1>🛡️ ResilientReno</h1>
        <div class="slogan-tag">"An ounce of prevention is worth a pound of cure."</div>
        <p style="margin-top: 10px; color: #cbd5e1;">
            A decision-support tool built to map regional natural hazard risks 
            to prioritized home retrofits across Canadian communities.
        </p>
    </div>
""", unsafe_allow_html=True)

# 4. Regional Hazard Database (City + FSA)
LOCATION_RISK_DB = {
    "Burlington / Halton Region (L7R)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Waterloo / Kitchener (N2L)": {"flood": "High", "wildfire": "Low", "wind": "Medium"},
    "Toronto - Downtown Core (M5V)": {"flood": "Medium", "wildfire": "Low", "wind": "High"},
    "Toronto - North York (M2N)": {"flood": "Medium", "wildfire": "Low", "wind": "Medium"},
    "Mississauga / Peel (L5B)": {"flood": "High", "wildfire": "Low", "wind": "Medium"},
    "Hamilton / Mountain (L8P)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Ottawa Region (K1P)": {"flood": "High", "wildfire": "Medium", "wind": "Medium"},
    "London / Middlesex (N6A)": {"flood": "Medium", "wildfire": "Low", "wind": "High"},
    "Windsor / Essex (N9A)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Barrie / Simcoe (L4M)": {"flood": "Medium", "wildfire": "Medium", "wind": "High"},
    "Calgary - Central (T2P)": {"flood": "Medium", "wildfire": "High", "wind": "Medium"},
    "Edmonton - Downtown (T5J)": {"flood": "Medium", "wildfire": "High", "wind": "Medium"},
    "Vancouver - Central (V6B)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Surrey / Fraser Valley (V3T)": {"flood": "High", "wildfire": "Medium", "wind": "Medium"},
    "Kelowna / Okanagan (V1Y)": {"flood": "Low", "wildfire": "High", "wind": "Medium"},
    "Victoria / Island (V8W)": {"flood": "High", "wildfire": "Medium", "wind": "High"},
    "Halifax Region (B3J)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Winnipeg / Red River (R3C)": {"flood": "High", "wildfire": "Medium", "wind": "Medium"},
    "Montreal - Downtown (H3B)": {"flood": "Medium", "wildfire": "Low", "wind": "Medium"},
    "Quebec City (G1R)": {"flood": "High", "wildfire": "Low", "wind": "Medium"},
}

# 5. Retrofit Recommendations Database
RETROFIT_DB = {
    "flood": [
        "Install a mainline sewer backwater valve to stop basement flooding during heavy rain.",
        "Add a battery-powered backup power system to the main sump pump.",
        "Fix perimeter soil grading so land slopes outward at least 5% away from foundation walls."
    ],
    "wildfire": [
        "Create a 1.5-meter non-combustible gravel/stone border around all exterior walls.",
        "Attach 1/8-inch non-combustible metal mesh screens over attic and soffit vents.",
        "Swap out ground-level wood siding for non-flammable fiber-cement boards."
    ],
    "wind": [
        "Install metal hurricane ties at roof-to-wall joints to stop roof uplift in heavy storms.",
        "Add vertical reinforcement braces to double-car garage doors against strong winds.",
        "Upgrade ground-floor and basement windows to impact-resistant laminated glass."
    ]
}

# 6. Interactive Dropdown Selection
st.subheader("📍 Step 1: Select Location")
selected_location = st.selectbox(
    "Choose your city and Forward Sortation Area (FSA):",
    options=["-- Select City & Postal Code --"] + list(LOCATION_RISK_DB.keys()),
    key="location_selector"
)

# 7. Dynamic Output Container (Resets completely on every dropdown change)
output_container = st.container()

with output_container:
    if selected_location and selected_location != "-- Select City & Postal Code --":
        data = LOCATION_RISK_DB[selected_location]
        
        st.divider()
        st.subheader("📊 Step 2: Regional Risk Analysis")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Flood Risk", data["flood"])
        col2.metric("Wildfire Risk", data["wildfire"])
        col3.metric("Wind / Storm Risk", data["wind"])
        
        st.divider()
        st.subheader("🛠️ Step 3: Top Priority Retrofits for Your Area")
        
        # Priority Logic: Filter risks flagged as High or Medium
        actions = []
        for hazard in ["flood", "wildfire", "wind"]:
            if data[hazard] in ["High", "Medium"]:
                actions.extend(RETROFIT_DB[hazard])
                
        # Output clean card layout without messy numbers
        for rec in actions[:5]:
            st.markdown(f'<div class="rec-card">⚡ {rec}</div>', unsafe_allow_html=True)
    else:
        st.info("👈 Select a location from the dropdown above to run the resilience assessment.")

st.divider()

# 8. Waterloo Management Engineering AIF Context
with st.expander("📌 Project Context & Waterloo Management Engineering Connection (AIF)"):
    st.markdown("""
    **Why I Built This (High School Project Background):**
    I created ResilientReno as a side project to explore how software and data tools can solve practical everyday problems like climate-driven home damage. Most online advice for home improvement is way too broad. I wanted to build something interactive that takes complex regional hazard data and turns it into immediate, actionable steps for homeowners.

    **Connection to Waterloo Management Engineering Curriculum:**
    * **Decision-Support Systems (`MSE 436`):** This app acts as a lightweight decision engine, taking location inputs and outputting a custom risk mitigation plan so users can make decisions without getting bogged down by raw numbers.
    * **Process Optimization (`MSE 100` / `MSE 131`):** Homeowners usually have limited budgets. By ranking retrofits according to local risk levels, the app helps prioritize projects with the highest risk reduction value first.
    * **Software & Data Engineering (`MSE 121`):** Built entirely in Python using Streamlit, this project taught me how to structure conditional logic and build clean web interfaces.

    **Future Upgrades I Plan to Build:**
    Next, I want to connect this to real-time weather APIs and GIS mapping tools (like OpenStreetMap) to pull property-specific features like roof slope and vegetation proximity for micro-targeted suggestions.
    """)

st.caption("ResilientReno | High School Side Project built for Waterloo Management Engineering AIF Context")
