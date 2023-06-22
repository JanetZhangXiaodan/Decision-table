import pytest
from pathlib import Path
from app.models.decision_data_holder import DecisionDataHolder
from app.models.abstract import AbstractDecisionTable

class DummyDecisionTable(AbstractDecisionTable):
    @staticmethod
    def create_from_csv(filepath: Path) -> "AbstractDecisionTable":
        return DummyDecisionTable()

    def evaluate(self, ddh: DecisionDataHolder) -> bool:
        return True


@pytest.fixture
def decision_table():
    return DummyDecisionTable()


def test_create_from_csv(decision_table: DummyDecisionTable):
    filepath = Path("dummy.csv")
    table = decision_table.create_from_csv(filepath)
    assert isinstance(table, AbstractDecisionTable)


def test_evaluate(decision_table: DummyDecisionTable):
    ddh = DecisionDataHolder()
    result = decision_table.evaluate(ddh)
    assert isinstance(result, bool)
    