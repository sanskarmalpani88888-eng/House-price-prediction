import streamlit as st
import random

# 1. Hierarchical Location Data
LOCATION_DATA = {
    "Karnataka": {
        "Bangalore Urban": {
            "Bangalore City": ["Whitefield", "Electronic City", "Indiranagar", "Koramanagala"],
            "Yelahanka": ["Allalasandra", "Chikkajala", "Bagaluru"]
        },
        "Bangalore Rural": {
            "Devanahalli": ["Vijayapura", "Budigere", "Channarayapatna"],
            "Nelamangala": ["Tyamagondlu", "Sondekoppa"]
        }
    },
    "Maharashtra": {
        "Pune": {
            "Pune City": ["Kothrud", "Shivajinagar", "Viman Nagar", "Kalyani Nagar"],
            "Haveli": ["Wagholi", "Hinjawadi", "Hadapsar", "Dhanori"],
            "Maval": ["Lonavala", "Talegaon", "Kanhe"]
        },
        "Mumbai Suburban": {
            "Andheri": ["Versova", "Lokhandwala", "Marol"],
            "Borivali": ["Gorai", "Dahisar", "Magathane"],
            "Kurla": ["Ghatkopar", "Chembur", "Sakinaka"]
        },
        "Nagpur": {
            "Nagpur Urban": ["Sitabuldi", "Dharampeth", "Sadat", "Wardhaman Nagar"],
            "Nagpur Rural": ["Wadi", "Kanhan", "Kamptee", "Hingna"]
        }
    }
}

# 2. Web App UI Configuration
st.set_page_config(page_title="IndiHomes Predictor", page_icon="🏠", layout="centered")

st.title("🏠 Indian House Price Prediction Portal")
st.write("Enter the property details below to estimate the market value.")

st.divider()

# 3. Dynamic Dropdown Selectors
st.subheader("📍 Location Details")

# State Selection
state = st.selectbox("Select State", list(LOCATION_DATA.keys()))

# District Selection (updates based on State)
districts = LOCATION_DATA[state]
district = st.selectbox("Select District", list(districts.keys()))

# City/Taluka Selection (updates based on District)
cities = districts[district]
city = st.selectbox("Select City/Taluka", list(cities.keys()))

# Village/Area Selection (updates based on City)
villages = cities[city]
village = st.selectbox("Select Village/Neighborhood Area", villages)

st.divider()

# 4. Property Features Input
st.subheader("📐 Property Specifications")
col1, col2 = st.columns(2)

with col1:
    bhk = st.slider("Number of BHK", min_value=1, max_value=5, value=2, step=1)
    sqft = st.number_input("Total Area (Square Feet)", min_value=300, max_value=10000, value=1200, step=50)

with col2:
    bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4, 5], index=1)
    status = st.radio("Construction Status", ["Ready to Move", "Under Construction"])

st.divider()

# 5. Prediction Logic
if st.button("🔮 Calculate Estimated Price", type="primary"):
    with st.spinner("Analyzing local market trends..."):
        # Placeholder pricing logic (Replace this with your actual ML model prediction loading)
        # e.g., price = model.predict([[sqft, bhk, bathrooms]])
        
        base_rate = 4500  # Base rate per sqft
        
        # Give specific weightage boosts to premium areas
        if village in ["Indiranagar", "Kalyani Nagar", "Lokhandwala"]:
            base_rate += 3500
        elif state == "Maharashtra" and "Mumbai" in district:
            base_rate += 5000
            
        estimated_price = sqft * base_rate
        
        # Format price beautifully into Lakhs or Crores
        if estimated_price >= 10000000:
            formatted_price = f"₹{estimated_price / 10000000:.2f} Crores"
        else:
            formatted_price = f"₹{estimated_price / 100000:.2f} Lakhs"
            
        st.success(f"### Estimated Market Value: {formatted_price}")
        st.balloons()
        
        st.info(f"**Property Summary:** A {status} {bhk} BHK apartment spanning {sqft} sq.ft. located in {village}, {city}, {district} ({state}).")
