import streamlit as st
import re
import pandas as pd
from agent import answer_question


st.title("🎓 Student Query Assistant")
st.write("Ask questions about student attendance using natural language.")

question = st.text_area(
    "Example questions:",
    "Which students have below 50% attendance in Physics?"
)

if st.button("Ask"):
    if question.strip():
        answer, sql, results = answer_question(question)        
        st.subheader("Answer")
        st.write(answer)

        # Display debug info
        with st.expander("Debug"):
            st.markdown("Generated SQL")
            st.code(sql, language="sql")

            st.markdown("Database Result")
            if results:
                # Extract selected column names from SQL
                select_part = sql.lower().split("from")[0]
                columns = [
                    col.strip()
                    for col in select_part.replace("select", "").split(",")
                ]
                df = pd.DataFrame(results, columns=columns)
                st.dataframe(df)
            else:
                st.info("No rows returned from database.")
    else:
        st.warning("Please enter a question.")
