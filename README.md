# 🧠 FinAI_Advisor.ai – RAG Agent on IBM Cloud

FinAI_Advisor.ai is an AI-powered Retrieval-Augmented Generation (RAG) agent built on IBM Cloud.
It helps users improve **digital financial literacy** with trusted answers on:
- UPI & digital payments
- Fraud prevention & safety
- Budgeting & saving
- Credit cards, interest & finance basics

---

## 🚀 **Built with**
- 🟩 IBM Granite large language model (deployed on IBM Cloud)
- 🟩 IBM Watson Assistant (chatbot interface)
- 🔍 Local retrieval from curated knowledge base (`Knowledge_base/`)
- 🐍 Python (with requests, dotenv)
- 🌱 `.env` for safe API key & endpoint management

---

## 🛠 Project structure
📦 IBM-Cloud-FinAI_Advisor-Agent-project
├── Knowledge_base/ ← Local text corpus (UPI, fraud, budgeting, etc.)
├── granite_generation.py ← Main Python script (retrieval + generation)
├── .env.example ← Template for your own API keys
├── .gitignore
├── requirement.txt
├── Project.pptx ← Presentation slides
└── README.md

---

## 📦 **Setup & run locally**
1. Clone this repo:
```bash
git clone [https://github.com/VishveshSharma2005/IBM-Cloud-FinAI_Advisor-Agent-project.git](https://github.com/VishveshSharma2005/IBM-Cloud-FinAI_Advisor-Agent-project.git)
cd IBM-Cloud-FinAI_Advisor-Agent-project
Install requirements:

Bash

pip install -r requirement.txt
Create your .env file (see .env.example):

Code snippet

API_KEY=your_ibm_api_key_here
ENDPOINT_URL=your_ibm_granite_endpoint_here
Run:

Bash

python granite_generation.py
🌐 Future scope
Streamlit web app for public demo

Add multilingual answers (Hindi, Gujarati, etc.)

Integrate Watson Assistant frontend with Granite backend

Expand knowledge base with live web data / vector index

📚 References
IBM Watson Discovery: https://cloud.ibm.com/docs/discovery

IBM Granite Models: https://www.ibm.com/products/granite-models

NPCI UPI: https://www.npci.org.in/what-we-do/upi/product-overvie

RBI Digital Literacy: https://www.rbi.org.in/financialeducation/home.aspx

Lewis et al. (2020). Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401

ChatGPT by OpenAI – assisted in drafting, ideation & docs: https://openai.com/chatgpt

✅ Author: Vishvesh Sharma (2025)
📌 Personal project for digital financial literacy, built on IBM Cloud.
