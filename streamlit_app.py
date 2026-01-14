import streamlit as st
import importlib

PAGES = {
    "Home": "Home",
    "Services": "Services",
    "Inquiry": "Inquiry",
    "QandA": "QandA",
    "Reviews": "Reviews",
    "Admin": "Admin",
}

st.sidebar.title("Pages")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

module_name = PAGES[selection]
page_module = importlib.import_module(f"streamlit_app_pages.{module_name}")

page_module.main()
