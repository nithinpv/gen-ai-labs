import streamlit as st
from agent import get_help

st.title("🎓 ChatMIT 1.0")
st.write("Ask any question related to studies,  time management or learning resources.")

user_input = st.text_area("Your question")

if st.button("Get Help"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        response = get_help(user_input)

        st.subheader("Response")
        st.write(response)
