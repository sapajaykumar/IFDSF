"""
--------------------------------------------------------
IFDSF Research Prototype
Module : forecast_agent.py

Purpose:
Forecast Agent responsible for invoking the
Forecasting Engine and returning forecasting results.

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

import os
import pandas as pd


class ForecastAgent:

    def __init__(self):

        self.name = "Forecast Agent"

        self.result_file = "/content/drive/MyDrive/IFDSF_Data/outputs/forecast_results.csv"

        self.metrics_file = "/content/drive/MyDrive/IFDSF_Data/outputs/forecast_metrics.csv"

    # -------------------------------------------------

    def run(self):

        print("=" * 60)
        print(f"Running {self.name}")
        print("=" * 60)

        if not os.path.exists(self.result_file):

            print("Forecast results not found.")
            print("Run forecasting_model.py first.")

            return None

        results = pd.read_csv(self.result_file)

        metrics = pd.read_csv(self.metrics_file)

        latest_prediction = results.iloc[-1]["Predicted"]

        latest_actual = results.iloc[-1]["Actual"]

        print(f"\nLatest Forecast : {latest_prediction:.2f}")
        print(f"Latest Actual   : {latest_actual:.2f}")

        print("\nModel Performance")

        print(metrics)

        response = {

            "agent": self.name,

            "forecast": float(latest_prediction),

            "actual": float(latest_actual),

            "metrics": metrics.to_dict(),

            "status": "SUCCESS"

        }

        print("\nForecast Agent Completed Successfully.")

        return response


# ---------------------------------------------------------

if __name__ == "__main__":

    agent = ForecastAgent()

    output = agent.run()

    print("\nReturned Object")

    print(output)
