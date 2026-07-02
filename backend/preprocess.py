"""
Text preprocessing utilities for DBA-Net
"""

import re
import pickle
import numpy as np
import pandas as pd

from collections import Counter
from gensim.models import FastText

from config import *


# =====================================
# CLEAN TEXT
# =====================================

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", " ", text)

    text = re.sub(r"www\S+", " ", text)

    text = re.sub(r"[^a-z0-9\s']", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# =====================================
# TOKENIZE
# =====================================

def tokenize(text):

    return clean_text(text).split()


# =====================================
# BUILD VOCABULARY
# =====================================

def build_vocab(token_lists):

    counter = Counter()

    for tokens in token_lists:
        counter.update(tokens)

    word2idx = {
        "<PAD>": 0,
        "<UNK>": 1
    }

    for word, _ in counter.most_common(VOCAB_SIZE - 2):
        word2idx[word] = len(word2idx)

    return word2idx


# =====================================
# ENCODE
# =====================================

def encode(tokens, word2idx):

    ids = []

    for token in tokens:

        ids.append(
            word2idx.get(
                token,
                word2idx["<UNK>"]
            )
        )

    ids = ids[:MAX_LEN]

    while len(ids) < MAX_LEN:

        ids.append(0)

    return ids