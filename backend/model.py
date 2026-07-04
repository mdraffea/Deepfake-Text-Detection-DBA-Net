"""
DBA-Net
Dual Branch Attention Network

Architecture

FastText
      │
Multi-Scale CNN
      │
BiLSTM
      │
Multi-Head Self Attention
      │
Gated Fusion
      │
Classifier
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

from .config import (
    EMBEDDING_DIM,
    CNN_FILTERS,
    KERNEL_SIZES,
    LSTM_HIDDEN,
    NUM_HEADS
)


class DBANet(nn.Module):
    """
    Dual Branch Attention Network

    Branch 1:
        Multi-scale CNN

    Branch 2:
        BiLSTM + MultiHead Attention

    Fusion:
        Gated Feature Fusion

    Output:
        Binary Classification
    """

    def __init__(self, embedding_matrix, dropout=0.4):

        super(DBANet, self).__init__()

        # ==========================================
        # FastText Embedding Layer
        # ==========================================

        embedding_matrix = torch.tensor(
            embedding_matrix,
            dtype=torch.float32
        )

        self.embedding = nn.Embedding.from_pretrained(
            embedding_matrix,
            freeze=False
        )

        # ==========================================
        # CNN Branch
        # ==========================================

        self.convs = nn.ModuleList([
            nn.Conv1d(
                in_channels=EMBEDDING_DIM,
                out_channels=CNN_FILTERS,
                kernel_size=k,
                padding=k // 2
            )
            for k in KERNEL_SIZES
        ])

        # ==========================================
        # BiLSTM Branch
        # ==========================================

        self.bilstm = nn.LSTM(
            input_size=EMBEDDING_DIM,
            hidden_size=LSTM_HIDDEN,
            num_layers=1,
            batch_first=True,
            bidirectional=True
        )

        # ==========================================
        # Multi-Head Self Attention
        # ==========================================

        self.attention = nn.MultiheadAttention(
    embed_dim=LSTM_HIDDEN * 2,
    num_heads=NUM_HEADS,
    batch_first=True
)

        # ==========================================
        # Feature Dimensions
        # ==========================================

        self.cnn_dim = CNN_FILTERS * len(KERNEL_SIZES)

        self.lstm_dim = LSTM_HIDDEN * 2

        self.fusion_dim = self.cnn_dim + self.lstm_dim

        # ==========================================
        # Gated Fusion
        # ==========================================

        self.gate = nn.Sequential(

            nn.Linear(
                self.fusion_dim,
                self.fusion_dim
            ),

            nn.Sigmoid()

        )

        # ==========================================
        # Classifier
        # ==========================================

        self.fc1 = nn.Linear(
            self.fusion_dim,
            256
        )

        self.fc2 = nn.Linear(
            256,
            128
        )

        self.fc3 = nn.Linear(
            128,
            1
        )

        self.dropout = nn.Dropout(dropout)
        self.initialize_weights()

    def forward(self, input_ids):           

        # =====================================
        # FastText Embedding
        # =====================================

        embedding = self.embedding(input_ids)

        # =====================================
        # CNN Branch
        # =====================================

        cnn_input = embedding.transpose(1, 2)

        cnn_features = []

        for conv in self.convs:

            feature = F.relu(conv(cnn_input))

            feature = F.adaptive_max_pool1d(
                feature,
                1
            ).squeeze(-1)

            cnn_features.append(feature)

        cnn_output = torch.cat(
            cnn_features,
            dim=1
        )

        # =====================================
        # BiLSTM Branch
        # =====================================

        lstm_output, _ = self.bilstm(
            embedding
        )

        # =====================================
        # Multi-Head Self Attention
        # =====================================

        attention_output, _ = self.attention(
            lstm_output,
            lstm_output,
            lstm_output
        )

        lstm_feature = torch.mean(
            attention_output,
            dim=1
        )

        # =====================================
        # Feature Fusion
        # =====================================

        fused = torch.cat(
            [
                cnn_output,
                lstm_feature
            ],
            dim=1
        )

        gate = self.gate(fused)

        fused = fused * gate

        # =====================================
        # Classification Head
        # =====================================

        x = F.relu(
            self.fc1(fused)
        )

        x = self.dropout(x)

        x = F.relu(
            self.fc2(x)
        )

        x = self.dropout(x)

        logits = self.fc3(x)

        output = torch.sigmoid(
            logits
        )

        return output.squeeze(1)
    def initialize_weights(self):
        """
    Initialize trainable weights using Xavier initialization.
        """

        for module in self.modules():

            if isinstance(module, nn.Linear):
                nn.init.xavier_uniform_(module.weight)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

            elif isinstance(module, nn.Conv1d):
                nn.init.xavier_uniform_(module.weight)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

            elif isinstance(module, nn.LSTM):

                for name, param in module.named_parameters():

                    if "weight" in name:
                        nn.init.xavier_uniform_(param)

                    elif "bias" in name:
                        nn.init.zeros_(param)