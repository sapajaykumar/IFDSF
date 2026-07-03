"""
IFDSF Prototype v1.0

Main Entry Point
"""

from src.config import *


def main():

    print("=" * 60)
    print(PROJECT_NAME)
    print(VERSION)
    print("=" * 60)

    print(f"Project Root : {PROJECT_ROOT}")
    print(f"Data Folder  : {DATA_DIR}")
    print(f"Random Seed  : {RANDOM_SEED}")
    print(f"Forecast AI  : {FORECAST_MODEL}")
    print(f"RL Algorithm : {RL_ALGORITHM}")

    print("\nIFDSF Prototype Successfully Started")


if __name__ == "__main__":
    main()
