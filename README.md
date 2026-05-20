# 📄 DocAI Agent 🐍

<div align="center">

🧠 **AI-Powered Document Question Answering System**

Upload documents and ask questions to instantly extract accurate answers using LLMs + semantic search.
🚀 Developed by: **Ahmed Nazzal**  
🌐 Live Demo:https://www.linkedin.com/in/ahmad-nazzal-61316b406?utm_source=share_via&utm_content=profile&utm_medium=member_ios 
📦 GitHub:https://github.com/ahmadnazzal22 

</div>

---

## 📌 Overview

**DocAI Agent** is an AI-powered document understanding system that allows users to upload PDFs or TXT files and ask natural language questions.

It combines:

* 📄 Document ingestion & processing
* 🧠 Embedding-based semantic search
* ⚡ Groq LLM inference for fast responses
* 🎨 Streamlit-based dark UI

---

## ✨ Features

⚡ **Fast AI Responses**
Powered by Groq API for ultra-low latency inference

🧠 **Semantic Understanding**
Uses embeddings + vector search to retrieve the most relevant context

📄 **Document Support**

* PDF files
* TXT files

🎨 **Modern UI**
Clean dark-themed Streamlit interface

🔍 **Transparent Processing**

* Shows chunking process
* Displays retrieved context

---

## 🛠️ Tech Stack

| Tool             | Purpose          |
| ---------------- | ---------------- |
| Python           | Core language    |
| Streamlit        | Web UI           |
| LangChain        | AI orchestration |
| Groq API         | LLM inference    |
| FAISS / ChromaDB | Vector database  |

---

## 📁 Project Structure

```bash
docai-agent/
│
├── app.py
├── requirements.txt
├── .env
│
├── chains/
│   └── qa_chain.py
│
├── utils/
│   ├── loader.py
│   └── splitter.py
│
├── embeddings/
│   └── vector_store.py
│
├── data/
│   └── sample.pdf
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/docai-agent.git
cd docai-agent
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

```env
GROQ_API_KEY=your_api_key_here
```

### 6️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧠 AI Pipeline Flow

Upload Document → Chunking → Embedding → Vector Search → LLM Answer Generation

---

## 🧪 Example Usage

**Upload:** PDF or TXT file
**Ask:** *“What is the main topic of this document?”*

**Response:**

> The document discusses artificial intelligence and its applications in modern systems...

---

## 🚀 Future Improvements

* 📚 Multi-document chat
* 💬 Chat memory
* 🔐 Authentication system
* 🌍 Multi-language support
* 📊 Analytics dashboard
* ☁️ Cloud deployment
* 🐳 Docker production setup

---

## 🐳 Docker Support

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch
3. Commit changes
4. Open a Pull Request

---

## 👨‍💻 Developer

Ahmed Nazzal
🐍 Python Developer
🧠 AI Engineer
⚡ LLM Systems Builder

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---




* Add **badges (GitHub stars, license, Python version, etc.)**
* Or turn it into a **portfolio-ready case study README**
