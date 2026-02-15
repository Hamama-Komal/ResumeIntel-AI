import streamlit as st
import requests

# =========================
# CONFIG
# =========================
API = "http://localhost:8000"
st.set_page_config(
    page_title="ResumeIntel AI",
    page_icon="⚡",
    layout="wide"
)

# =========================
# GLOBAL UI STYLING
# =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&display=swap');

    * {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .stApp {
        background: radial-gradient(circle at 40% -20%, #3b327a, #0a0a1a 70%) !important;
        background-attachment: fixed;
        color: white !important;
    }

    /* Tabs Container */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255,255,255,0.06);
        padding: 10px 18px;
        border-radius: 50px;
        border: 1px solid rgba(255,255,255,0.15);
        justify-content: center;
    }

    /* Tab Button */
    .stTabs [data-baseweb="tab"] {
        padding: 10px 25px;
        border-radius: 30px !important;
        font-weight: 600;
        color: #a1a1b5;
        transition: all 0.25s ease;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #6d68ff, #bb65ff);
        color: white !important;
        box-shadow: 0 4px 18px rgba(130, 80, 255, 0.35);
    }

    /* Content Card */
    .content-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 22px;
        padding: 25px;
        backdrop-filter: blur(12px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.35);
        margin-top: 20px;
    }

    /* Header Animation */
    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(25px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .header-container {
        animation: fadeUp 0.8s ease-out;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 25px;
    }

    .gradient-text {
        background: linear-gradient(90deg, #7c83ff, #d16fff, #ff6f91);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.1rem;
        font-weight: 800;
    }

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="header-container">
    <p style="color:#9ca3ff; font-weight:600; letter-spacing:2px;">NEXT-GEN CAREER ANALYTICS</p>
    <h1 class="gradient-text">ResumeIntel AI</h1>
    <p style="color:#cbd5e1; font-size:1.15rem;">Advanced AI insights powered by OpenAI & Vector Intelligence</p>
</div>
""", unsafe_allow_html=True)


# =========================
# FILE UPLOAD
# =========================
uploaded = st.file_uploader("Upload your Resume (PDF / DOCX)", type=["pdf", "docx"])

if not uploaded:
    st.markdown("""
    <div style="padding:2.5rem; text-align:center; border:2px dashed rgba(255,255,255,0.15); border-radius:20px;">
        <p style="color:#64748b;">Upload a resume to unlock AI-powered tools</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "✨ Summary",
    "🎤 Interview Prep",
    "⭐ ATS Rating",
    "💬 Chat Assistant"
])

# -------------------------
# TAB 1 — SUMMARY
# -------------------------
with tab1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    if st.button("Generate Executive Summary", use_container_width=True):
        with st.spinner("Extracting and analyzing your profile..."):
            response = requests.post(f"{API}/summarize", files={"file": uploaded})
        st.subheader("📝 Professional Summary")
        st.write(response.json().get("summary", "Error generating summary."))

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# TAB 2 — INTERVIEW Q/A
# -------------------------
with tab2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    if st.button("Generate Interview Q/A", use_container_width=True):
        with st.spinner("Preparing your mock interview..."):
            response = requests.post(f"{API}/qa", files={"file": uploaded})
        st.subheader("🎤 Interview Simulation")
        st.write(response.json().get("qa", "Error generating interview Q/A."))

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# TAB 3 — ATS RATING
# -------------------------
with tab3:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    role = st.text_input("Target Job Title", placeholder="e.g. Senior AI Engineer")

    if st.button("Run ATS Score Analysis", use_container_width=True):
        if not role:
            st.warning("Please enter a job role.")
        else:
            with st.spinner("Evaluating resume using AI + ATS rules..."):
                response = requests.post(f"{API}/rate?role={role}", files={"file": uploaded})
            st.subheader(f"⭐ ATS Fit Score for {role}")
            st.write(response.json().get("rating", "Error scoring resume."))

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------
# TAB 4 — CHAT WITH RESUME
# -------------------------
with tab4:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### 💬 Resume Intelligence Chat")

    # Custom CSS for the dots
    st.markdown("""
        <style>
        .user-dot {
            height: 12px; width: 12px; background-color: #FF8C00; 
            border-radius: 50%; display: inline-block; margin-right: 8px;
            box-shadow: 0 0 8px #FF8C00;
        }
        .ai-dot {
            height: 12px; width: 12px; background-color: #00FF7F; 
            border-radius: 50%; display: inline-block; margin-right: 8px;
            box-shadow: 0 0 8px #00FF7F;
        }
        .chat-bubble {
            margin-bottom: 20px;
            padding: 10px;
            border-left: 2px solid rgba(255,255,255,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display History
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"<div class='chat-bubble'><span class='user-dot'></span><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble'><span class='ai-dot'></span><b>AI:</b> {message['content']}</div>", unsafe_allow_html=True)

    # Input Area
    query = st.chat_input("Ask a question about the resume...")

    if query:
        # Display User Input
        st.markdown(f"<div class='chat-bubble'><span class='user-dot'></span><b>You:</b> {query}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": query})

        with st.spinner("Analyzing vector data..."):
            try:
                response = requests.post(f"{API}/chat?question={query}", files={"file": uploaded})
                raw_answer = response.json().get('answer', 'Error')

                # --- CLEANING THE OUTPUT ---
                # This check handles the messy JSON if the backend is still sending the full object
                if isinstance(raw_answer, dict):
                    clean_answer = raw_answer.get('content', str(raw_answer))
                else:
                    clean_answer = str(raw_answer)

                # Display AI Output
                st.markdown(f"<div class='chat-bubble'><span class='ai-dot'></span><b>AI:</b> {clean_answer}</div>", unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": clean_answer})

            except Exception as e:
                st.error(f"Backend offline or Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)
