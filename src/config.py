"""
---------------------------------------------------------
IFDSF Prototype v1.0
Configuration Module

Project:
An Autonomous Multi-Agent AI Framework for Intelligent
Financial Planning and Decision Support using
Deep Learning and Reinforcement Learning

Author: Ajay Kumar
M.Tech Data Science & AI
IIIT Dharwad

Semester:
Prototype v1.0
---------------------------------------------------------
"""

from pathlib import Path

# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path("/content/IFDSF")

SRC_DIR = PROJECT_ROOT / "src"

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

FEATURE_DIR = DATA_DIR / "features"

RESULTS_DIR = PROJECT_ROOT / "results"

EXPERIMENTS_DIR = PROJECT_ROOT / "experiments"

MODELS_DIR = PROJECT_ROOT / "models"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# ==========================================================
# RANDOMNESS
# ==========================================================

RANDOM_SEED = 42

# ==========================================================
# DATASET
# ==========================================================

DATASET_NAME = "To be finalized"

DATASET_VERSION = "v1.0"

# ==========================================================
# MODEL SETTINGS
# ==========================================================

FORECAST_MODEL = "LSTM"

RL_ALGORITHM = "DQN"

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

PROJECT_NAME = "IFDSF"

VERSION = "Prototype v1.0"

CURRENT_SEMESTER = "Semester 2"
