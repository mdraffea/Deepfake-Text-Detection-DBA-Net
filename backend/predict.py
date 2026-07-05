"""
Predict AI/Human Text using DBA-Net
"""

import pickle
import numpy as np
import torch

from .config import *
from .model import DBANet
from .preprocess import clean_text

# ============================================================
# Device
# ============================================================

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("=" * 60)
print("Device :", DEVICE)
print("=" * 60)

# ============================================================
# Load Vocabulary
# ============================================================

print("Loading Vocabulary...")

with open(VOCAB_FILE, "rb") as f:
    word2idx = pickle.load(f)

embedding_matrix = np.load(
    EMBEDDING_FILE
)

print("Vocabulary Loaded")

# ============================================================
# Load Model
# ============================================================

print("Loading DBA-Net...")

model = DBANet(
    embedding_matrix=embedding_matrix
)

model.load_state_dict(
    torch.load(
        MODEL_FILE,
        map_location=DEVICE
    )
)

model.to(DEVICE)

model.eval()

print("Model Loaded Successfully")

# ============================================================
# Encode Text
# ============================================================

def encode(text):

    tokens = clean_text(text).split()

    ids = [
        word2idx.get(token, 1)
        for token in tokens
    ]

    ids = ids[:MAX_LEN]

    if len(ids) < MAX_LEN:

        ids += [0] * (MAX_LEN - len(ids))

    return torch.tensor(
        ids,
        dtype=torch.long
    ).unsqueeze(0)

# ============================================================
# Predict Function
# ============================================================

def predict_text(text):
    """
    Predict whether the input text is Human or AI Generated.
    """

    input_ids = encode(text).to(DEVICE)

    with torch.no_grad():

        probability = model(input_ids).item()

    confidence = probability * 100

    if probability >= 0.5:

        prediction = "AI Generated"

    else:

        prediction = "Human Written"

        confidence = (1 - probability) * 100

    return prediction, confidence

# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("DBA-Net Deepfake Text Detection")
    print("=" * 60)

    while True:

        print("\nEnter text to analyze")
        print("(Type 'exit' to quit)\n")

        text = input("Input: ")

        if text.lower() == "exit":
            break

        prediction, confidence = predict_text(text)

        print("\nPrediction :", prediction)

        print(f"Confidence : {confidence:.2f}%")

        print("-" * 60)