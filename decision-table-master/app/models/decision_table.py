from pathlib import Path
from models.abstract import AbstractDecisionTable
from models.decision_data_holder import DecisionDataHolder
import csv
from typing import Any, List, Dict


class DecisionTable(AbstractDecisionTable):
    def __init__(self, table_data: List) -> None:
        self.table_data = table_data

    @staticmethod
    def create_from_csv(filepath: Path) -> "DecisionTable":
        table_data = []
        with open(filepath, "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                table_data.append(dict(row))

        return DecisionTable(table_data)

    def evaluate(self, ddh: DecisionDataHolder) -> bool:
        for row in self.table_data:
            if self._evaluate_conditions(row, ddh):
                return ddh  # Evaluation ends if conditions are met

        return False  # Evaluation completed, no conditions met

    def _evaluate_conditions(self, row: Dict, ddh: DecisionDataHolder) -> bool:
        for i, cell in enumerate(row.items()):
            predictor_name, condition = cell
            if predictor_name == "*":
                continue
            if predictor_name == "status":
                output_predictor, output_value = cell
                ddh[output_predictor] = output_value
                return ddh
            if not self._evaluate_condition(predictor_name, condition, ddh):
                return False  # Condition not met, move to the next row

        return ddh  # All conditions met for the row

    @staticmethod
    def _evaluate_condition(predictor_name: Any, condition: str, ddh: DecisionDataHolder) -> bool:
        predictor_value = ddh.get(predictor_name)
        if condition.startswith("="):
            return str(predictor_value).lower() == condition[1:]
        elif condition.startswith(">="):
            return predictor_value >= int(condition[2:])
        elif condition.startswith("<="):
            return predictor_value <= int(condition[2:])
        elif condition.startswith(">"):
            return predictor_value > int(condition[1:])
        elif condition.startswith("<"):
            return predictor_value < int(condition[1:])
        else:
            raise ValueError("Invalid condition")
