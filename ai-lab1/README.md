#  AI application Tutorial

This tutorial demonstrates a simple AI application implementation using langchain framework. The application is a helpful AI assistant called **ChatMIT**

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

## Folder structure
```
ai-lab1/
│
├── app.py 
├── agent.py 
├── README.md 
└── .env 
```
---

## Step 1: Setup the code files

If **git** utility is available, setup code files using **git** as mentioned below  
Create a folder named ```training``` under C: drive  
Run the following commands to clone the repository
```
cd C:\training

git clone https://github.com/nithinpv/gen-ai-labs.git
```
Or
If **git** utility is not available, setup code files as mentioned below 
Go to https://github.com/nithinpv/gen-ai-labs  
Click on **"<> Code"** and select **"Download Zip"**  
Unzip the file. Replace the existing destination path with ```C:\training``` while extraction  
After extraction rename the newly created folder from ```gen-ai-labs-main``` to ```gen-ai-labs```

---

## Step 2: Create a Groq API key

We will be using inference provider named **Groq** to access an LLM.

Go to https://console.groq.com  
Sign in or create a new account  
Click on **“API keys”** shown on the right side of the top banner  
Click on **“Create API key”**  
Copy the generated API key  

---

## Step 3: Set up environment variables
Open the ```C:\training\gen-ai-labs``` folder in vscode.  
Select the ```ai-lab1``` folder and create a new file with name ```".env"``` under it.  
Note: The full file name is ```".env"```. No other prefix or suffix should be given.  
Add the following code to this file. 

```env
GROQ_API_KEY=<value>
```
Replace ```<value>``` with the API key copied in the previous step  

---
## Step 4: Setup python enviroment and install dependencies

Open the terminal in vscode and execute the following commands
```
cd C:\training\gen-ai-labs

python -m venv .venv

.venv\Scripts\Activate.ps1 
```
Note: For command prompt use ```.venv\Scripts\activate.bat ``` instead.  
Verify that the terminal prompt shows ```(.venv)``` indicating that the virtual enviroment is active  
Install the python libraries using the following command
```
pip install langchain langchain_groq streamlit python-dotenv
```


---
## Step 5: Run the application

```
cd C:\training\gen-ai-labs\ai-lab1

streamlit run app.py
```
Your browser will open automatically with the UI.

