"""
Train DBA-Net

This script:

1. Loads dataset
2. Cleans text
3. Builds vocabulary
4. Trains FastText
5. Creates embedding matrix
6. Creates DataLoaders
7. Trains DBA-Net
8. Saves best model
"""

import os
import pickle
import numpy as np
import pandas as pd

from collections import Counter

import torch
import torch.nn as nn

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

from torch.optim import AdamW
from torch.optim.lr_scheduler import CosineAnnealingLR

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from gensim.models import FastText

from .config import *

from .preprocess import clean_text

from .model import DBANet

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("=" * 60)
print("Device :", DEVICE)
print("=" * 60)

print("\nLoading Dataset...")

df = pd.read_csv(DATASET_PATH)

df = df.dropna(
    subset=["text", "source"]
).reset_index(drop=True)

df["label"] = (
    df["source"] == "ai"
).astype(int)

print(df.head())

print()

print("Dataset Shape :", df.shape)

print("\nCleaning text...")

df["clean_text"] = df["text"].apply(clean_text)

df["tokens"] = df["clean_text"].apply(
    lambda x: x.split()
)

print("Cleaning Complete")

train_df, temp_df = train_test_split(
    df,
    test_size=0.20,
    random_state=42,
    stratify=df["label"]
)

val_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    random_state=42,
    stratify=temp_df["label"]
)

print()

print("Training :", len(train_df))
print("Validation :", len(val_df))
print("Testing :", len(test_df))

print("\nBuilding Vocabulary...")

counter = Counter()

for sentence in train_df["tokens"]:
    counter.update(sentence)

word2idx = {
    "<PAD>": 0,
    "<UNK>": 1
}

for word, _ in counter.most_common(VOCAB_SIZE - 2):
    word2idx[word] = len(word2idx)

print("Vocabulary Size :", len(word2idx))

# ============================================================
# Train FastText
# ============================================================

print("\nTraining FastText Embeddings...")

fasttext_model = FastText(
    sentences=train_df["tokens"].tolist(),
    vector_size=EMBEDDING_DIM,
    window=FASTTEXT_WINDOW,
    min_count=FASTTEXT_MIN_COUNT,
    sg=1,
    epochs=FASTTEXT_EPOCHS
)

print("FastText Training Complete")
# ============================================================
# Embedding Matrix
# ============================================================

print("\nBuilding Embedding Matrix...")

embedding_matrix = np.zeros(
    (len(word2idx), EMBEDDING_DIM),
    dtype=np.float32
)

for word, idx in word2idx.items():

    if word in fasttext_model.wv:
        embedding_matrix[idx] = fasttext_model.wv[word]

print("Embedding Matrix Shape:", embedding_matrix.shape)
# ============================================================
# Save Vocabulary
# ============================================================

MODEL_DIR.mkdir(parents=True, exist_ok=True)

with open(VOCAB_FILE, "wb") as f:
    pickle.dump(word2idx, f)

np.save(
    EMBEDDING_FILE,
    embedding_matrix
)

print("Vocabulary Saved")
print("Embedding Matrix Saved")

# ============================================================
# Encode Text
# ============================================================

def encode(tokens):

    ids = [
        word2idx.get(token, 1)
        for token in tokens
    ]

    ids = ids[:MAX_LEN]

    if len(ids) < MAX_LEN:
        ids += [0] * (MAX_LEN - len(ids))

    return ids
train_df["input_ids"] = train_df["tokens"].apply(encode)
val_df["input_ids"] = val_df["tokens"].apply(encode)
test_df["input_ids"] = test_df["tokens"].apply(encode)

# ============================================================
# Dataset
# ============================================================

class DeepfakeDataset(Dataset):

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
    # ============================================================
# DataLoaders
# ============================================================

train_loader = DataLoader(
    DeepfakeDataset(train_df),
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_loader = DataLoader(
    DeepfakeDataset(val_df),
    batch_size=BATCH_SIZE,
    shuffle=False
)

test_loader = DataLoader(
    DeepfakeDataset(test_df),
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("\nDataLoaders Ready")

# ============================================================
# Build Model
# ============================================================

print("\nBuilding DBA-Net...")

model = DBANet(
    embedding_matrix=embedding_matrix
)

model = model.to(DEVICE)

print("DBA-Net Loaded Successfully")
# ============================================================
# Loss Function
# ============================================================

criterion = nn.BCELoss()

optimizer = AdamW(
    model.parameters(),
    lr=LEARNING_RATE,
    weight_decay=WEIGHT_DECAY
)

scheduler = CosineAnnealingLR(
    optimizer,
    T_max=EPOCHS
)
# ============================================================
# Train One Epoch
# ============================================================

def train_epoch():

    model.train()

    total_loss = 0
    predictions = []
    labels = []

    for batch in train_loader:

        input_ids = batch["input_ids"].to(DEVICE)
        target = batch["label"].to(DEVICE)

        optimizer.zero_grad()

        output = model(input_ids)

        loss = criterion(output, target)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

        predictions.extend(
            (output >= 0.5).cpu().numpy()
        )

        labels.extend(
            target.cpu().numpy()
        )

    accuracy = accuracy_score(
        labels,
        predictions
    )

    return total_loss / len(train_loader), accuracy
# ============================================================
# Validation
# ============================================================

def validate():

    model.eval()

    total_loss = 0
    predictions = []
    labels = []

    with torch.no_grad():

        for batch in val_loader:

            input_ids = batch["input_ids"].to(DEVICE)
            target = batch["label"].to(DEVICE)

            output = model(input_ids)

            loss = criterion(
                output,
                target
            )

            total_loss += loss.item()

            predictions.extend(
                (output >= 0.5).cpu().numpy()
            )

            labels.extend(
                target.cpu().numpy()
            )

    accuracy = accuracy_score(
        labels,
        predictions
    )

    return total_loss / len(val_loader), accuracy

# ============================================================
# Early Stopping
# ============================================================

best_accuracy = 0.0

patience_counter = 0

# ============================================================
# Training Loop
# ============================================================

print("\nStarting Training...\n")

for epoch in range(EPOCHS):

    train_loss, train_acc = train_epoch()

    val_loss, val_acc = validate()

    scheduler.step()

    print(
        f"Epoch [{epoch+1}/{EPOCHS}] | "
        f"Train Loss: {train_loss:.4f} | "
        f"Train Acc: {train_acc:.4f} | "
        f"Val Loss: {val_loss:.4f} | "
        f"Val Acc: {val_acc:.4f}"
    )

    if val_acc > best_accuracy:

        best_accuracy = val_acc

        patience_counter = 0

        MODEL_DIR.mkdir(parents=True, exist_ok=True)

        torch.save(
            model.state_dict(),
            MODEL_FILE
        )

        print("✅ Best model saved.")

    else:

        patience_counter += 1

        print(
            f"No Improvement "
            f"({patience_counter}/{PATIENCE})"
        )

        if patience_counter >= PATIENCE:

            print("\n🛑 Early Stopping Triggered")

            break

print("\n===================================")
print("Training Completed Successfully")
print("===================================")

print(f"Best Validation Accuracy : {best_accuracy:.4f}")