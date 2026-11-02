# 🤖 AI News Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask)
![LangChain](https://img.shields.io/badge/LangChain-AI_Framework-1C3C3C?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM_API-FF6B00?style=for-the-badge)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web_Scraping-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### 🧠 AI-Powered Technology News Summarizer

A Python application designed to collect technology and AI news, process article content, and generate concise summaries using Large Language Models.

</div>

---

## 📌 Overview

**AI News Agent** is a Python-based application that combines web scraping, content processing, and AI-powered summarization to help users explore technology and artificial intelligence news.

The application uses Python libraries to retrieve and parse web content, integrates with an LLM through the Groq API, and presents processed news through a Flask web interface.

---

## ✨ Features

### 📰 News Collection
- Retrieves news content from configured sources.
- Extracts article information from web pages.
- Processes article titles and available content.
- Organizes collected news for further processing.

### 🧠 AI Summarization
- Generates concise article summaries using an LLM.
- Helps identify important information.
- Presents summaries in a readable format.

### 🌐 Flask Web Interface
- Web-based application interface.
- Uses Flask templates to display content.
- Organizes news information and summaries.

### ⚙️ Python Backend
- HTTP requests and HTML parsing.
- Environment variable configuration.
- Modular code organization.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| Requests | HTTP requests |
| BeautifulSoup4 | HTML parsing and web scraping |
| LangChain | AI workflow integration |
| Groq API | Language model integration |
| python-dotenv | Environment variable management |

---

## 📦 Requirements

The main dependencies include:

```text
Flask
requests
beautifulsoup4
langchain
python-dotenv
groq
```

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ahmadnazzal22/ai-news-agent.git
cd ai-news-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

Keep your API key private. Do not upload your `.env` file to GitHub.

### 5. Run the Application

```bash
python app.py
```

---

## 🌐 Access the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧠 How It Works

```text
       News Sources
             ↓
       Web Scraping
             ↓
     Article Extraction
             ↓
      Content Processing
             ↓
      Groq API + LLM
             ↓
     AI-Generated Summary
             ↓
       Flask Web Interface
```

---

## 🚀 Future Improvements

Potential enhancements for future versions:

- 📰 Additional news sources.
- 🧠 News categorization.
- 📊 Sentiment analysis.
- 🔖 Article bookmarking.
- 🔐 User authentication.
- 🗄️ Database integration.
- 🐳 Docker support.
- ☁️ Cloud deployment.

---

## 🤝 Contributing

Contributions and suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

## 👨‍💻 Developer

**Ahmad Nazzal**

Python Developer | Exploring AI & Automation

- GitHub: [ahmadnazzal22](https://github.com/ahmadnazzal22)
- Repository: [AI News Agent](https://github.com/ahmadnazzal22/ai-news-agent)

---

## 📄 License

This project is licensed under the MIT License.
