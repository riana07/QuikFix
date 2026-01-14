import streamlit as st
import importlib


# 1. Set a default app name or icon
st.set_page_config(page_title="QuikFix Job Board", page_icon="🛠️", layout="wide")

# 2. HEADER
st.title("🛠️ QuikFix")

# 3. SESSION STATE: Track which page is selected
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# 4. PAGE CONFIGURATION
pages = [
    {"label": "Home", "name": "Home", "icon": "🏠"},
    {"label": "Services", "name": "Services", "icon": "🧰"},
    {"label": "Inquiry", "name": "Inquiry", "icon": "✉️"},
    {"label": "Q&A", "name": "QandA", "icon": "❓"},
    {"label": "Reviews", "name": "Reviews", "icon": "⭐"},
    {"label": "Admin", "name": "Admin", "icon": "🔒"},
]

# 5. SAFETY CHECK
valid_page_names = [p['name'] for p in pages]
if st.session_state.current_page not in valid_page_names:
    st.session_state.current_page = "Home"

# 6. NAVIGATION RENDERING
nav_cols = st.columns(len(pages))

def set_page(p):
    st.session_state.current_page = p

for i, page in enumerate(pages):
    with nav_cols[i]:
        is_active = st.session_state.current_page == page["name"]
        st.button(
            f"{page['icon']} {page['label']}", 
            type="primary" if is_active else "secondary", 
            on_click=set_page, 
            args=(page["name"],), 
            key=f"nav_btn_{i}",
            use_container_width=True
        )

st.markdown("---")

# 7. ROUTING LOGIC
if st.session_state.current_page == "Home":
    from views import home
    home.show_view()  # You’ll define this

elif st.session_state.current_page == "Services":
    from views import services
    services.show_view()  # You’ll define this

elif st.session_state.current_page == "Inquiry":
    from views import inquiry
    inquiry.show_view()

elif st.session_state.current_page == "QandA":
    from views import qanda
    qanda.show_view()

elif st.session_state.current_page == "Reviews":
    from views import reviews
    reviews.show_view()

elif st.session_state.current_page == "Admin":
    from views import admin
    admin.show_view()

# Optional footer
footer_html = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    color: gray;
    text-align: center;
}
</style>
<div class="footer">
    <hr>
    <small>© 2026 QuikFix. All rights reserved.</small>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

