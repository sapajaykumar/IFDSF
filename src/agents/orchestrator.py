"""
--------------------------------------------------------
IFDSF Research Prototype
Module : orchestrator.py
--------------------------------------------------------
"""

from src.agents.forecast_agent import ForecastAgent
from src.agents.optimization_agent import OptimizationAgent


class IFDSFOrchestrator:

    def __init__(self):

        self.forecast_agent = ForecastAgent()

        self.optimization_agent = OptimizationAgent()

    # --------------------------------------------

    def run(self):

        print("\n" + "="*70)
        print("IFDSF ORCHESTRATOR")
        print("="*70)

        forecast = self.forecast_agent.run()

        optimization = self.optimization_agent.run()

        print("\nFinal Decision Summary\n")

        print(f"Forecast      : {forecast['forecast']:.2f}")

        print(f"Recommendation: {optimization['recommendation']}")

        print(f"Risk Level    : {optimization['risk']}")

        print(f"Confidence    : {optimization['confidence']}%")

        print("\nIFDSF Workflow Completed Successfully.")

        return {

            "forecast": forecast,

            "optimization": optimization

        }


if __name__ == "__main__":

    orchestrator = IFDSFOrchestrator()

    orchestrator.run()
