import streamlit as st
def show_view():



    st.header("❓ Frequently Asked Questions")


    faqs = {
        "What is QuikFix?": "A fast, flexible contracting solution for short-term home & business jobs.",
        "How quickly can someone arrive?": "We aim to connect you with a contractor the same day or within 48 hours.",
        "Do I need to sign a long-term contract?": "Nope! Most jobs are by-the-hour or flat-rate."
        }


    for q, a in faqs.items():
        with st.expander(q):
            st.markdown(a)