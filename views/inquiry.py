import streamlit as st

def show_view():


    st.header("✉️ Submit an Inquiry")
    st.markdown("""
    Looking for fast help? Fill out the form below and our team will get in touch with you within a few hours.
    """)


    with st.form("inquiry_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        location = st.text_input("Job Location (City/Neighborhood)")
        category = st.selectbox("Type of Work", [
            "Plumbing", "Flooring", "Painting", "Drywall", "Roofing", "Cleaning",
            "Housekeeping", "Electrical Work", "House Moving", "Window Repair",
            "Window Cleaning", "Pressure Washing", "Car Detailing", "Car Washing",
            "Repair Men", "Roof Moss Removal", "Landscaping", "Lawn Mowing", "Mulching"
        ])
        urgency = st.selectbox("Urgency", ["ASAP (Today/Tomorrow)", "This Week", "Flexible Schedule"])
        description = st.text_area("Job Description")


        submitted = st.form_submit_button("Submit Inquiry")
        if submitted:
            st.success("✅ Inquiry submitted successfully! We’ll follow up shortly.")
# Add email/DB/store logic here later