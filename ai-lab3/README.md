# 🎓 Student Query Assistant  
### RAG (Retrieval-Augmented Generation) Tutorial

This tutorial demonstrates how to build a small but realistic AI system. It answers natural language questions over **tudent attendance data stored in a relational database.

The application uses:
- **SQLite** as the database
- **LangChain** for LLM interaction
- **Streamlit** for a UI

---
**Retrieval-Augmented Generation (RAG)** means:

> The AI does not store or memorize data.  
> It **retrieves data from an external source** and then generates an answer.

In this tutorial:
- **Retrieval** → SQL query on a relational database
- **Generation** → LLM explains the query result in plain English

### Why this is important
- Data stays **accurate and up to date**
- Prevents hallucinated answers
- Works well with existing enterprise databases

---

## 🏗️ High-level architecture

```
User Question (English)
↓
LLM → Generate SQL query
↓
Attendance Database 
↓
Query Results
↓
LLM → Convert results to plain English
↓
Answer
```

**Key idea:**
- The LLM *reasons*
- The database *answers*
- The LLM *explains*

---

## 🗂️ Project structure
```
ai-lab3/
│
├── app.py 
├── agent.py 
├── db.py 
├── attendance.csv 
├── requirements.txt
└── .env 
```

---

## 📋 Example questions

You can ask questions like:

- Which students have 100% attendance in all the subjects in the "CSE" branch?
- Which students have below 50% attendance in Physics?
- What is the average attendance in Maths subject in the "ECE" branch?

---

## 🔑 Step 1: Create a Groq API key

We use **Groq** to access an LLM.

1. Go to https://console.groq.com  
2. Sign in or create a new account  
3. Click on **“API keys”** shown on the right side of the top banner  
4. Click on **“Create API key”**  
5. Copy the generated API key  

---

## 🔐 Step 2: Set up environment variables

Create a file named `.env` in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

## 🧪 Step 3: Install dependencies

```
pip install -r requirements.txt
```

## ▶️ Step 4: Run the application

```
streamlit run app.py
```
Your browser will open automatically with the UI.

