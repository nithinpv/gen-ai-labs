#  AI application Tutorial

This tutorial demonstrates a very simples AI application implementation using langchain framework. The application is a helpful AI assistant called **ChatMIT**

Students can ask questions like:

- How can I study effectively for exams when I only have one week left?
- What are some good time management tips for balancing school and homework?
- What are the best free online resources to learn Python?

But will not support questions like

- What is the best smartphone to buy right now?
- Can you explain how to invest money in the stock market?

---
In this tutorial, you will understand:

- How to call an LLM from Python
- How prompts influence responses
- How to separate UI and AI logic

The application uses:
- **LLaMa 3.3** as the LLM
- **Groq** for Inference provider
- **LangChain** for Agent framework
- **Streamlit** for a rendering the UI
---

## Architecture

![Diagram](../images/arch_diagram1.png)

---

## 🗂️ Project structure
```
ai-lab1/
│
├── app.py 
├── agent.py 
└── .env 
```
---

## Step 1: Setup the code files

Create a folder under C: drive and use **git** to clone the repository
```
git clone https://github.com/nithinpv/gen-ai-labs.git
```
Or

- Go to https://github.com/nithinpv/gen-ai-labs 
- Click on **"<> Code"** and select **"Download Zip"**
- Unzip the content to a folder under C: drive

---

## Step 2: Create a Groq API key

We use **Groq** to access an LLM.

1. Go to https://console.groq.com  
2. Sign in or create a new account  
3. Click on **“API keys”** shown on the right side of the top banner  
4. Click on **“Create API key”**  
5. Copy the generated API key  

---

## Step 3: Set up environment variables

Create a file named `.env` in the project root. Add a key named **GROQ_API_KEY**. Add the API key copied in the previous step as value, as shown below

```env
GROQ_API_KEY=<paste_your_api_key_here>
```
---
## Step 4: Setup python enviroment and install dependencies

Using the vscode terminal (or command prompt/power shell) go to the **gen-ai-labs** folder (e.g. ```cd C:\gen-ai-labs```) and execute the following commands
```
python -m venv .venv

.venv\Scripts\activate.bat

cd ai-lab1

pip install langchain langchain_groq streamlit python-dotenv
```
Note: For PowerShell use ```.venv\Scripts\Activate.ps1 ```

---
## Step 5: Run the application

```
streamlit run app.py
```
Your browser will open automatically with the UI.

