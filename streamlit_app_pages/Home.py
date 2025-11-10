def main():
    st.write("This is the Home page.")
    
    # Sidebar TOC
    with st.sidebar:
        st.header("🧭 Navigation")
        st.markdown("""
        - [🏠 Home](#home)
        - [🛠️ Services](#services)
        - [📬 Inquiry](#inquiry)
        - [🛡️ Admin](#admin)
        - [❓ Q&A](#q-a)
        - [⭐ Reviews](#reviews)
        """, unsafe_allow_html=True)

    st.set_page_config(page_title="Home", page_icon="🏠")

    st.title("🏠 Welcome to QuickFix Contractor Services")
    st.markdown("""
    Need a job done fast, with no long-term contract? **We’re your go-to** for quick, same-week service.
    
    🔧 Small jobs welcome – even 1-hour tasks!
    """)

    # Services
    st.markdown("## 🛠️ Services Offered")
    services = [
        "Plumbing", "Flooring", "Painting", "Drywall", "Roofing", "Cleaning",
        "Electrical Work", "House Moving", "Window Repair", "Window Cleaning",
        "Car Detailing", "Car Washing", "Repairmen", "Roof Moss Removal",
        "Landscaping", "Lawn Mowing", "Mulch & Garden Prep"
    ]
    st.markdown("\n".join([f"- {s}" for s in services]))
    st.markdown("---")
    st.markdown("[👉 Check out the Services page for detailed info or Submit an Inquiry!](#inquiry)")

# ✅ This line is crucial!
main()