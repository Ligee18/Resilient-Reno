import streamlit as st

# 1. Page Configuration (Centered Grid Layout)
st.set_page_config(
    page_title="ResilientReno | Climate Risk Decision Engine",
    page_icon="🛡️",
    layout="wide"
)

# 2. Premium SaaS Theme Custom CSS (Linear / Vercel Dark Aesthetics)
st.markdown("""
    <style>
    /* Dark Theme Base */
    .stAppViewContainer, .stApp {
        background-color: #090d16 !important;
        color: #f8fafc !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Restrain Max-Width for Optimal Visual Balance & Line Length */
    .main .block-container {
        max-width: 1040px !important;
        padding-top: 3rem !important;
        padding-bottom: 5rem !important;
        margin: 0 auto !important;
    }
    
    /* Typography Overrides & Contrast Hierarchy */
    h1, h2, h3, h4, h5, h6, p, label, span, div, li {
        color: #f8fafc !important;
    }

    /* Input Select Box Styling */
    div[data-baseweb="select"] > div {
        background-color: #111827 !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }
    div[data-baseweb="select"] * {
        color: #f8fafc !important;
    }

    /* Popover Dropdown Container Background */
    [data-baseweb="popover"],
    [data-baseweb="popover"] > div,
    div[role="listbox"] {
        background-color: #111827 !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
    }

    /* Dropdown Menu Text & Hover States */
    div[role="listbox"] li,
    div[role="listbox"] li *,
    ul[data-baseweb="menu"] li,
    ul[data-baseweb="menu"] li * {
        color: #cbd5e1 !important;
        background-color: transparent !important;
    }
    div[role="listbox"] li:hover,
    div[role="listbox"] li:hover * {
        background-color: #1f2937 !important;
        color: #38bdf8 !important;
    }

    /* Refined Hero Banner */
    .hero-card {
        background: linear-gradient(180deg, #111827 0%, #0d1322 100%);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 16px;
        padding: 36px 40px;
        margin-bottom: 32px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #f8fafc !important;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        color: #94a3b8 !important;
        font-size: 1rem;
        font-style: italic;
    }

    /* Info Card */
    .info-card {
        background-color: #111827;
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-left: 3px solid #38bdf8;
        border-radius: 12px;
        padding: 24px 28px;
        margin-bottom: 36px;
        line-height: 1.6;
        color: #94a3b8 !important;
        font-size: 0.95rem;
    }
    .info-card strong {
        color: #f8fafc !important;
    }

    /* Expanders Clean Styling */
    .stExpander {
        background-color: #111827 !important;
        border: 1px solid rgba(255, 255, 255, 0.07) !important;
        border-radius: 12px !important;
        margin-bottom: 24px !important;
    }
    .stExpander summary {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
    }

    /* Minimalist Risk Badges */
    .badge-card {
        background: #111827;
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    .badge-label {
        color: #94a3b8 !important;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-pill {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
    }
    .badge-high {
        background-color: rgba(239, 68, 68, 0.12);
        color: #fca5a5 !important;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    .badge-medium {
        background-color: rgba(245, 158, 11, 0.12);
        color: #fde047 !important;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }
    .badge-low {
        background-color: rgba(16, 185, 129, 0.12);
        color: #6ee7b7 !important;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }

    /* Enhanced Recommendation Cards with Hover States */
    .rec-card {
        background-color: #111827;
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 12px;
        padding: 22px 26px;
        margin-bottom: 16px;
        transition: transform 0.15s ease, border-color 0.15s ease, background-color 0.15s ease;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    .rec-card:hover {
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.4);
        background-color: #131d31;
    }
    .rec-header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }
    .rec-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #f8fafc !important;
        letter-spacing: -0.2px;
    }
    .rec-desc {
        color: #94a3b8 !important;
        font-size: 0.92rem;
        line-height: 1.5;
    }
    .hazard-tag {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 3px 10px;
        border-radius: 6px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: #1a2333;
        color: #38bdf8 !important;
    }

    /* Summary Bar */
    .summary-bar {
        display: flex;
        gap: 12px;
        margin-bottom: 20px;
        font-size: 0.85rem;
        color: #94a3b8;
    }
    .summary-pill {
        background: #111827;
        border: 1px solid rgba(255, 255, 255, 0.06);
        padding: 4px 12px;
        border-radius: 8px;
        font-weight: 500;
    }

    /* Engineering Feature Cards */
    .eng-card {
        background-color: #111827;
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 12px;
        padding: 24px;
        height: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .eng-number {
        font-size: 0.8rem;
        font-weight: 700;
        color: #38bdf8;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }
    .eng-title {
        font-size: 1rem;
        font-weight: 700;
        color: #f8fafc !important;
        margin-bottom: 8px;
    }
    .eng-desc {
        font-size: 0.88rem;
        color: #94a3b8 !important;
        line-height: 1.5;
    }

    /* Roadmap Timeline */
    .roadmap-container {
        background-color: #111827;
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 12px;
        padding: 24px 28px;
        margin-top: 20px;
    }
    .roadmap-step {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 10px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.04);
    }
    .roadmap-step:last-child {
        border-bottom: none;
    }
    .roadmap-bullet {
        width: 8px;
        height: 8px;
        background-color: #38bdf8;
        border-radius: 50%;
        box-shadow: 0 0 8px rgba(56, 189, 248, 0.5);
    }
    .roadmap-text {
        font-size: 0.9rem;
        color: #cbd5e1;
        font-weight: 500;
    }

    .footer-text {
        color: #64748b !important;
        font-size: 0.85rem;
        text-align: center;
        margin-top: 48px;
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
        <strong style="color: #f8fafc;">💡 What is ResilientReno & Why Does It Matter?</strong><br>
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
st.markdown("<p style='font-size: 0.85rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px;'>Step 1</p>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 1.25rem; font-weight: 700; margin-bottom: 12px;'>Select Location</h3>", unsafe_allow_html=True)
selected_location = st.selectbox(
    "Choose your city and area postal code:",
    options=["-- Select City & Postal Code --"] + list(LOCATION_RISK_DB.keys()),
    key="location_selector",
    label_visibility="collapsed"
)

# 8. Dynamic Step 2 & 3 Output
if selected_location and selected_location != "-- Select City & Postal Code --":
    data = LOCATION_RISK_DB[selected_location]
    
    st.markdown("<div style='margin-top: 36px;'></div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.85rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px;'>Step 2</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 1.25rem; font-weight: 700; margin-bottom: 16px;'>Local Weather Risk Profile</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(render_badge("Flood Exposure", data["flood"]), unsafe_allow_html=True)
    with col2:
        st.markdown(render_badge("Wildfire Exposure", data["wildfire"]), unsafe_allow_html=True)
    with col3:
        st.markdown(render_badge("Wind Hazard", data["wind"]), unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 36px;'></div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.85rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px;'>Step 3</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 1.25rem; font-weight: 700; margin-bottom: 4px;'>Priority Action Plan</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; font-size: 0.9rem; margin-bottom: 16px;'>Recommended improvements ranked by your property's local climate-risk profile.</p>", unsafe_allow_html=True)
    
    # Logic for weighted priority scoring & structured parsing
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    scored_actions = []
    
    for hazard in ["flood", "wildfire", "wind"]:
        risk_level = data[hazard]
        weight = priority_map[risk_level]
        for item in TIERED_RETROFIT_DB[hazard][risk_level]:
            scored_actions.append((weight, hazard, item))
            
    scored_actions.sort(key=lambda x: x[0], reverse=True)
    top_5_actions = scored_actions[:5]
    
    # Recommendation Summary Bar
    high_count = sum(1 for w, h, i in top_5_actions if w == 3)
    flood_count = sum(1 for w, h, i in top_5_actions if h == "flood")
    wind_count = sum(1 for w, h, i in top_5_actions if h == "wind")
    wildfire_count = sum(1 for w, h, i in top_5_actions if h == "wildfire")
    
    st.markdown(f"""
        <div class="summary-bar">
            <div class="summary-pill">⚡ 5 recommended actions</div>
            <div class="summary-pill">{high_count} high priority</div>
            <div class="summary-pill">{max(flood_count, wind_count, wildfire_count)} primary hazard category</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Render structured recommendation cards
    for weight, hazard_type, rec in top_5_actions:
        # Split title and description from the stored string format "<strong>Title:</strong> Description"
        clean_rec = rec.replace("<strong>", "").replace("</strong>", "")
        if ":" in clean_rec:
            parts = clean_rec.split(":", 1)
            title = parts[0].strip()
            desc = parts[1].strip()
        else:
            title = "Property Defense Action"
            desc = clean_rec
            
        badge_label = f"{hazard_type.upper()} PROTECTION"
        
        st.markdown(f"""
            <div class="rec-card">
                <div class="rec-header-row">
                    <span class="rec-title">⚡ {title}</span>
                    <span class="hazard-tag">{badge_label}</span>
                </div>
                <div class="rec-desc">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
    st.info("👈 Select a location from the dropdown above to view risk levels and recommended home fixes.")

st.markdown("<div style='margin-top: 48px;'></div>", unsafe_allow_html=True)

# 9. Redesigned Engineering Overview & Architecture Section
st.markdown("<p style='font-size: 0.85rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px;'>Engineering Overview</p>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 1.35rem; font-weight: 700; margin-bottom: 6px;'>How ResilientReno Works</h3>", unsafe_allow_html=True)
st.markdown("<p style='color: #94a3b8; font-size: 0.92rem; margin-bottom: 24px;'>Turning regional climate data into property-level decisions.</p>", unsafe_allow_html=True)

eng_col1, eng_col2, eng_col3 = st.columns(3)

with eng_col1:
    st.markdown("""
        <div class="eng-card">
            <div class="eng-number">01 — Decision Support</div>
            <div class="eng-title">Multi-Variable Analysis</div>
            <div class="eng-desc">Converts complex climate-risk datasets into clear, localized recommendations without manual research friction.</div>
        </div>
    """, unsafe_allow_html=True)

with eng_col2:
    st.markdown("""
        <div class="eng-card">
            <div class="eng-number">02 — Priority Engine</div>
            <div class="eng-title">Severity Weighting</div>
            <div class="eng-desc">Ranks mitigation strategies dynamically according to local hazard severity tiers and maximum risk mitigation value.</div>
        </div>
    """, unsafe_allow_html=True)

with eng_col3:
    st.markdown("""
        <div class="eng-card">
            <div class="eng-number">03 — Streamlining</div>
            <div class="eng-title">Actionable Outputs</div>
            <div class="eng-desc">Filters dense environmental reports down to the top high-impact interventions tailored for home capital allocation.</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-top: 32px;'></div>", unsafe_allow_html=True)
st.markdown("<h4 style='font-size: 1.05rem; font-weight: 700; margin-bottom: 12px;'>Technical Roadmap & Future Scale</h4>", unsafe_allow_html=True)

st.markdown("""
    <div class="roadmap-container">
        <div class="roadmap-step">
            <div class="roadmap-bullet"></div>
            <div class="roadmap-text"><b>Phase 1:</b> Integration of OpenStreetMap & terrain elevation datasets for micro-location topography mapping.</div>
        </div>
        <div class="roadmap-step">
            <div class="roadmap-bullet"></div>
            <div class="roadmap-text"><b>Phase 2:</b> Watershed proximity and local hydrological flow-path calculations for basement flood modeling.</div>
        </div>
        <div class="roadmap-step">
            <div class="roadmap-bullet"></div>
            <div class="roadmap-text"><b>Phase 3:</b> Vegetation density and canopy coverage metrics for localized wildfire ember exposure indexing.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer-text">ResilientReno | Built by Elijah Lloyd</div>', unsafe_allow_html=True)
