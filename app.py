import streamlit as st

# 1. Page Configuration (Centered Grid Layout)
st.set_page_config(
    page_title="ResilientReno | Home Resilience Engine",
    page_icon="🛡️",
    layout="wide"
)

# 2. Premium SaaS Theme Custom CSS
st.markdown("""
    <style>
    /* Dark Theme Base */
    .stAppViewContainer, .stApp {
        background-color: #0b0f17 !important;
        color: #f8fafc !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Restrain Max-Width for Optimal Visual Balance & Line Length */
    .main .block-container {
        max-width: 1080px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 4rem !important;
        margin: 0 auto !important;
    }
    
    /* Typography Overrides */
    h1, h2, h3, h4, h5, h6, p, label, span, div, li {
        color: #f8fafc !important;
    }

    /* Input Select Box Styling */
    div[data-baseweb="select"] > div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }
    div[data-baseweb="select"] * {
        color: #ffffff !important;
    }

    /* Popover Dropdown Container Background */
    [data-baseweb="popover"],
    [data-baseweb="popover"] > div,
    div[role="listbox"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
    }

    /* Dropdown Menu Text & Hover States */
    div[role="listbox"] li,
    div[role="listbox"] li *,
    ul[data-baseweb="menu"] li,
    ul[data-baseweb="menu"] li * {
        color: #e2e8f0 !important;
        background-color: transparent !important;
    }
    div[role="listbox"] li:hover,
    div[role="listbox"] li:hover * {
        background-color: #334155 !important;
        color: #38bdf8 !important;
    }

    /* Clean Hero Banner */
    .hero-card {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 36px 40px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #38bdf8 !important;
        letter-spacing: -0.5px;
        margin-bottom: 6px;
    }
    .hero-subtitle {
        color: #94a3b8 !important;
        font-size: 1.05rem;
        font-style: italic;
    }

    /* Info Card */
    .info-card {
        background-color: #131c2e;
        border: 1px solid #1e293b;
        border-left: 4px solid #38bdf8;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 28px;
        line-height: 1.6;
        color: #cbd5e1 !important;
    }

    /* Expanders Clean Styling */
    .stExpander {
        background-color: #131c2e !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
        margin-bottom: 20px !important;
    }
    .stExpander summary {
        color: #94a3b8 !important;
        font-weight: 600 !important;
    }

    /* Minimalist Risk Badges */
    .badge-card {
        background: #131c2e;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    .badge-label {
        color: #94a3b8 !important;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-pill {
        display: inline-block;
        padding: 6px 18px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.95rem;
    }
    .badge-high {
        background-color: rgba(239, 68, 68, 0.15);
        color: #fca5a5 !important;
        border: 1px solid rgba(239, 68, 68, 0.4);
    }
    .badge-medium {
        background-color: rgba(245, 158, 11, 0.15);
        color: #fde047 !important;
        border: 1px solid rgba(245, 158, 11, 0.4);
    }
    .badge-low {
        background-color: rgba(16, 185, 129, 0.15);
        color: #6ee7b7 !important;
        border: 1px solid rgba(16, 185, 129, 0.4);
    }

    /* Recommendation Cards */
    .rec-card {
        background-color: #131c2e;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 14px;
        color: #e2e8f0 !important;
        font-size: 1rem;
        line-height: 1.6;
        transition: border-color 0.2s ease;
    }
    .rec-card:hover {
        border-color: #38bdf8;
    }
    .rec-card strong {
        color: #38bdf8 !important;
    }

    .footer-text {
        color: #64748b !important;
        font-size: 0.85rem;
        text-align: center;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Title Block
st.markdown("""
    <div class="hero-card">
        <div class="hero-title">🛡️ ResilientReno</div>
        <div class="hero-subtitle">"An ounce of prevention is worth a pound of cure."</div>
    </div>
""", unsafe_allow_html=True)

# 4. Collapsible About Me Menu
with st.expander("👋 About the Creator"):
    st.markdown("""
    Hi! My name is **Elijah Lloyd**. I'm a Grade 12 student passionate about software engineering, data analytics, and building tools that tackle practical problems. I designed **ResilientReno** to explore how decision-support systems can translate complex environmental datasets into straightforward, actionable insights for everyday homeowners.
    """)

# 5. Purpose Banner
st.markdown("""
    <div class="info-card">
        <strong style="color: #38bdf8;">💡 What is ResilientReno & Why Does It Matter?</strong><br>
        Extreme weather like severe basement flooding, high windstorms, and wildfire smoke is hitting Canadian homes more often, causing thousands of dollars in unexpected damage. Most home improvement advice online is way too broad. <strong>ResilientReno</strong> takes local weather hazard data across Canadian towns and turns it into a targeted, practical home protection plan so homeowners can spend their budget on repairs that actually matter for their area.
    </div>
""", unsafe_allow_html=True)

# 6. Database Configuration
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

TIERED_RETROFIT_DB = {
    "flood": {
        "High": [
            "<strong>Install a Backwater Valve:</strong> Put a one-way sewer valve on your main line so dirty storm sewer water can't back up into your basement drain during heavy rainstorms.",
            "<strong>Add Sump Pump Battery Backup:</strong> Get a secondary battery pack for your sump pump so it keeps pushing water away from your foundation even if power goes out.",
            "<strong>Fix Your Soil Grading:</strong> Make sure the dirt and gardens around your house slope downward at least 5% away from your walls so rainwater flows toward the street instead of pooling around your basement.",
            "<strong>Waterproof External Walls:</strong> Apply a rubberized asphalt membrane to exterior foundation walls below ground level."
        ],
        "Medium": [
            "<strong>Extend Downspout Discharges:</strong> Add extension pipes so downspouts dump rainwater at least 6 feet away from your foundation wall.",
            "<strong>Seal Foundation Wall Cracks:</strong> Fill concrete basement wall cracks using hydraulic cement or high-grade polyurethane sealant to block ground leaks.",
            "<strong>Window Well Covers:</strong> Fit clear polycarbonate domes over basement window wells to stop water accumulation from pouring in."
        ],
        "Low": [
            "<strong>Elevate Basement Appliances:</strong> Mount laundry units, water heaters, and furnaces on 6-inch concrete pedestals off the floor.",
            "<strong>Install Sump Pump Smart Alarm:</strong> Add a Wi-Fi water sensor inside your sump basin to alert your smartphone before a pump fails.",
            "<strong>Install Permeable Driveway Pavers:</strong> Replace solid concrete walkways with porous pavers so rainwater drains naturally into ground soil."
        ]
    },
    "wildfire": {
        "High": [
            "<strong>Build a Gravel Firebreak:</strong> Swap out wood mulch or grass within 1.5 meters of your exterior walls for gravel or river rocks so floating embers can't ignite your siding.",
            "<strong>Put Mesh Over Vents:</strong> Cover your attic and soffit vents with 1/8-inch metal mesh screens to block blowing embers from getting into your roof structure.",
            "<strong>Upgrade Ground Siding:</strong> Replace old wood siding near ground level with non-flammable fiber-cement boards or brick panels.",
            "<strong>Install Class-A Rated Roofing:</strong> Choose asphalt shingles or metal roofing systems certified with the highest fire-resistance rating."
        ],
        "Medium": [
            "<strong>Trim Tree Branches Near Roof:</strong> Prune overhead tree branches so they stay at least 10 feet away from your rooflines and chimneys.",
            "<strong>Store Firewood Away From House:</strong> Move wood piles at least 30 feet away from exterior walls and wooden decks.",
            "<strong>Enclose Open Deck Undersides:</strong> Wrap open space beneath elevated wooden decks using metal mesh or fire-resistant board panels."
        ],
        "Low": [
            "<strong>Clear Gutter Debris Weekly:</strong> Remove dried pine needles and leaves from roof gutters where embers easily spark fires.",
            "<strong>Upgrade Window Screen Material:</strong> Swap plastic window mesh for flame-resistant bronze or aluminum mesh screens.",
            "<strong>Install External Rooftop Sprinklers:</strong> Mount roof-line water misters to soak shingles and surrounding soil during nearby wildfire warnings."
        ]
    },
    "wind": {
        "High": [
            "<strong>Install Roof Hurricane Clips:</strong> Secure roof trusses directly to your wall frames using metal hurricane straps to prevent strong roof uplift in high-wind storms.",
            "<strong>Brace Your Garage Door:</strong> Add vertical metal bracing kits to your garage door to keep strong wind pressure from popping it off the tracks.",
            "<strong>Upgrade Windows to Impact Glass:</strong> Swap out basement and main-floor glass for laminated impact-resistant glass that won't shatter when hit by flying debris.",
            "<strong>Reinforce Entry Door Locks:</strong> Add heavy-duty three-point deadbolt locks to keep exterior doors from blowing open in severe pressure shifts."
        ],
        "Medium": [
            "<strong>Anchor Outdoor Sheds & Structures:</strong> Secure yard sheds, pergolas, and heavy furniture into concrete footings with steel tie-down straps.",
            "<strong>Install Storm Shutters:</strong> Mount exterior aluminum or steel shutters that fold closed over glass windows during storm alerts.",
            "<strong>Reinforce Roof Sheathing Straps:</strong> Add ring-shank nails along roof plywood deck seams to double resistance against wind suction."
        ],
        "Low": [
            "<strong>Secure Loose Roof Flashing:</strong> Seal all edge flashing around chimneys, skylights, and vents with heavy-duty roof adhesive sealant.",
            "<strong>Replace Dead Yard Trees:</strong> Remove rotting trees or compromised branches that could collapse onto your house during high-wind gusts.",
            "<strong>Upgrade Vinyl Siding Fasteners:</strong> Fasten exterior wall siding panels with wide-head galvanized nails spaced every 12 inches."
        ]
    }
}

# Helper Function for Badges
def render_badge(label, level):
    css_class = f"badge-{level.lower()}"
    return f"""
    <div class="badge-card">
        <div class="badge-label">{label}</div>
        <span class="badge-pill {css_class}">{level} Risk</span>
    </div>
    """

# 7. Step 1: Location Input
st.markdown("### 📍 Step 1: Select Your Location")
selected_location = st.selectbox(
    "Choose your city and area postal code:",
    options=["-- Select City & Postal Code --"] + list(LOCATION_RISK_DB.keys()),
    key="location_selector"
)

# 8. Dynamic Step 2 & 3 Output
if selected_location and selected_location != "-- Select City & Postal Code --":
    data = LOCATION_RISK_DB[selected_location]
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📊 Step 2: Local Risk Profile")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(render_badge("Flood Exposure", data["flood"]), unsafe_allow_html=True)
    with col2:
        st.markdown(render_badge("Wildfire Exposure", data["wildfire"]), unsafe_allow_html=True)
    with col3:
        st.markdown(render_badge("Wind Hazard", data["wind"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🛠️ Step 3: Priority Action Plan")
    
    # Logic for weighted priority scoring
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    scored_actions = []
    
    for hazard in ["flood", "wildfire", "wind"]:
        risk_level = data[hazard]
        weight = priority_map[risk_level]
        for item in TIERED_RETROFIT_DB[hazard][risk_level]:
            scored_actions.append((weight, item))
            
    scored_actions.sort(key=lambda x: x[0], reverse=True)
    top_5_actions = [item[1] for item in scored_actions[:5]]
    
    for rec in top_5_actions:
        st.markdown(f'<div class="rec-card">⚡ {rec}</div>', unsafe_allow_html=True)

else:
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Select a location from the dropdown above to view risk levels and recommended home fixes.")

st.markdown("<br>", unsafe_allow_html=True)

# 9. Technical Architecture Expander
with st.expander("⚙️ System Architecture & Engineering Methodology"):
    st.markdown("""
    **Problem Context:**
    Climate risk data is publicly available, but it is rarely actionable for individual property owners. Homeowners frequently face information overload, making it difficult to allocate renovation capital efficiently. ResilientReno was engineered to bridge the gap between raw regional risk indicators and personalized decision-making.

    **Core Engineering Implementation:**
    The engine relies on three primary systems engineering concepts:

    * **Decision-Support Architecture:** Converts multi-variable climate data into localized dynamic recommendations, eliminating manual analysis for the user.
    * **Multi-Criteria Priority Logic:** Uses a weighted scoring algorithm to rank mitigation strategies based on local severity tiers (High, Medium, Low), ensuring high-impact interventions take precedence.
    * **Information Streamlining:** Filters complex hazard metrics down to top actionable outputs, reducing process friction and guiding efficient resource allocation.

    **Technical Roadmap:**
    Future development will focus on integrating geospatial APIs (such as OpenStreetMap and terrain elevation datasets) to incorporate micro-location variables like property elevation, watershed proximity, and local vegetation density into the scoring matrix.
    """)

st.markdown('<div class="footer-text">ResilientReno | Built by Elijah Lloyd</div>', unsafe_allow_html=True)
