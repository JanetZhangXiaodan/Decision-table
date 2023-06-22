from pathlib import Path
from models.decision_table import DecisionTable
from models.decision_data_holder import DecisionDataHolder


def main() -> None:
    decision_table = DecisionTable.create_from_csv(Path("C:/Users/ABC/Desktop/decision-table-master/tests/resources/decision_tables/scoring_process_result.csv"))
    # tests/resources/decision_tables/scoring_process_result.csv

    # Create a DecisionDataHolder object with example predictor values
    ddh = DecisionDataHolder({
        "hard_check_passed": True,
        "risk_score": 11,
        "all_data_collected": True
    })

    # Evaluate the decision table using the DecisionDataHolder
    decision_table.evaluate(ddh)

    # Print the result
    if "status" in ddh:
        print(f"Status: {ddh['status']}")
    else:
        print("Decision data does not match any criteria.")


if __name__ == "__main__":
    main()
