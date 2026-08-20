import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ResilientReno | Home Resilience Engine",
    page_icon="🛡️",
    layout="centered"
)

# 2. Header & Slogan
st.title("🛡️ ResilientReno")
st.caption("*\"An ounce of prevention is worth a pound of cure.\"*")
st.markdown(
    "Select your region to analyze localized natural hazard exposure "
    "and generate prioritized, climate-resilient home retrofits."
)

st.divider()

# 3. Expanded Regional Hazard Database (City + FSA)
LOCATION_RISK_DB = {
    "Burlington / Halton Region (L7R)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Waterloo / Kitchener (N2L)": {"flood": "High", "wildfire": "Low", "wind": "Medium"},
    "Toronto - Downtown Core (M5V)": {"flood": "Medium", "wildfire": "Low", "wind": "High"},
    "Toronto - North York (M2N)": {"flood": "Medium", "wildfire": "Low", "wind": "Medium"},
    "Mississauga / Peel Region (L5B)": {"flood": "High", "wildfire": "Low", "wind": "Medium"},
    "Hamilton / Mountain Area (L8P)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Ottawa / Capital Region (K1P)": {"flood": "High", "wildfire": "Medium", "wind": "Medium"},
    "London / Middlesex (N6A)": {"flood": "Medium", "wildfire": "Low", "wind": "High"},
    "Windsor / Essex (N9A)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Barrie / Simcoe County (L4M)": {"flood": "Medium", "wildfire": "Medium", "wind": "High"},
    "Calgary - Central (T2P)": {"flood": "Medium", "wildfire": "High", "wind": "Medium"},
    "Edmonton - Downtown (T5J)": {"flood": "Medium", "wildfire": "High", "wind": "Medium"},
    "Vancouver - Downtown (V6B)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Surrey / Fraser Valley (V3T)": {"flood": "High", "wildfire": "Medium", "wind": "Medium"},
    "Kelowna / Okanagan (V1Y)": {"flood": "Low", "wildfire": "High", "wind": "Medium"},
    "Victoria / Vancouver Island (V8W)": {"flood": "High", "wildfire": "Medium", "wind": "High"},
    "Halifax / Regional Municipality (B3J)": {"flood": "High", "wildfire": "Low", "wind": "High"},
    "Winnipeg / Red River Valley (R3C)": {"flood": "High", "wildfire": "Medium", "wind": "Medium"},
    "Montreal - Centre-Ville (H3B)": {"flood": "Medium", "wildfire": "Low", "wind": "Medium"},
    "Quebec City / Capital Area (G1R)": {"flood": "High", "wildfire": "Low", "wind": "Medium"},
}

# 4. Actionable Retrofit Recommendation Database
RETROFIT_DB = {
    "flood": [
        "Install a mainline sewer backwater valve to prevent storm basement backflow.",
        "Equip basement sump pumps with automatic battery-powered auxiliary backups.",
        "Re-grade perimeter soil to ensure minimum 5% outward slope from foundation walls."
    ],
    "wildfire": [
        "Establish a 1.5-meter non-combustible defensible perimeter (gravel/stone) around exterior walls.",
        "Install 1/8-inch non-combustible metal mesh screens over attic and soffit vents.",
        "Replace wood siding with non-flammable fiber-cement or masonry panels."
    ],
    "wind": [
        "Install structural roof-to-wall hurricane clips/ties to prevent wind uplift.",
        "Reinforce double-car garage doors with vertical bracing shafts against peak pressures.",
        "Upgrade ground-floor and basement windows to impact-resistant laminated glass."
    ]
}

# 5. Dropdown Selection Interface
st.subheader("1. Select Your Region")
selected_location = st.selectbox(
    "Choose your city and Forward Sortation Area (FSA):",
    options=["-- Select a City & Postal Code --"] + list(LOCATION_RISK_DB.keys())
)

# 6. Interactive Results Output
if selected_location and selected_location != "-- Select a City & Postal Code --":
    data = LOCATION_RISK_DB[selected_location]
    
    st.divider()
    st.subheader("2. Regional Hazard Risk Profile")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Flood Risk", data["flood"])
    col2.metric("Wildfire Risk", data["wildfire"])
    col3.metric("Wind / Storm Risk", data["wind"])
    
    st.divider()
    st.subheader("3. Recommended Priority Retrofits")
    
    # Prioritize hazards evaluated as High or Medium
    actions = []
    for hazard in ["flood", "wildfire", "wind"]:
        if data[hazard] in ["High", "Medium"]:
            actions.extend(RETROFIT_DB[hazard])
            
    for idx, item in enumerate(actions[:5], 1):
        st.markdown(f"**{idx}.** {item}")

st.divider()

# 7. Waterloo AIF Systems Note
with st.expander("📌 Engineering Systems & Methodology Note (AIF Application Context)"):
    st.markdown("""
    **Core Objective:** Mitigate residential property damage losses by translating regional climate risk datasets into prioritized home improvement actions.
    
    **System Architecture:**
    1. **Data Layer:** Regional hazard profiles compiled across major Canadian municipal Forward Sortation Areas (FSAs).
    2. **Logic Routing:** Risk-weighted matching engine identifying critical failure points (flood backflow, ember intrusion, wind uplift).
    3. **Presentation Layer:** User-centered dashboard enabling immediate, high-impact decision-making.
    """)

st.caption("ResilientReno | Built for Waterloo Management Engineering Portfolio")
