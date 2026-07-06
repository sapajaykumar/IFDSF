"""
--------------------------------------------------------
IFDSF Research Prototype
Module: data_catalog.py

Maintains information about all datasets used
in the project.

Author: Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

from pathlib import Path

# Google Drive Dataset Folder
DATASET_FOLDER = Path("/content/drive/MyDrive/IFDSF_Data/datasets")

# Dataset Information
DATASETS = {

    "D1": {
        "name": "SEC EDGAR Financial Statement Data",
        "provider": "U.S. SEC",
        "folder": DATASET_FOLDER / "sec_edgar",
        "format": "CSV",
        "purpose": "Enterprise financial statements"
    },

    "D2": {
        "name": "Corporate Financial Dataset",
        "provider": "Kaggle",
        "folder": DATASET_FOLDER / "kaggle_corporate",
        "format": "CSV",
        "purpose": "Corporate financial metrics"
    },

    "D3": {
        "name": "M5 Forecasting Dataset",
        "provider": "Kaggle",
        "folder": DATASET_FOLDER / "m5_forecasting",
        "format": "CSV",
        "purpose": "Forecasting benchmark"
    },

    "D4": {
        "name": "FRED Economic Data",
        "provider": "Federal Reserve",
        "folder": DATASET_FOLDER / "fred",
        "format": "CSV",
        "purpose": "Macroeconomic indicators"
    },

    "D5": {
        "name": "Yahoo Finance",
        "provider": "Yahoo Finance",
        "folder": DATASET_FOLDER / "yahoo_finance",
        "format": "CSV",
        "purpose": "Financial market time series"
    }

}


def show_datasets():
    """
    Display all available datasets.
    """

    print("\nAvailable Datasets\n")

    for key, value in DATASETS.items():

        print(f"{key}")
        print(f" Name     : {value['name']}")
        print(f" Provider : {value['provider']}")
        print(f" Folder   : {value['folder']}")
        print(f" Purpose  : {value['purpose']}")
        print("-" * 50)


if __name__ == "__main__":

    show_datasets()
