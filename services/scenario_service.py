import pandas as pd
from pathlib import Path

from models.scenario import Scenario


class ScenarioService:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent.parent

        self.file = self.project_root / "data" / "scenarios.csv"

        if not self.file.exists():

            df = pd.DataFrame(
                columns=[
                    "Scenario",
                    "Category",
                    "Product",
                    "Volume",
                    "Shipment",
                    "GSV",
                    "NSV",
                    "Spend",
                    "Fund Balance",
                    "Created Time",
                ]
            )

            df.to_csv(self.file, index=False)

    def save(self, scenario: Scenario):

        df = pd.read_csv(self.file)

        new_row = {
            "Scenario": scenario.scenario_name,
            "Category": scenario.category,
            "Product": scenario.product,
            "Volume": scenario.volume,
            "Shipment": scenario.shipment,
            "GSV": scenario.gsv,
            "NSV": scenario.nsv,
            "Spend": scenario.spend,
            "Fund Balance": scenario.fund_balance,
            "Created Time": scenario.created_time,
        }

        df = pd.concat(
            [df, pd.DataFrame([new_row])],
            ignore_index=True,
        )

        df.to_csv(self.file, index=False)

    def load(self):

        return pd.read_csv(self.file)
