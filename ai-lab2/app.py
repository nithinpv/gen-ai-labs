import streamlit as st
from agent.graph import build_agent

st.set_page_config(
    page_title="Student Support AI",
    page_icon="🎓"
)

st.title("🎓 Student Support AI Agent")
st.write("Ask any question related to studies, stress, or resources.")

agent = build_agent()

user_input = st.text_area("Your question")

if st.button("Get Help"):
    if user_input.strip():
        result = agent.invoke({"user_input": user_input})
        st.subheader("AI Response")
        st.write(result["response"])
    else:
        st.warning("Please enter a question.")
