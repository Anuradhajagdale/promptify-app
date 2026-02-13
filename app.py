import streamlit as st
from database import create_tables, save_prompt, get_history
from auth import login_ui, register_ui, pin_ui
from prompt_engine import generate_prompt

# ---------------- INITIAL SETUP ----------------
create_tables()

st.set_page_config(
    page_title="PROMPTIFY – AI Prompt Engineer",
    page_icon="🧠",
    layout="centered"
)

# ---------------- DARK MODE ----------------
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
        <style>
            body { background-color: #0e1117; color: white; }
            textarea, input, select { background-color: #262730 !important; color: white !important; }
        </style>
    """, unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🧠 PROMPTIFY")
st.caption("Create powerful AI-ready prompts in seconds")

st.markdown("---")

# ---------------- AUTH FLOW ----------------
if "user" not in st.session_state:
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])
    with tab1:
        login_ui()
    with tab2:
        register_ui()

elif not st.session_state.get("pin_verified", False):
    st.subheader("🔢 Security PIN Verification")
    pin_ui()

# ---------------- MAIN APP ----------------
else:
    st.success(f"Welcome {st.session_state['user']} 👋")

    st.subheader("🎯 Prompt Builder")

    category = st.selectbox(
        "Category",
        [
            "YouTube Content",
            "Resume / LinkedIn",
            "Student Assignment",
            "Marketing / Business",
            "Motivational Speech"
        ]
    )

    topic = st.text_input("Topic / Idea")
    tone = st.selectbox("Tone", ["Professional", "Casual", "Motivational", "Persuasive"])
    length = st.selectbox("Length", ["Short", "Medium", "Long"])
    language = st.selectbox("Language", ["Auto", "English", "Hindi", "Marathi"])
    audience = st.text_input("Target Audience (optional)")

    if st.button("🚀 Generate Prompt"):
        if topic.strip() == "":
            st.warning("⚠️ Please enter a topic")
        else:
            final_prompt = generate_prompt(
                category, topic, tone, length, language, audience
            )
            save_prompt(st.session_state["user"], final_prompt)

            st.success("✅ Prompt Generated")
            st.text_area(
                "📋 Copy Your Prompt",
                final_prompt,
                height=260
            )

    # ---------------- HISTORY ----------------
    st.subheader("📜 Prompt History")
    history = get_history(st.session_state["user"])

    if history:
        for h in history[::-1]:
            st.code(h[0])
    else:
        st.info("No prompts generated yet")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:gray;'>© 2026 PROMPTIFY | Built with Python & AI</div>",
    unsafe_allow_html=True
)
