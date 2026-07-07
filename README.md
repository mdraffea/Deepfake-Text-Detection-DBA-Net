# 🧠 DBA-Net: Deepfake Text Detection System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-UI-38BDF8)
![License](https://img.shields.io/badge/License-MIT-yellow)

A full-stack AI-powered Deepfake Text Detection system that identifies whether a piece of text is Human-written or AI-generated using a custom deep learning architecture called **DBA-Net**.

---

# 🌐 Live Demo

### Frontend

https://deepfake-text-detection-dba-net.netlify.app

### Backend API

https://deepfake-text-detection-dba-net.onrender.com

### API Documentation

https://deepfake-text-detection-dba-net.onrender.com/docs

---

# 📖 Overview

The rapid growth of Large Language Models has made AI-generated content nearly indistinguishable from human-written text. This project introduces **DBA-Net**, a hybrid deep learning architecture that combines:

- FastText Embeddings
- Multi-scale CNN
- Bidirectional LSTM
- Multi-Head Attention

to accurately detect AI-generated text.

The application includes:

- Modern React Frontend
- FastAPI Backend
- PyTorch Deep Learning Model
- REST API
- Live Deployment

---

# ✨ Features

- Detect AI-generated text
- Detect Human-written text
- Confidence Score
- Real-time Prediction
- Responsive UI
- FastAPI REST API
- PyTorch Inference
- Live Deployment

---

# 🏗 Model Architecture

```
Input Text
      │
      ▼
Text Cleaning
      │
      ▼
FastText Embeddings
      │
      ▼
Multi-scale CNN
      │
      ▼
BiLSTM
      │
      ▼
Multi-Head Attention
      │
      ▼
Dense Layer
      │
      ▼
Sigmoid Output
      │
      ▼
Human / AI
```

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- Tailwind CSS
- Axios
- Lucide React

## Backend

- FastAPI
- Uvicorn

## Machine Learning

- PyTorch
- FastText
- CNN
- BiLSTM
- Multi-Head Attention

## Deployment

- Netlify
- Render
- GitHub

---

# 📊 Model Performance

| Metric | Score |
|---------|------:|
| Accuracy | **92.36%** |
| Precision | **89.45%** |
| Recall | **96.04%** |
| F1 Score | **92.63%** |

---

# 📂 Project Structure

```
DBA-Net
│
├── backend
│   ├── app.py
│   ├── predict.py
│   ├── model.py
│   ├── preprocess.py
│   └── config.py
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── model
│   ├── dba_net_best.pt
│   ├── vocabulary.pkl
│   └── embedding_matrix.npy
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/mdraffea/Deepfake-Text-Detection-DBA-Net.git
```

```
cd Deepfake-Text-Detection-DBA-Net
```

---

## Backend

```
pip install -r requirements.txt
```

Run FastAPI

```
uvicorn backend.app:app --reload
```

---

## Frontend

```
cd frontend
npm install
npm run dev
```

---

# REST API

## Health Check

```
GET /health
```

Response

```json
{
  "status":"healthy"
}
```

---

## Prediction

```
POST /predict
```

Request

```json
{
    "text":"Artificial Intelligence is transforming the world."
}
```

Response

```json
{
    "prediction":"Human Written",
    "confidence":93.21
}
```

---

# 📸 Screenshots

Coming Soon

- Home
- Prediction
- Architecture
- Performance

---

# 👨‍💻 Developer

**Mohd Raffea Chisti**

B.Tech Computer Science & Engineering

Galgotias University

GitHub

https://github.com/mdraffea

LinkedIn

(Add your LinkedIn URL)

---

# ⭐ If you like this project

Give it a ⭐ on GitHub.
