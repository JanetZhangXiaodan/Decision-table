import pytest
from pathlib import Path
from models.decision_table import DecisionTable
from main import main
from io import StringIO
import sys


@pytest.fixture
def decision_table() -> "DecisionTable":
    filepath = Path("tests/resources/decision_tables/scoring_process_result.csv")
    return DecisionTable.create_from_csv(filepath)


def test_main(decision_table: DecisionTable) -> None:
    # Redirect stdout to capture the print statements
    sys.stdout = StringIO()

    # Call the main function
    main()

    # Get the printed output
    output = sys.stdout.getvalue()

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check the output
    assert "Status: APPROVED" in output


if __name__ == "__main__":
    pytest.main()
