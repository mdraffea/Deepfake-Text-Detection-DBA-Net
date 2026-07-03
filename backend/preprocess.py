import os
import re
import pickle
import numpy as np
import pandas as pd

from collections import Counter
from gensim.models import FastText

from sklearn.model_selection import train_test_split

from config import *

# =====================================
# LOAD DATASET
# =====================================

def load_dataset():

    df = pd.read_csv(DATASET_PATH)

    df = df.dropna(subset=["text", "source"])

    df = df.reset_index(drop=True)

    df["label"] = (df["source"] == "ai").astype(int)

    return df

# =====================================
# TRAIN TEST SPLIT
# =====================================

def split_dataset(df):

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

    return train_df, val_df, test_df

# =====================================
# TRAIN FASTTEXT
# =====================================

def train_fasttext(token_lists):

    print("Training FastText...")

    model = FastText(

        sentences=token_lists,

        vector_size=EMBEDDING_DIM,

        window=FASTTEXT_WINDOW,

        min_count=FASTTEXT_MIN_COUNT,

        epochs=FASTTEXT_EPOCHS,

        sg=1

    )

    print("FastText Training Complete")

    return model

# =====================================
# EMBEDDING MATRIX
# =====================================

def build_embedding_matrix(
    word2idx,
    fasttext_model
):

    embedding_matrix = np.zeros(

        (
            len(word2idx),
            EMBEDDING_DIM
        ),

        dtype=np.float32

    )

    for word, idx in word2idx.items():

        if word in fasttext_model.wv:

            embedding_matrix[idx] = fasttext_model.wv[word]

    return embedding_matrix

# =====================================
# SAVE VOCABULARY
# =====================================

def save_vocab(word2idx):

    with open(
        VOCAB_FILE,
        "wb"
    ) as f:

        pickle.dump(
            word2idx,
            f
        )

    print("Vocabulary Saved")

    # =====================================
# LOAD VOCABULARY
# =====================================

def load_vocab():

    with open(
        VOCAB_FILE,
        "rb"
    ) as f:

        word2idx = pickle.load(f)

    return word2idx