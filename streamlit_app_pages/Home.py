import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("🏠 Welcome to QuikFix Contractor Services")
st.markdown("""
Need a job done fast, with no long-term contract? We’re your go-to for quick, premium contractor help:

✅ **Same-day or this-week service**  
🕐 **Small jobs welcome — even 1 hour**  
🔧 **Plumbing, Painting, Tiling, Flooring, Electrical**

""")

# Image
st.image("assets/workers.jpg", caption="QuikFix in Action", use_container_width=True)

# Services
st.markdown("## 🔨 Services Offered")
services = [
    "Plumbing", "Flooring", "Painting", "Drywall", "Roofing", "Cleaning", "Housekeeping", 
    "Electrical Work", "House Moving", "Window Repair", "Window Cleaning", "Pressure Washing",
    "Car Detailing", "Car Washing", "Repairmen", "Roof Moss Removal", "Landscaping", 
    "Lawn Mowing", "Mulch & Garden Prep"
]
st.markdown("\n".join([f"- {s}" for s in services]))

st.markdown("---")
st.markdown("💡 *Check out the Services page for detailed info or Submit an Inquiry to get started!*")