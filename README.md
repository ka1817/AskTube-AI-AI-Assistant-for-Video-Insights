---
📺 AskTube-AI Assistant for Video Insights

**AskTube-AI** is an intelligent system that allows users to input a YouTube Video ID and ask questions about the video content. It retrieves video transcripts and performs Retrieval-Augmented Generation (RAG) to provide insightful answers.

---

## 🚀 Tech Stack

- **Backend:** FastAPI (port **4000**)
- **Frontend:** Streamlit (port **8200**)
- **Model:** `llama-3.1-8b-instant` via GROQ API
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions (for testing, building, and pushing images)

---

## 📁 Folder Structure

```
AskTube-AI-Assistant-for-Video-Insights/
├── __pycache__/
├── .github/
├── .pytest_cache/
├── tests/
├── venv/
├── .dockerignore
├── .env
├── .gitignore
├── app.py
├── backend.Dockerfile
├── docker-compose.yml
├── frontend.Dockerfile
├── main.py
├── README.md
├── requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file with the following:

```bash
GROQ_API_KEY="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"
```

---

## 🚲 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ka1817/AskTube-AI-Assistant-for-Video-Insights.git
cd AskTube-AI-Assistant-for-Video-Insights
```

### 2. Pull Docker Images Directly

```bash
docker pull pranavreddy123/youtube_qa_backend

docker pull pranavreddy123/youtube_qa_frontend
```

### 3. Run using Docker-Compose

```bash
docker-compose up
```

**Note:** Ensure Docker is installed and running.

### 4. Access

- **Frontend (Streamlit UI):** [http://localhost:8200](http://localhost:8200)
- **Backend (FastAPI):** [http://localhost:4000/docs](http://localhost:4000/docs)

---

## 🏑 DockerHub Images

- **Backend:** [pranavreddy123/youtube_qa_backend](https://hub.docker.com/r/pranavreddy123/youtube_qa_backend)
- **Frontend:** [pranavreddy123/youtube_qa_frontend](https://hub.docker.com/r/pranavreddy123/youtube_qa_frontend)

---

## 📈 GitHub Repository

[GitHub - AskTube-AI](https://github.com/ka1817/AskTube-AI-Assistant-for-Video-Insights)

---

## 🎉 Features

- 🎥 Fetch YouTube Transcripts.
- 💡 Intelligent Q&A on video content.
- 🌐 FastAPI backend APIs.
- 📊 Streamlit frontend for seamless UX.
- 📦 Dockerized for easy deployment.
- 📆 Automated builds & tests via GitHub Actions.

---
![image alt](https://github.com/ka1817/AskTube-AI-Assistant-for-Video-Insights/blob/38f40516e8b45b5cde6a91e61c1406a21d29ccbc/Project_Template.png)
---

>  Developed by Pranav Reddy

