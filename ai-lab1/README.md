#  AI application Tutorial

This tutorial demonstrates a very simples AI application implementation using langchain framework. The application is called **Student Support Agent**. It provides a UI page where student can post their queries and get answers.

The application uses:
- **LangChain** for LLM interaction
- **Streamlit** for a UI

---
In this tutorial, you will understand:

- How to call an LLM from Python
- How prompts influence responses
- How to separate UI and AI logic

---

## 🏗️ High-level architecture

```
User Question 
↓
Prompt (text)
↓
LLM
↓
Answer
```

---

## 🗂️ Project structure
```
ai-lab3/
│
├── app.py 
├── agent.py 
└── .env 
```

---

## 📋 Example questions

You can ask questions like:

- *How can I prepare better for technical interviews?*
- *I cannot afford online courses. What are my options for learning generative ai?*

The AI responds with **kind, practical, and actionable advice**.

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

Create a file named `.env` in the project root. Add the API key copied in the previous step, to this file as shown below

```env
GROQ_API_KEY=<paste_your_api_key_here>
```

## 🧪 Step 3: Install dependencies

```
pip install langchain langchain_groq streamlit python-dotenv
```

## ▶️ Step 4: Run the application

```
streamlit run app.py
```
Your browser will open automatically with the UI.

