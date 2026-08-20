import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ResilientReno | Home Resilience Engine",
    page_icon="🛡️",
    layout="centered"
)

# 2. Custom CSS & High-Contrast Visual Enhancement
st.markdown("""
    <style>
    /* Full Dark Background Contrast Fix */
    .stAppViewContainer, .stApp {
        background-color: #090d16 !important;
        color: #ffffff !important;
    }
    
    /* Global Typography Force White/Light */
    h1, h2, h3, h4, h5, h6, p, label, span, div, li {
        color: #f8fafc !important;
    }
    
    /* Header Container */
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 28px;
        border-radius: 14px;
        color: #ffffff !important;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
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
        color: #f59e0b !important;
        font-size: 1.05rem;
        font-weight: 500;
    }
    
    /* About Me Box */
    .about-me-box {
        background-color: #0f172a;
        border: 1px solid #38bdf8;
        padding: 18px 22px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #f8fafc !important;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    .about-me-box strong {
        color: #38bdf8 !important;
    }

    /* Intro Banner Box */
    .info-banner {
        background-color: #1e293b;
        border-left: 4px solid #38bdf8;
        padding: 16px 20px;
        border-radius: 10px;
        margin-bottom: 24px;
        color: #ffffff !important;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* Modern Retrofit Cards */
    .rec-card {
        background-color: #0f172a;
        border: 1px solid #334155;
        border-left: 5px solid #38bdf8;
        padding: 18px 22px;
        border-radius: 10px;
        font-size: 0.95rem;
        color: #ffffff !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        height: 100%;
        display: flex;
        align-items: center;
    }
    .rec-card strong {
        color: #38bdf8 !important;
    }

    /* Risk Badges */
    .badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.9rem;
        text-align: center;
        margin-top: 4px;
    }
    .badge-high {
        background-color: rgba(239, 68, 68, 0.25);
        color: #fca5a5 !important;
        border: 1px solid #ef4444;
    }
    .badge-medium {
        background-color: rgba(245, 158, 11, 0.25);
        color: #fde047 !important;
        border: 1px solid #f59e0b;
    }
    .badge-low {
        background-color: rgba(16, 185, 129, 0.25);
        color: #6ee7b7 !important;
        border: 1px solid #10b981;
    }

    /* Expander & Footer Text Contrast Fixes */
    .stExpander {
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }
    .stExpander p, .stExpander span, .stExpander li, .stExpander div {
        color: #ffffff !important;
    }
    .stExpander strong {
        color: #38bdf8 !important;
    }
    .footer-text {
        color: #ffffff !important;
        font-size: 0.85rem;
        text-align: center;
        margin-top: 15px;
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

# 4. About Me Section
st.markdown("""
    <div class="about-me-box">
        👋 <strong>About Me:</strong><br>
        Hi! My name is <strong>Elijah Lloyd</strong>. I'm a Grade 12 student with a passion for software development, data analytics, and engineering problem-solving. I built <strong>ResilientReno</strong> as an independent engineering portfolio project for my University of Waterloo Management Engineering application. My goal was to explore how decision-support software can take big, complicated datasets and turn them into simple, helpful tools for everyday people.
    </div>
""", unsafe_allow_html=True)

# 5. Top Intro Section
st.markdown("""
    <div class="info-banner">
        <strong>💡 What is ResilientReno & Why Does It Matter?</strong><br>
        Extreme weather like severe basement flooding, high windstorms, and wildfire smoke is hitting Canadian homes more often, causing thousands of dollars in unexpected damage. Most home improvement advice online is way too broad. <strong>ResilientReno</strong> takes local weather hazard data across Canadian towns and turns it into a targeted, practical home protection plan so you can spend your budget on repairs that actually matter for your area.
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

# 7. Retrofit Database Paired with Specific Correlated Images
TIERED_RETROFIT_DB = {
    "flood": {
        "High": [
            {
                "text": "<strong>Install a Backwater Valve:</strong> Put a one-way sewer valve on your main line so dirty storm sewer water can't back up into your basement drain during heavy rainstorms.",
                "img": "https://images.unsplash.com/photo-1585704032915-c3400ca199e7?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Add Sump Pump Battery Backup:</strong> Get a secondary battery pack for your sump pump so it keeps pushing water away from your foundation even if power goes out.",
                "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Fix Your Soil Grading:</strong> Make sure the dirt and gardens around your house slope downward at least 5% away from your walls so rainwater flows toward the street instead of pooling around your basement.",
                "img": "https://images.unsplash.com/photo-1592417817098-8f3d6ef23a81?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Waterproof External Walls:</strong> Apply a rubberized asphalt membrane to exterior foundation walls below ground level.",
                "img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=300&q=80"
            }
        ],
        "Medium": [
            {
                "text": "<strong>Extend Downspout Discharges:</strong> Add extension pipes so downspouts dump rainwater at least 6 feet away from your foundation wall.",
                "img": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Seal Foundation Wall Cracks:</strong> Fill concrete basement wall cracks using hydraulic cement or high-grade polyurethane sealant to block ground leaks.",
                "img": "https://images.unsplash.com/photo-1581094288338-2314dddb7ece?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Window Well Covers:</strong> Fit clear polycarbonate domes over basement window wells to stop water accumulation from pouring in.",
                "img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=300&q=80"
            }
        ],
        "Low": [
            {
                "text": "<strong>Elevate Basement Appliances:</strong> Mount laundry units, water heaters, and furnaces on 6-inch concrete pedestals off the floor.",
                "img": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Install Sump Pump Smart Alarm:</strong> Add a Wi-Fi water sensor inside your sump basin to alert your smartphone before a pump fails.",
                "img": "https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Install Permeable Driveway Pavers:</strong> Replace solid concrete walkways with porous pavers so rainwater drains naturally into ground soil.",
                "img": "https://images.unsplash.com/photo-1590381105924-c72589b9ef3f?auto=format&fit=crop&w=300&q=80"
            }
        ]
    },
    "wildfire": {
        "High": [
            {
                "text": "<strong>Build a Gravel Firebreak:</strong> Swap out wood mulch or grass within 1.5 meters of your exterior walls for gravel or river rocks so floating embers can't ignite your siding.",
                "img": "https://images.unsplash.com/photo-1508873696983-2df515122519?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Put Mesh Over Vents:</strong> Cover your attic and soffit vents with 1/8-inch metal mesh screens to block blowing embers from getting into your roof structure.",
                "img": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Upgrade Ground Siding:</strong> Replace old wood siding near ground level with non-flammable fiber-cement boards or brick panels.",
                "img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Install Class-A Rated Roofing:</strong> Choose asphalt shingles or metal roofing systems certified with the highest fire-resistance rating.",
                "img": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=300&q=80"
            }
        ],
        "Medium": [
            {
                "text": "<strong>Trim Tree Branches Near Roof:</strong> Prune overhead tree branches so they stay at least 10 feet away from your rooflines and chimneys.",
                "img": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Store Firewood Away From House:</strong> Move wood piles at least 30 feet away from exterior walls and wooden decks.",
                "img": "https://images.unsplash.com/photo-1520114878144-6123749968dd?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Enclose Open Deck Undersides:</strong> Wrap open space beneath elevated wooden decks using metal mesh or fire-resistant board panels.",
                "img": "https://images.unsplash.com/photo-1591825729269-caeb344f6df2?auto=format&fit=crop&w=300&q=80"
            }
        ],
        "Low": [
            {
                "text": "<strong>Clear Gutter Debris Weekly:</strong> Remove dried pine needles and leaves from roof gutters where embers easily spark fires.",
                "img": "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Upgrade Window Screen Material:</strong> Swap plastic window mesh for flame-resistant bronze or aluminum mesh screens.",
                "img": "https://images.unsplash.com/photo-1509644851169-2acc08aa15b6?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Install External Rooftop Sprinklers:</strong> Mount roof-line water misters to soak shingles and surrounding soil during nearby wildfire warnings.",
                "img": "https://images.unsplash.com/photo-1585704032915-c3400ca199e7?auto=format&fit=crop&w=300&q=80"
            }
        ]
    },
    "wind": {
        "High": [
            {
                "text": "<strong>Install Roof Hurricane Clips:</strong> Secure roof trusses directly to your wall frames using metal hurricane straps to prevent strong roof uplift in high-wind storms.",
                "img": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Brace Your Garage Door:</strong> Add vertical metal bracing kits to your garage door to keep strong wind pressure from popping it off the tracks.",
                "img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Upgrade Windows to Impact Glass:</strong> Swap out basement and main-floor glass for laminated impact-resistant glass that won't shatter when hit by flying debris.",
                "img": "https://images.unsplash.com/photo-1509644851169-2acc08aa15b6?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Reinforce Entry Door Locks:</strong> Add heavy-duty three-point deadbolt locks to keep exterior doors from blowing open in severe pressure shifts.",
                "img": "https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=300&q=80"
            }
        ],
        "Medium": [
            {
                "text": "<strong>Anchor Outdoor Sheds & Structures:</strong> Secure yard sheds, pergolas, and heavy furniture into concrete footings with steel tie-down straps.",
                "img": "https://images.unsplash.com/photo-1591825729269-caeb344f6df2?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Install Storm Shutters:</strong> Mount exterior aluminum or steel shutters that fold closed over glass windows during storm alerts.",
                "img": "https://images.unsplash.com/photo-1509644851169-2acc08aa15b6?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Reinforce Roof Sheathing Straps:</strong> Add ring-shank nails along roof plywood deck seams to double resistance against wind suction.",
                "img": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=300&q=80"
            }
        ],
        "Low": [
            {
                "text": "<strong>Secure Loose Roof Flashing:</strong> Seal all edge flashing around chimneys, skylights, and vents with heavy-duty roof adhesive sealant.",
                "img": "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Replace Dead Yard Trees:</strong> Remove rotting trees or compromised branches that could collapse onto your house during high-wind gusts.",
                "img": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=300&q=80"
            },
            {
                "text": "<strong>Upgrade Vinyl Siding Fasteners:</strong> Fasten exterior wall siding panels with wide-head galvanized nails spaced every 12 inches.",
                "img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=300&q=80"
            }
        ]
    }
}

# Helper function to generate risk badge HTML
def get_badge_html(label, level):
    css_class = f"badge-{level.lower()}"
    return f"""
    <div style="text-align: center;">
        <span style="color: #ffffff; font-size: 0.85rem;">{label}</span><br>
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
        
        # Display Top 5 Recommendations with paired mini images side-by-side
        for rec in top_5_actions:
            text_col, img_col = st.columns([3, 1])
            with text_col:
                st.markdown(f'<div class="rec-card">⚡ {rec["text"]}</div>', unsafe_allow_html=True)
            with img_col:
                st.image(rec["img"], use_column_width=True)
            st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

    else:
        st.info("👈 Select a location from the dropdown above to view risk levels and recommended home fixes.")

st.divider()

# 10. Waterloo Management Engineering Specific Context
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

st.markdown('<div class="footer-text">ResilientReno | Built by Elijah Lloyd for Waterloo Management Engineering Context</div>', unsafe_allow_html=True)
