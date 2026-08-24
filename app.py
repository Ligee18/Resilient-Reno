import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ResilientReno",
    page_icon="🛡️",
    layout="wide"
)

# Minimal CSS to touch up dark mode contrast naturally
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. App Title & Intro
st.title("🛡️ ResilientReno")
st.caption("An ounce of prevention is worth a pound of cure.")

# Collapsible About Section
with st.expander("👋 About Me"):
    st.write("""
    Hi! I'm **Elijah Lloyd**, a Grade 12 student interested in software engineering and climate tech. 
    I built **ResilientReno** to help homeowners figure out the most effective ways to protect 
    their homes from extreme weather using local risk data.
    """)

# Purpose Box
with st.container():
    st.info("""
    **What is ResilientReno?**  
    Floods, wildfires, and windstorms are causing more home damage every year across Canada. 
    Most home upgrade advice online is generic. This tool looks at local climate hazards in your area 
    and gives you a prioritized checklist of fixes that actually make sense for your house.
    """)

# 3. Database Configurations
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
            "Install a Backwater Valve: Put a one-way sewer valve on your main line to block dirty storm sewer water from backing up into your basement.",
            "Add Sump Pump Battery Backup: Get a backup battery for your sump pump so it works even during power outages.",
            "Fix Your Soil Grading: Slope soil at least 5% away from your walls so rainwater drains toward the street instead of pooling around your foundation.",
            "Waterproof External Walls: Apply a rubberized asphalt membrane to exterior basement walls."
        ],
        "Medium": [
            "Extend Downspout Discharges: Run downspout extensions at least 6 feet away from your foundation.",
            "Seal Foundation Wall Cracks: Fill concrete basement cracks using hydraulic cement or polyurethane sealant.",
            "Window Well Covers: Add plastic covers over basement window wells to keep rain out."
        ],
        "Low": [
            "Elevate Basement Appliances: Raise laundry units and water heaters off the floor using concrete blocks.",
            "Install Sump Pump Smart Alarm: Put a Wi-Fi water sensor in your sump pit to alert your phone if it overflows.",
            "Install Permeable Driveway Pavers: Use porous pavers so rainwater can soak into the ground."
        ]
    },
    "wildfire": {
        "High": [
            "Build a Gravel Firebreak: Replace mulch within 1.5 meters of your walls with stone so embers cannot ignite siding.",
            "Put Mesh Over Vents: Cover attic and soffit vents with 1/8-inch metal mesh to stop blowing embers.",
            "Upgrade Ground Siding: Swap wood siding near the ground for fire-resistant fiber-cement boards.",
            "Install Class-A Rated Roofing: Use fire-resistant asphalt shingles or metal roofing."
        ],
        "Medium": [
            "Trim Tree Branches Near Roof: Keep tree limbs trimmed back 10 feet from rooflines and chimneys.",
            "Store Firewood Away From House: Move wood piles at least 30 feet away from exterior walls and decks.",
            "Enclose Deck Undersides: Shield the open space under decks using metal mesh or fire-resistant panels."
        ],
        "Low": [
            "Clear Gutter Debris Weekly: Keep roof gutters clear of dry leaves and pine needles.",
            "Upgrade Window Screen Material: Swap plastic window screens for aluminum or bronze mesh.",
            "Install Rooftop Sprinklers: Mount sprinklers to wet down your roof during nearby wildfire alerts."
        ]
    },
    "wind": {
        "High": [
            "Install Roof Hurricane Clips: Attach metal straps between roof trusses and walls to prevent roof uplift.",
            "Brace Your Garage Door: Install vertical bracing kits so high wind pressure doesn't pop garage doors off track.",
            "Upgrade Windows to Impact Glass: Use laminated glass on lower windows so flying debris won't shatter them.",
            "Reinforce Entry Door Locks: Add heavy-duty three-point deadbolts to keep exterior doors closed during severe storms."
        ],
        "Medium": [
            "Anchor Outdoor Sheds: Fasten sheds, pergolas, and heavy furniture into concrete footings.",
            "Install Storm Shutters: Mount exterior shutters over large glass windows.",
            "Reinforce Roof Sheathing Straps: Use ring-shank nails on roof plywood seams to better resist wind suction."
        ],
        "Low": [
            "Secure Loose Roof Flashing: Seal roof flashing around chimneys and vents with roof adhesive.",
            "Replace Dead Yard Trees: Remove rotting trees or branches that could fall during high wind gusts.",
            "Upgrade Vinyl Siding Fasteners: Secure siding panels with wide-head nails spaced every 12 inches."
        ]
    }
}

# 4. Step 1: Selection
st.subheader("Step 1: Choose Location")
selected_location = st.selectbox(
    "Select your area:",
    options=["-- Select City & Postal Code --"] + list(LOCATION_RISK_DB.keys()),
    label_visibility="collapsed"
)

# 5. Step 2 & 3 Output
if selected_location and selected_location != "-- Select City & Postal Code --":
    data = LOCATION_RISK_DB[selected_location]
    
    st.divider()
    st.subheader("Step 2: Risk Profile")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="🌊 Flood Risk", value=data["flood"])
    col2.metric(label="🔥 Wildfire Risk", value=data["wildfire"])
    col3.metric(label="💨 Wind Risk", value=data["wind"])
    
    st.divider()
    st.subheader("Step 3: Action Plan")
    st.caption("Recommended home fixes ranked by your local hazard levels.")
    
    # Priority sorting logic
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    scored_actions = []
    
    for hazard in ["flood", "wildfire", "wind"]:
        risk_level = data[hazard]
        weight = priority_map[risk_level]
        for item in TIERED_RETROFIT_DB[hazard][risk_level]:
            scored_actions.append((weight, hazard, item))
            
    scored_actions.sort(key=lambda x: x[0], reverse=True)
    top_5_actions = scored_actions[:5]
    
    # Render Action Cards using native Streamlit containers
    for weight, hazard_type, text in top_5_actions:
        with st.container(border=True):
            if ":" in text:
                title, desc = text.split(":", 1)
            else:
                title, desc = "Fix Recommendation", text
            
            c1, c2 = st.columns([0.8, 0.2])
            with c1:
                st.markdown(f"**⚡ {title.strip()}**")
                st.write(desc.strip())
            with c2:
                if weight == 3:
                    st.error("HIGH PRIORITY")
                elif weight == 2:
                    st.warning("MEDIUM")
                else:
                    st.success("LOW")

else:
    st.info("Select a city above to see your risk profile and action plan.")

st.divider()

# 6. Technical Explanation
st.subheader("How It Works")

e1, e2, e3 = st.columns(3)
with e1:
    with st.container(border=True):
        st.markdown("**1. Data Mapping**")
        st.write("Matches postal code regions with local environmental risk scores.")

with e2:
    with st.container(border=True):
        st.markdown("**2. Priority Scoring**")
        st.write("Ranks home improvements based on which local hazards are most severe.")

with e3:
    with st.container(border=True):
        st.markdown("**3. Action Output**")
        st.write("Filters down to the top 5 highest-impact fixes for the homeowner.")

# Roadmap Section
st.markdown("#### Future Improvements")
st.write("- **Phase 1:** Add terrain and elevation data to improve local flood calculations.")
st.write("- **Phase 2:** Integrate live weather alerts and seasonal risk updates.")
st.write("- **Phase 3:** Include cost estimates and local contractor recommendations.")

st.caption("Built by Elijah Lloyd")
