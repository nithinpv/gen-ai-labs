import streamlit as st
from agent.graph import build_agent

st.set_page_config(page_title="ChatMIT 2.0", page_icon="🎓", layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("### 🎓 ChatMIT 2.0")

agent = build_agent()

# Initialize conversation history in Streamlit session state
if "history" not in st.session_state:
    st.session_state.history = []
if "question" not in st.session_state:
    st.session_state.question = ""

with st.container(border=True, height=230):    
    if st.session_state.history:
        for turn in st.session_state.history:
            st.markdown(f'<div style="padding-bottom: 10px; color: #388e3c;"><b>You:</b> {turn.get("user","")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="padding-bottom: 10px;"><b>ChatMIT:</b> {turn.get("ai","")}</div>', unsafe_allow_html=True)
    else:
        st.info("Start a conversation by typing a question below.")

with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([9, 1], gap="small")
    
    with col1:
        user_input = st.text_area("Question", placeholder="Ask me anything about studies, time management, resources...", height=40)
    
    with col2:        
        submit_button = st.form_submit_button("Send", use_container_width=True)

if submit_button:
    if user_input.strip():
        result = agent.invoke({"question": user_input, "history": st.session_state.history})
        st.session_state.history.append({"user": user_input, "ai": result.get("response", "")})
        st.rerun()
    else:
        st.warning("Please enter a question.")
