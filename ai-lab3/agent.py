from langchain_groq import ChatGroq
from db import init_db, run_query
from dotenv import load_dotenv
import os

load_dotenv()

#Initialize the database at startup
init_db()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), 
               model="llama-3.3-70b-versatile", 
               temperature=0.2)

DB_SCHEMA = """
Table: attendance
Columns:
- student_name (TEXT)
- subject (TEXT)
- branch (TEXT)
- month (TEXT)
- attendance_percentage (INTEGER)
"""

def generate_sql(question: str) -> str:
    prompt = f"""
You are an expert SQL assistant.

Database schema:
{DB_SCHEMA}

Write a valid SQLite SQL query for the question below.
Return ONLY the SQL query.
Do NOT use markdown or code fences.

Question:
{question}
"""
    return llm.invoke(prompt).content.strip()

def answer_question(question: str) -> str:
    sql = generate_sql(question)
    print("Generated SQL:", sql)
    
    results = run_query(sql)
    print("Results:", results)
    answer_prompt = f"""
User question:
{question}

SQL query:
{sql}

Query result:
{results}

Answer in simple English. Keep the answer concise.
"""
    return llm.invoke(answer_prompt).content
