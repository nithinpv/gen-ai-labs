from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from db import init_db, run_query
from dotenv import load_dotenv
import os

load_dotenv()

#Initialize the database at startup
init_db()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), 
               model="llama-3.3-70b-versatile", 
               temperature=0.2)

sql_prompt = PromptTemplate(
    input_variables=["schema", "question"],
    template="""
You are an expert SQL assistant.

Database schema:
{schema}

Write a valid SQLite SELECT query.
- Return ONLY the SQL query
- Do NOT use markdown or code fences
- Do NOT modify data

Question:
{question}
"""
)

answer_prompt = PromptTemplate(
    input_variables=["question", "sql", "results"],
    template="""
User question:
{question}

SQL query:
{sql}

Query result:
{results}

Explain the answer in simple English.
Keep the answer concise.
"""
)

output_parser = StrOutputParser()

sql_chain = sql_prompt | llm | output_parser
answer_chain = answer_prompt | llm | output_parser


DB_SCHEMA = """
Table: attendance
Columns:
- student_name (TEXT)
- subject (TEXT)
- branch (TEXT)
- month (TEXT)
- attendance_percentage (INTEGER)
"""

def answer_question(question: str):
    sql = sql_chain.invoke({
        "schema": DB_SCHEMA,
        "question": question
    })

    results = run_query(sql)

    answer = answer_chain.invoke({
        "question": question,
        "sql": sql,
        "results": results
    })
    print(results)
    return answer, sql, results


