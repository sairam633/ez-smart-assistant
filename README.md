# Smart Assistant for Research Summarization

This project allows users to upload a PDF/TXT document, ask questions based on it, or be challenged with logic-based questions.

## Features
- PDF/TXT Upload
- Auto summarization
- Q&A and logic challenge modes
- Justified, grounded answers

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py


# 📄 Smart Assistant for Research Summarization

An AI-powered assistant that helps users interact with uploaded documents by summarizing content, answering questions, and generating logic-based challenges. Ideal for research papers, legal documents, manuals, and more.

---

## 🚀 Features

- 📥 **Document Upload** (PDF or TXT)
- 🧠 **AI Summary** (≤150 words)
- ❓ **Ask Anything**: Free-form Q&A based on document
- 🎯 **Challenge Me**: AI-generated comprehension questions
- ✅ **Answer Evaluation**: Feedback with document-based justifications
- 🖼️ Clean, user-friendly UI built with Streamlit

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI/NLP**: Hugging Face Transformers (`BERT`, `GPT-2`, `Summarization` pipeline)
- **PDF Parsing**: `pdfminer.six`
- **Environment Management**: `venv`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sairam633/ez-smart-assistant.git
cd ez-smart-assistant

Create and Activate Virtual Environment

python -m venv assistant_env
assistant_env\Scripts\activate  # Windows
# or
source assistant_env/bin/activate  # macOS/Linux

Install Dependencies
pip install -r requirements.txt
pip freeze > requirements.txt

 Run the Application

 streamlit run app.py
