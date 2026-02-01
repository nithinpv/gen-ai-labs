import streamlit as st
from agent import answer_question


st.title("🎓 Student Query Assistant")
st.write("Ask questions about student attendance using natural language.")

question = st.text_area(
    "Example questions:",
    "Which students have below 50% attendance in Physics?"
)

if st.button("Ask"):
    if question.strip():
        answer = answer_question(question)
        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
