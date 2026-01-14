import streamlit as st

def show_view():
    st.set_page_config(
        page_title="Home",
        page_icon="🏠",
        layout="wide"
    )

    st.title("🏡 Welcome to QuickFix Contractor Services")

    st.markdown("""
        Need a job done fast, with no long-term contract?  
        We’re your go-to for **quick, premium contractor help**.
        
        ✅ **Same-day or this-week service**  
        ⏱️ **Small jobs welcome — even 1 hour**  
        🛠️ **Trusted local professionals**
    """)

 