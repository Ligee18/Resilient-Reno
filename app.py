import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ResilientReno | Home Resilience Engine",
    page_icon="🛡️",
    layout="centered"
)

# 2. Custom CSS & Visual Enhancement
st.markdown("""
    <style>
    /* Sleek Dark Theme Polish */
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 28px;
        border-radius: 14px;
        color: #ffffff;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        border: 1px solid #334155;
    }
    .main-header h1 {
        color: #38bdf8 !important;
        font-size: 2.2rem;
        margin-bottom: 6px;
        font-weight: 700;
    }
    .slogan-tag {
        font-style: italic;
        color: #f59e0b;
        font-size: 1.05rem;
        font-weight: 500;
    }
    
    /* Intro Banner Box */
    .info-banner {
        background-color: #1e293b;
        border-left: 4px solid #38bdf8;
        padding: 16px 20px;
        border-radius: 10px;
        margin-bottom: 24px;
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* Clean Modern Retrofit Cards */
    .rec-card {
        background-color: #0f172a;
        border: 1px solid #334155;
        border-left: 5px solid #38bdf8;
        padding: 16px 20px;
        border-radius: 10px;
        margin-bottom: 12px;
        font-size: 0.98rem;
        color: #f8fafc;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    .rec-card strong {
        color: #38bdf8;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header & Slogan
st.markdown("""
    <div class="main-header">
        <h1>🛡️ ResilientReno</h1>
        <div class="slogan-tag">"An ounce of prevention is worth a pound of cure."</div>
    </div>
""", unsafe_allow_html=True)

# 4. New Top Intro Section: What this is & Why it matters
st.markdown("""
    <div class="info-banner">
        <strong>💡 What is ResilientReno & Why Does It Matter?</strong><br>
        Extreme weather like severe basement flooding, high windstorms, and wildfire smoke is hitting Canadian homes more often, causing thousands of dollars in unexpected damage. Most home improvement advice online is way too broad. <strong>ResilientReno</strong> takes local weather hazard data across Canadian towns and turns it into a targeted, practical home protection plan so you can spend your budget on repairs that actually matter for your area.
    </div>
""", unsafe_allow_html=True)

# 5. Canadian Regional Hazard Database (City + FSA)
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

# 6. Everyday Language Retrofit Database
RETROFIT_DB = {
    "flood": [
        "<strong>Install a Backwater Valve:</strong> Put a one-way sewer valve on your main line so dirty storm sewer water can't back up into your basement drain during heavy rainstorms.",
        "<strong>Add Sump Pump Battery Backup:</strong> Get a secondary battery pack for your sump pump so it keeps pushing water away from your foundation even if power goes out.",
        "<strong>Fix Your Soil Grading:</strong> Make sure the dirt and gardens around your house slope downward at least 5% away from your walls so rainwater flows toward the street instead of pooling around your basement."
    ],
    "wildfire": [
        "<strong>Build a Gravel Firebreak:</strong> Swap out wood mulch or grass within 1.5 meters of your exterior walls for gravel or river rocks so floating embers can't ignite your siding.",
        "<strong>Put Mesh Over Vents:</strong> Cover your attic and soffit vents with 1/8-inch metal mesh screens to block blowing embers from getting into your roof structure.",
        "<strong>Upgrade Ground Siding:</strong> Replace old wood siding near ground level with non-flammable fiber-cement boards or brick panels."
    ],
    "wind": [
        "<strong>Install Roof Hurricane Clips:</strong> Secure roof trusses directly to your wall frames using metal hurricane straps to prevent strong roof uplift in high-wind storms.",
        "<strong>Brace Your Garage Door:</strong> Add vertical metal bracing kits to your garage door to keep strong wind pressure from popping it off the tracks.",
        "<strong>Upgrade Windows to Impact Glass:</strong> Swap out basement and main-floor glass for laminated impact-resistant glass that won't shatter when hit by flying debris."
    ]
}

# 7. Interactive Dropdown Selection
st.subheader("📍 Step 1: Select Your Location")
selected_location = st.selectbox(
    "Choose your city and area postal code:",
    options=["-- Select City & Postal Code --"] + list(LOCATION_RISK_DB.keys()),
    key="location_selector"
)

# 8. Dynamic Output Container (Resets completely on selection change)
output_container = st.container()

with output_container:
    if selected_location and selected_location != "-- Select City & Postal Code --":
        data = LOCATION_RISK_DB[selected_location]
        
        st.divider()
        st.subheader("📊 Step 2: Local Weather Risk Levels")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Flood Risk", data["flood"])
        col2.metric("Wildfire Risk", data["wildfire"])
        col3.metric("Wind / Storm Risk", data["wind"])
        
        st.divider()
        st.subheader("🛠️ Step 3: Most Important Upgrades for Your House")
        
        # Priority Logic: Filter risks flagged as High or Medium
        actions = []
        for hazard in ["flood", "wildfire", "wind"]:
            if data[hazard] in ["High", "Medium"]:
                actions.extend(RETROFIT_DB[hazard])
                
        # Output clean card layout
        for rec in actions[:5]:
            st.markdown(f'<div class="rec-card">⚡ {rec}</div>', unsafe_allow_html=True)
    else:
        st.info("👈 Select a location from the dropdown above to view risk levels and recommended home fixes.")

st.divider()

# 9. Waterloo Management Engineering Specific Context
with st.expander("📌 Project Context & Waterloo Management Engineering Connection (AIF)"):
    st.markdown("""
    **Why I Built This Project:**
    I built ResilientReno to bridge the gap between complex climate risk data and everyday decision-making for Canadian homeowners. After seeing family and neighbors deal with costly basement flood damage, I realized that people rarely do preventive retrofits because they don't know which fixes matter most for their exact neighborhood.

    **Direct Connection to Waterloo Management Engineering:**
    Management Engineering at Waterloo focuses on using data analytics, software, and operations research to design efficient systems and optimize decision-making. ResilientReno reflects these core Management Engineering principles:

    * **Decision-Support Systems:** Instead of making users read lengthy climate reports, this tool filters and structures data so users can make an immediate, informed choice on where to spend money.
    * **Resource Allocation & Priority Optimization:** Homeowners have limited home improvement budgets. The matching logic ranks retrofits based on local hazard exposure so resources go to the highest risk-reduction projects first.
    * **Systemic Risk Reduction:** By encouraging preventive retrofits at the household level, this project addresses broader systemic losses for municipal infrastructure and home insurance providers.

    **Future Engineering Iterations:**
    I want to expand this tool by connecting it to GIS mapping tools (like OpenStreetMap APIs) to evaluate micro-level property features, such as roof elevation, slope gradients, and proximity to forest boundaries.
    """)

st.caption("ResilientReno | High School Project built for Waterloo Management Engineering Context")
