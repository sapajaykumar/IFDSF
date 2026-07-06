"""
--------------------------------------------------------
IFDSF Research Prototype
Module : orchestrator.py

Purpose:
Coordinates all AI agents within the IFDSF
framework.

Author : Ajay Kumar
M.Tech (Data Science & AI)
IIIT Dharwad
--------------------------------------------------------
"""

from src.agents.forecast_agent import ForecastAgent
from src.agents.optimization_agent import OptimizationAgent


class IFDSFOrchestrator:

    def __init__(self):

        self.name = "IFDSF Orchestrator"

        self.forecast_agent = ForecastAgent()

        self.optimization_agent = OptimizationAgent()

    # -------------------------------------------------

    def run(self):

        print("\n" + "=" * 70)
        print(self.name)
        print("=" * 70)

        # -----------------------------
        # Step 1
        # -----------------------------

        forecast_response = self.forecast_agent.run()

        # -----------------------------
        # Step 2
        # -----------------------------

        optimization_response = self.optimization_agent.run()

        # -----------------------------
        # Final Summary
        # -----------------------------

        print("\n" + "=" * 70)
        print("IFDSF FINAL DECISION")
        print("=" * 70)

        print(f"Forecast        : {forecast_response['forecast']:.2f}")
        print(f"Actual          : {forecast_response['actual']:.2f}")

        print(f"Recommendation  : {optimization_response['recommendation']}")
        print(f"Risk Level      : {optimization_response['risk']}")
        print(f"Confidence      : {optimization_response['confidence']}%")

        print("\nIFDSF Workflow Completed Successfully.")

        return {

            "forecast": forecast_response,

            "optimization": optimization_response

        }


# --------------------------------------------------------

if __name__ == "__main__":

    orchestrator = IFDSFOrchestrator()

    result = orchestrator.run()

    print("\nReturned Object")

    print(result)
