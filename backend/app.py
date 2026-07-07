"""
FastAPI Backend for DBA-Net
Deepfake Text Detection
"""
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from .predict import predict_text

# ============================================================
# FastAPI App
# ============================================================

app = FastAPI(
    title="DBA-Net API",
    description="Deepfake Text Detection using DBA-Net",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# Request Model
# ============================================================

class TextRequest(BaseModel):
    text: str

# ============================================================
# Home
# ============================================================

@app.get("/")
def home():

    return {
        "message": "DBA-Net API is Running 🚀"
    }

# ============================================================
# Health Check
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

# ============================================================
# Prediction Endpoint
# ============================================================

@app.post("/predict")
def predict(request: TextRequest):

    prediction, confidence = predict_text(request.text)

    return {

        "input_text": request.text,

        "prediction": prediction,

        "confidence": round(confidence, 2)

    }