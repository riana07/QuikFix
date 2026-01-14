import streamlit as st

def show_view():
    


    st.header("🧰 Services Available")
    st.markdown("""
    We offer fast, short-term contracting solutions for urgent or small jobs — completed same day or same week.
    Below are categories of services we offer:
    """)


    service_categories = [
        ("Plumbing", "🚰"),
        ("Flooring", "🪵"),
        ("Painting", "🎨"),
        ("Drywall", "🧱"),
        ("Roofing", "🏠"),
        ("Cleaning", "🧽"),
        ("Housekeeping", "🛏️"),
        ("Electrical Work", "💡"),
        ("House Moving", "📦"),
        ("Window Repair", "🪟"),
        ("Window Cleaning", "🧼"),
        ("Pressure Washing", "🚿"),
        ("Car Detailing", "🚗"),
        ("Car Washing", "🧴"),
        ("Repair Men", "🔧"),
        ("Roof Moss Removal", "🌿"),
        ("Landscaping", "🌳"),
        ("Lawn Mowing", "🌱"),
        ("Mulching", "🪵"),
    ]


    cols = st.columns(3)
    for i, (name, icon) in enumerate(service_categories):
        with cols[i % 3]:
            st.markdown(f"{icon} **{name}**")