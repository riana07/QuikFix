import streamlit as st
import pandas as pd
import os

SUBMISSION_FILE = "Submissions.csv"

def load_submissions():
    if os.path.exists(SUBMISSION_FILE):
        return pd.read_csv(SUBMISSION_FILE)
    else:
        return pd.DataFrame()

def show_view():
    st.header("🔒 Admin Panel")
    st.caption("Restricted access: view user inquiries")

    # Simple login
    password = st.text_input("Enter admin password", type="password")
    if password != "admin123":  # 🔒 change this later!
        st.warning("Enter a valid password to view submissions.")
        return

    # Load submission data
    df = load_submissions()

    if df.empty:
        st.info("No inquiries submitted yet.")
    else:
        st.success(f"Total inquiries: {len(df)}")
        st.dataframe(df, use_container_width=True)

        # Optional download button
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="inquiries.csv",
            mime="text/csv",
        )
