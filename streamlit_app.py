import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Page selection menu in sidebar
with st.sidebar:
    selected = option_menu("Pages", ["Home", "Services", "Inquiry", "QandA", "Reviews", "Admin"],
        icons=['house', 'gear', 'envelope', 'question-circle', 'star', 'lock'],
        menu_icon="cast", default_index=0)

# Dynamically import and run the selected module
page_module = importlib.import_module(f"streamlit_app_pages.{selected}")
page_module.main()