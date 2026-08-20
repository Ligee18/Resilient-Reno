import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ResilientReno | Home Resilience Engine",
    page_icon="🛡️",
    layout="centered"
)

# 2. Header & Slogan Setup
st.title("🛡️ ResilientReno")
st.caption("*\"An ounce of prevention is worth a pound of cure.\"*")
st.markdown(
    "A decision-support tool built to map regional natural hazard risks "
    "to prioritized home retrofits based on Canadian locations."
)

st.divider()

# 3. Canadian Regional Hazard Database (City + FSA)
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

# 4. Actionable Retrofit Recommendation Database
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

# 5. Interactive User Input (Dropdown)
st.subheader("1. Pick Your Area")
selected_location = st.selectbox(
    "Choose your city and postal code (FSA):",
    options=["-- Select City & Postal Code --"] + list(LOCATION_RISK_DB.keys())
)

# 6. Recommendation Logic & Output Display
if selected_location and selected_location != "-- Select City & Postal Code --":
    data = LOCATION_RISK_DB[selected_location]
    
    st.divider()
    st.subheader("2. Local Natural Hazard Profile")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Flood Risk", data["flood"])
    col2.metric("Wildfire Risk", data["wildfire"])
    col3.metric("Wind / Storm Risk", data["wind"])
    
    st.divider()
    st.subheader("3. Top 5 Recommended Home Improvements")
    
    # Priority logic: Filter risks flagged as High or Medium
    actions = []
    for hazard in ["flood", "wildfire", "wind"]:
        if data[hazard] in ["High", "Medium"]:
            actions.extend(RETROFIT_DB[hazard])
            
    # Output top 5 actions
    for i, rec in enumerate(actions[:5], 1):
        st.markdown(f"**{i}.** {rec}")

st.divider()

# 7. Waterloo AIF Systems & Engineering Context
with st.expander("📌 Project Context & Management Engineering Connection (AIF)"):
    st.markdown("""
    **Why I Built This:**
    I created ResilientReno to show how data-driven decision tools can help homeowners prevent major property damage before bad weather strikes. Instead of sorting through general advice, users get clear, location-specific actions based on local hazard risk levels.

    **How It Relates to Management Engineering at Waterloo:**
    * **Decision-Support Systems:** Translates regional risk data into a clean interface so users can make quick decisions without getting overwhelmed by raw data.
    * **Process Optimization:** Ranks retrofits by local risk priority so homeowners focus time and money on high-impact projects first.
    * **Future Upgrades:** In the future, I plan to use APIs like OpenStreetMap to pull property-level data (like roof type and elevation) for micro-targeted suggestions.
    """)

st.caption("ResilientReno | Built as a side project for Waterloo Management Engineering context")
