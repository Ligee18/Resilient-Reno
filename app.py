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
    "A data-driven decision-support tool that maps regional natural hazard risks "
    "to prioritized, high-impact home retrofits based on postal code inputs."
)

st.divider()

# 3. Hazard Database (Forward Sortation Areas)
LOCATION_RISK_DB = {
    "L7R": {"city": "Burlington / Halton Region", "flood": "High", "wildfire": "Low", "wind": "High"},
    "N2L": {"city": "Waterloo / Kitchener Region", "flood": "High", "wildfire": "Low", "wind": "Medium"},
    "M5V": {"city": "Downtown Toronto", "flood": "Medium", "wildfire": "Low", "wind": "High"},
    "K1P": {"city": "Ottawa Region", "flood": "High", "wildfire": "Medium", "wind": "Medium"},
    "T2P": {"city": "Calgary Region", "flood": "Medium", "wildfire": "High", "wind": "Medium"},
    "V6B": {"city": "Vancouver Region", "flood": "High", "wildfire": "Low", "wind": "High"}
}

# 4. Actionable Retrofit Recommendation Database
RETROFIT_DB = {
    "flood": [
        "Install a sewer backwater valve on the main outflow line to prevent basement backflow.",
        "Equip the basement sump pump with an automatic, battery-powered backup system.",
        "Re-grade perimeter soil to slope away from foundation walls (minimum 5% gradient)."
    ],
    "wildfire": [
        "Create a 1.5-meter non-combustible defensible perimeter (gravel/stone) around exterior walls.",
        "Install 1/8-inch non-combustible metal mesh screens over all attic and soffit vents.",
        "Replace ground-level wood siding with non-flammable fiber-cement or masonry panels."
    ],
    "wind": [
        "Retrofit roof-to-wall connections with structural metal hurricane ties/clips.",
        "Reinforce double-car garage doors with vertical bracing shafts against wind-load pressures.",
        "Upgrade ground-floor and basement windows to impact-resistant laminated glass."
    ]
}

# 5. User Input Interface
st.subheader("1. Enter Location Information")
postal_input = st.text_input(
    "Enter Postal Code or Forward Sortation Area (e.g., L7R, N2L, M5V):"
).strip().upper()

# 6. Recommendation Logic & Output Processing
if postal_input:
    fsa = postal_input[:3]  # Extract first 3 characters
    
    if fsa in LOCATION_RISK_DB:
        location_data = LOCATION_RISK_DB[fsa]
        st.success(f"Location Found: **{location_data['city']} (`{fsa}`)**")
        
        st.subheader("2. Natural Hazard Risk Profile")
        col1, col2, col3 = st.columns(3)
        col1.metric("Flood Risk", location_data["flood"])
        col2.metric("Wildfire Risk", location_data["wildfire"])
        col3.metric("Wind / Storm Risk", location_data["wind"])
        
        st.divider()
        st.subheader("3. Top Prioritized Preventive Retrofits")
        
        # Collect recommendations for hazards evaluated as High or Medium
        recommendations = []
        for hazard in ["flood", "wildfire", "wind"]:
            if location_data[hazard] in ["High", "Medium"]:
                recommendations.extend(RETROFIT_DB[hazard])
        
        # Display top 5 actions
        for i, rec in enumerate(recommendations[:5], 1):
            st.markdown(f"**{i}.** {rec}")
            
    else:
        st.warning(
            f"FSA `{fsa}` is not in the current regional demonstration database. "
            "Please test using one of these postal code prefixes: **L7R, N2L, M5V, K1P, T2P, V6B**."
        )

st.divider()

# 7. Systems & Engineering Reflection (Waterloo AIF Context)
with st.expander("📌 Engineering Systems & Methodology Note (AIF Project Context)"):
    st.markdown("""
    **Core Objective:** Mitigate systemic municipal and home insurance losses by converting macro-level climate hazard datasets into personalized preventive action plans.
    
    **System Architecture:**
    1. **Data Layer:** Regional hazard profiles compiled from municipal open data and historical weather indices.
    2. **Logic Engine:** Rule-based decision routing prioritizing highest-risk environmental exposure.
    3. **Presentation Layer:** Lightweight web dashboard enabling actionable homeowner decision-making.
    
    **Limitations & Scope for Future Engineering Iterations:**
    * *Current Iteration:* Relies on aggregated Forward Sortation Area (FSA) regional hazard averages.
    * *Future Scope:* Integration of high-resolution satellite imagery (Sentinel/OpenStreetMap API) to evaluate micro-level properties, such as roof material type, exact elevation gradients, and proximity to forest boundary zones.
    """)

st.caption("ResilientReno | Built for Waterloo Management Engineering Application Portfolio")