"""
Configuration file for DBA-Net
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"
MODEL_DIR = BASE_DIR / "model"
OUTPUT_DIR = BASE_DIR / "outputs"

DATASET_PATH = DATASET_DIR / "50k deepfake text balanced_dataset.csv"

MODEL_NAME = "DBA-Net"

VOCAB_SIZE = 25000
MAX_LEN = 150
EMBEDDING_DIM = 100

FASTTEXT_WINDOW = 5
FASTTEXT_MIN_COUNT = 3
FASTTEXT_EPOCHS = 5

CNN_FILTERS = 128
KERNEL_SIZES = [3, 5, 7]

LSTM_HIDDEN = 128

ATTENTION_HEADS = 4

BATCH_SIZE = 32
EPOCHS = 10

LEARNING_RATE = 1e-3
WEIGHT_DECAY = 1e-4

PATIENCE = 3

MODEL_FILE = MODEL_DIR / "dba_net_best.pt"
VOCAB_FILE = MODEL_DIR / "vocabulary.pkl"
EMBEDDING_FILE = MODEL_DIR / "embedding_matrix.npy"