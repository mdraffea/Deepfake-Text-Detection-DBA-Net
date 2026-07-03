"""
DBA-Net
Dual Branch Attention Network

FastText Embedding
+
Multi-scale CNN
+
BiLSTM
+
Multi-Head Self Attention
+
Gated Fusion
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

from config import (
    EMBEDDING_DIM,
    CNN_FILTERS,
    KERNEL_SIZES,
    LSTM_HIDDEN,
    ATTENTION_HEADS,
    VOCAB_SIZE,
    MAX_LEN
)


class DBANet(nn.Module):

    """
    DBA-Net

    FastText
        ↓
    Multi-scale CNN
        ↓
    BiLSTM
        ↓
    MultiHead Attention
        ↓
    Gated Fusion
        ↓
    Classifier
    """

    def __init__(self, embedding_matrix):

        super().__init__()

        embedding_matrix = torch.tensor(
            embedding_matrix,
            dtype=torch.float32
        )

        self.embedding = nn.Embedding.from_pretrained(
            embedding_matrix,
            freeze=False
        )

        self.embedding_dim = EMBEDDING_DIM