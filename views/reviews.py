import streamlit as st
import pandas as pd
import os
from datetime import datetime

REVIEWS_FILE = "reviews.csv"


def load_reviews():
    if os.path.exists(REVIEWS_FILE):
        return pd.read_csv(REVIEWS_FILE)
    else:
        return pd.DataFrame(
            columns=["name", "rating", "review", "reply", "timestamp"]
        )


def save_reviews(df):
    df.to_csv(REVIEWS_FILE, index=False)


def show_view():
    st.header("⭐ Customer Reviews")
    st.markdown("Real feedback from customers who needed help — fast.")

    # Load existing reviews
    reviews_df = load_reviews()

    # -----------------------------
    # DISPLAY REVIEWS
    # -----------------------------
    if not reviews_df.empty:
        for i, row in reviews_df.iterrows():
            st.markdown(
                f"""
                **{row['name']}**  
                ⭐ {row['rating']} / 5  
                {row['review']}
                """
            )

            if pd.notna(row["reply"]) and row["reply"].strip() != "":
                st.info(f"🛠️ **QuikFix Reply:** {row['reply']}")

            st.divider()
    else:
        st.info("No reviews yet — be the first to leave one!")

    # -----------------------------
    # SUBMIT A REVIEW
    # -----------------------------
    st.subheader("✍️ Leave a Review")

    with st.form("review_form"):
        name = st.text_input("Your Name")
        rating = st.slider("Rating", 1, 5, 5)
        review_text = st.text_area("Your Review")

        submitted = st.form_submit_button("Submit Review")

        if submitted:
            if name and review_text:
                new_row = {
                    "name": name,
                    "rating": rating,
                    "review": review_text,
                    "reply": "",
                    "timestamp": datetime.utcnow().isoformat(),
                }

                reviews_df = pd.concat(
                    [reviews_df, pd.DataFrame([new_row])],
                    ignore_index=True,
                )
                save_reviews(reviews_df)
                st.success("✅ Thank you! Your review has been submitted.")
                st.rerun()
            else:
                st.error("Please fill out your name and review.")

    # -----------------------------
    # ADMIN REPLY SECTION
    # -----------------------------
    st.subheader("🔒 Admin: Reply to Reviews")

    admin_password = st.text_input(
        "Admin Password", type="password", placeholder="Enter admin password"
    )

    # ⚠️ change this later to something secure
    if admin_password == "admin123":
        if not reviews_df.empty:
            for i, row in reviews_df.iterrows():
                with st.expander(f"Reply to {row['name']}"):
                    reply_text = st.text_area(
                        "Admin Reply",
                        value="" if pd.isna(row["reply"]) else row["reply"],
                        key=f"reply_{i}",
                    )

                    if st.button("Save Reply", key=f"save_{i}"):
                        reviews_df.at[i, "reply"] = reply_text
                        save_reviews(reviews_df)
                        st.success("Reply saved.")
                        st.rerun()
        else:
            st.info("No reviews to reply to yet.")
