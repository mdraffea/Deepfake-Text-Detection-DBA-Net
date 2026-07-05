"""
Evaluate DBA-Net on Test Dataset
"""

import pickle
import numpy as np
import pandas as pd
import torch

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

from .config import *
from .model import DBANet
from .preprocess import clean_text

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("=" * 60)
print("Device :", DEVICE)
print("=" * 60)

print("\nLoading Vocabulary...")

with open(VOCAB_FILE, "rb") as f:
    word2idx = pickle.load(f)

embedding_matrix = np.load(
    EMBEDDING_FILE
)

print("Vocabulary Loaded")
print("Embedding Matrix Loaded")

print("\nLoading Dataset...")

df = pd.read_csv(DATASET_PATH)

df = df.dropna(
    subset=["text", "source"]
).reset_index(drop=True)

df["label"] = (
    df["source"] == "ai"
).astype(int)

df["clean_text"] = df["text"].apply(clean_text)

df["tokens"] = df["clean_text"].apply(
    lambda x: x.split()
)

from sklearn.model_selection import train_test_split

_, temp_df = train_test_split(
    df,
    test_size=0.20,
    random_state=42,
    stratify=df["label"]
)

_, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    random_state=42,
    stratify=temp_df["label"]
)

print("Test Samples :", len(test_df))

def encode(tokens):

    ids = [
        word2idx.get(token, 1)
        for token in tokens
    ]

    ids = ids[:MAX_LEN]

    if len(ids) < MAX_LEN:
        ids += [0] * (MAX_LEN - len(ids))

    return ids

test_df["input_ids"] = test_df["tokens"].apply(
    encode
)

class TestDataset(Dataset):

    def __init__(self, dataframe):

        self.input_ids = dataframe["input_ids"].tolist()

        self.labels = dataframe["label"].tolist()

    def __len__(self):

        return len(self.labels)

    def __getitem__(self, idx):

        return {

            "input_ids": torch.tensor(
                self.input_ids[idx],
                dtype=torch.long
            ),

            "label": torch.tensor(
                self.labels[idx],
                dtype=torch.float
            )

        }
test_loader = DataLoader(
  TestDataset(test_df),
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("Test DataLoader Ready")

# ============================================================
# Load Trained Model
# ============================================================

print("\nLoading DBA-Net...")

model = DBANet(
    embedding_matrix=embedding_matrix
)

model.load_state_dict(
    torch.load(
        MODEL_FILE,
        map_location=DEVICE
    )
)

model = model.to(DEVICE)

model.eval()

print("Model Loaded Successfully")

# ============================================================
# Evaluation
# ============================================================

predictions = []

labels = []

with torch.no_grad():

    for batch in test_loader:

        input_ids = batch["input_ids"].to(DEVICE)

        target = batch["label"].to(DEVICE)

        output = model(input_ids)

        pred = (output >= 0.5).float()

        predictions.extend(
            pred.cpu().numpy()
        )

        labels.extend(
            target.cpu().numpy()
        )

        # ============================================================
# Metrics
# ============================================================

accuracy = accuracy_score(
    labels,
    predictions
)

precision = precision_score(
    labels,
    predictions
)

recall = recall_score(
    labels,
    predictions
)

f1 = f1_score(
    labels,
    predictions
)


# ============================================================
# Results
# ============================================================

print("\n" + "=" * 45)

print("DBA-NET TEST RESULTS")

print("=" * 45)

print()

print(f"Accuracy  : {accuracy:.4f}")

print(f"Precision : {precision:.4f}")

print(f"Recall    : {recall:.4f}")

print(f"F1 Score  : {f1:.4f}")


print("\nConfusion Matrix")

print(
    confusion_matrix(
        labels,
        predictions
    )
)

print("\nClassification Report\n")

print(

    classification_report(

        labels,

        predictions,

        target_names=[
            "Human",
            "AI"
        ]

    )

)