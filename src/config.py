from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"
FEATURE_DATA = PROJECT_ROOT / "data" / "features"

DRIVE_ROOT = Path("/content/drive/MyDrive/IFDSF_Data")

DATASET_PATH = DRIVE_ROOT / "datasets"
MODEL_PATH = DRIVE_ROOT / "trained_models"
OUTPUT_PATH = DRIVE_ROOT / "outputs"
FIGURE_PATH = DRIVE_ROOT / "figures"
LOG_PATH = DRIVE_ROOT / "logs"
