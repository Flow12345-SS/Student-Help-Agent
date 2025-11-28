import streamlit as st
from agent import student_agent
from datetime import datetime



# Page configuration
st.set_page_config(
    page_title="EduMate AI",
    page_icon="📘",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.main {
    background: radial-gradient(circle at top, #eef3ff, #ffffff);
}

/* Glass card */
.glass {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}

/* Title */
.title {
    font-size: 50px;
    font-weight: 700;
    color: #1a237e;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    color: #444;
}

/* Chat bubbles */
.user {
    background: #1a237e;
    color: white;
    padding: 12px;
    border-radius: 15px;
    margin: 10px 0;
}

.bot {
    background: #e8eaf6;
    padding: 12px;
    border-radius: 15px;
    margin: 10px 0;
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ EduMate AI")
st.sidebar.write("Your personal study buddy")
st.sidebar.markdown("---")

st.sidebar.subheader("📌 What can I do?")
st.sidebar.markdown("""
✅ Explain concepts  
✅ Give study tips  
✅ Motivate you  
✅ Help in AI/ML basics  
✅ Solve simple doubts  
""")

st.sidebar.markdown("---")
st.sidebar.write("🕒 Today:", datetime.now().strftime("%d %B %Y"))

# ---------- MAIN PAGE ----------

col1, col2 = st.columns([3,1])

with col1:
    st.markdown('<div class="title">📘 EduMate - Student Help AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Ask. Learn. Grow. 🚀</div>', unsafe_allow_html=True)

with col2:
    st.metric(label="Status", value="Online ✅")

st.write("")

# Welcome Card
with st.container():
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("👋 Welcome, Simran!")
    st.write("""
    I am **EduMate**, your smart academic assistant.
    Ask any study-related question and I’ll help you instantly.

    Try asking:
    - What is AI?
    - Give me study tips
    - Motivate me
    - What is Machine Learning?
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")


# ---------- CHAT SECTION ----------
with st.container():
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("💬 Chat with EduMate")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Type your message here 👇")

    if st.button("Send 🚀", key="send"):
        if user_input.strip() != "":
            response = student_agent(user_input)

        # ✅ CLEAR OLD CHAT FIRST
        st.session_state.chat_history = []

        # ✅ ADD ONLY LATEST QUESTION + ANSWER
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("EduMate", response))
    else:
        st.warning("Please type something first!")



    # Display chat
    for sender, message in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f'<div class="user"><b>You:</b> {message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot"><b>EduMate:</b> {message}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
