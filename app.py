import streamlit as st

# 1. Page Configuration (Set to Wide Layout)
st.set_page_config(
    page_title="ResilientReno | Home Resilience Engine",
    page_icon="🛡️",
    layout="wide"
)

# 2. Custom CSS & Full-Width Visual Enhancement
st.markdown("""
    <style>
    /* Full Dark Background Base */
    .stAppViewContainer, .stApp {
        background-color: #0b0f19 !important;
        color: #ffffff !important;
    }

    /* Expand Max Page Width and Add Breathable Margins */
    .main .block-container {
        max-width: 92% !important;
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }
    
    /* Global Typography */
    h1, h2, h3, h4, h5, h6, p, label, span, div, li {
        color: #f8fafc !important;
    }

    /* FIX: Selected Text in Main Input Box */
    div[data-baseweb="select"] * {
        color: #0f172a !important;
    }

    /* FIX: Popover Dropdown Container Background */
    [data-baseweb="popover"],
    [data-baseweb="popover"] > div,
    div[role="listbox"] {
        background-color: #ffffff !important;
    }

    /* FIX: Force Dropdown Menu Text Dark Slate Blue */
    div[role="listbox"] li,
    div[role="listbox"] li *,
    div[role="listbox"] span,
    div[role="listbox"] div,
    ul[data-baseweb="menu"] li,
    ul[data-baseweb="menu"] li * {
        color: #0f172a !important;
        background-color: transparent !important;
        font-weight: 600 !important;
    }

    /* FIX: Hover & Active Selection Highlight */
    div[role="listbox"] li:hover,
    div[role="listbox"] li:hover *,
    div[role="listbox"] li[aria-selected="true"],
    div[role="listbox"] li[aria-selected="true"] * {
        background-color: #e2e8f0 !important;
        color: #0284c7 !important;
    }
    
    /* Header Container */
    .main-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 32px 40px;
        border-radius: 16px;
        color: #ffffff !important;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px -5px rgba(56, 189, 248, 0.15);
        border: 1px solid #334155;
    }
    .main-header h1 {
        color: #38bdf8 !important;
        font-size: 2.6rem;
        margin-bottom: 8px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    .slogan-tag {
        font-style: italic;
        color: #fbbf24 !important;
        font-size: 1.1rem;
        font-weight: 600;
    }

    /* Intro Banner Box */
    .info-banner {
        background-color: #1e293b;
        border-left: 5px solid #38bdf8;
        padding: 22px 28px;
        border-radius: 12px;
        margin-bottom: 28px;
        color: #ffffff !important;
        font-size: 1rem;
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
        padding: 22px 26px;
        border-radius: 12px;
        margin-bottom: 18px;
        font-size: 1.02rem;
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .rec-card:hover {
        transform: translateY(-2px);
        border-color: #38bdf8;
    }
    .rec-card strong {
        color: #38bdf8 !important;
    }

    /* Risk Badges */
    .badge {
        display: inline-block;
        padding: 10px 24px;
        border-radius: 20px;
        font-weight: 800;
        font-size: 1.05rem;
        text-align: center;
        margin-top: 8px;
        letter-spacing: 0.5px;
    }
    .badge-high {
        background-color: rgba(239, 68, 68, 0.2);
        color: #fca5a5 !important;
        border: 1px solid #ef4444;
        box-shadow: 0 0 12px rgba(239, 68, 68, 0.25);
    }
    .badge-medium {
        background-color: rgba(245, 158, 11, 0.2);
        color: #fde047 !important;
        border: 1px solid #f59e0b;
        box-shadow: 0 0 12px rgba(245, 158, 11, 0.25);
    }
    .badge-low {
        background-color: rgba(16, 185, 129, 0.2);
        color: #6ee7b7 !important;
        border: 1px solid #10b981;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.25);
    }

    /* Expander & Footer Text Contrast Fixes */
    .stExpander {
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        margin-bottom: 16px !important;
    }
    .stExpander p, .stExpander span, .stExpander li, .stExpander div {
        color: #ffffff !important;
    }
    .stExpander strong {
        color: #38bdf8 !important;
    }
    .footer-text {
        color: #94a3b8 !important;
        font-size: 0.9rem;
        text-align: center;
        margin-top: 30px;
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

# 4. Collapsible About Me Dropdown
with st.expander("👋 About the Creator (Elijah Lloyd)"):
    st.markdown("""
    Hi! My name is **Elijah Lloyd**. I'm a Grade 12 student passionate about software engineering, data analytics, and solving complex real-world problems. I built **ResilientReno** out of curiosity to explore how data-driven decision tools can take complex environmental risk data and turn it into clear, practical solutions for real people.
    """)

# 5. Top Intro Section
st.markdown("""
    <div class="info-banner">
        <strong>💡 What is ResilientReno & Why Does It Matter?</strong><br>
        Extreme weather like severe basement flooding, high windstorms, and wildfire smoke is hitting Canadian homes more often, causing thousands of dollars in unexpected damage. Most home improvement advice online is way too broad. <strong>ResilientReno</strong> takes local weather hazard data across Canadian towns and turns it into a targeted, practical home protection plan so homeowners can spend their budget on repairs that actually matter for their area.
    </div>
""", unsafe_allow_html=True)

# 6. Canadian Regional Hazard Database
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

# 7. Retrofit Database Categorized by Severity Level
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

# Helper function to generate risk badge HTML
def get_badge_html(label, level):
    css_class = f"badge-{level.lower()}"
    return f"""
    <div style="text-align: center; padding: 10px;">
        <span style="color: #ffffff; font-size: 0.95rem; font-weight: 600;">{label}</span><br>
        <span class="badge {css_class}">{level} Risk</span>
    </div>
    """

# 8. Interactive Dropdown Selection
st.subheader("📍 Step 1: Select Your Location")
selected_location = st.selectbox(
    "Choose your city and area postal code:",
    options=["-- Select City & Postal Code --"] + list(LOCATION_RISK_DB.keys()),
    key="location_selector"
)

# 9. Dynamic Output Container
output_container = st.container()

with output_container:
    if selected_location and selected_location != "-- Select City & Postal Code --":
        data = LOCATION_RISK_DB[selected_location]
        
        st.divider()
        st.subheader("📊 Step 2: Local Weather Risk Levels")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(get_badge_html("Flood Exposure", data["flood"]), unsafe_allow_html=True)
        with col2:
            st.markdown(get_badge_html("Wildfire Exposure", data["wildfire"]), unsafe_allow_html=True)
        with col3:
            st.markdown(get_badge_html("Wind / Storm Exposure", data["wind"]), unsafe_allow_html=True)
        
        st.divider()
        st.subheader("🛠️ Step 3: Top 5 Priority Upgrades for Your Location")
        
        # Priority Logic: Assign numerical weight to risk levels (High=3, Medium=2, Low=1)
        priority_map = {"High": 3, "Medium": 2, "Low": 1}
        scored_actions = []
        
        for hazard in ["flood", "wildfire", "wind"]:
            risk_level = data[hazard]
            weight = priority_map[risk_level]
            
            options = TIERED_RETROFIT_DB[hazard][risk_level]
            for item in options:
                scored_actions.append((weight, item))
                
        scored_actions.sort(key=lambda x: x[0], reverse=True)
        top_5_actions = [item[1] for item in scored_actions[:5]]
        
        # Output strictly the Top 5 unique recommendations
        for rec in top_5_actions:
            st.markdown(f'<div class="rec-card">⚡ {rec}</div>', unsafe_allow_html=True)

    else:
        st.info("👈 Select a location from the dropdown above to view risk levels and recommended home fixes.")

st.divider()

# 10. Management Engineering Systems Context
with st.expander("📌 Technical Design & Management Engineering Principles"):
    st.markdown("""
    **The Inspiration:**
    I built ResilientReno to solve a common decision-making problem facing Canadian homeowners: understanding and acting on climate risk data. Seeing communities struggle with unpredictable weather damage made me curious about how engineering techniques could turn raw hazard statistics into actionable, location-specific advice.

    **Core Systems Engineering Design:**
    This project applies key principles of Management Engineering to organize data and streamline human choices:

    * **Decision-Support Systems:** Instead of requiring homeowners to analyze dense environmental reports, this engine uses dynamic filtering to generate immediate, structured recommendations tailored to exact location inputs.
    * **Resource Allocation Logic:** Budgeting for home renovations requires smart trade-offs. The system evaluates localized risk vectors to prioritize retrofits that deliver the highest risk-mitigation value first.
    * **Process Optimization:** By automating hazard mapping and task prioritization, the system reduces complexity and guides proactive decision-making before damage occurs.

    **Future Technical Enhancements:**
    I plan to refine the underlying data model by integrating GIS mapping tools (such as OpenStreetMap APIs) to factor in micro-location variables like soil elevation, flood plains, and canopy coverage.
    """)

st.markdown('<div class="footer-text">ResilientReno | Built by Elijah Lloyd</div>', unsafe_allow_html=True)
