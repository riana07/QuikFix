import streamlit as st
import streamlit.components.v1 as components

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
    st.markdown("---")
    st.subheader("🌍 Visitors Around the Globe")

    st.markdown(
    """
    <a href="https://mapmyvisitors.com/web/1c1tk" title="Visit tracker" target="_blank">
        <img src="https://mapmyvisitors.com/map.png?cl=5b5151&w=561&t=tt&d=cFREfn93-g8GoqabQ9uiD0Eo99ymx1ckkUA1n3O2SgQ&ct=dddddd&co=d8d8d8" alt="Visitor Map" style="width:100%; max-width:561px;">
    </a>
    """,
    unsafe_allow_html=True
)
 