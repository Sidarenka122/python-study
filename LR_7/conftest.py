import pytest
from LR_4.problem_table_truck import Truck, Table


@pytest.fixture
def global_truck():
    return Truck(15)


@pytest.fixture
def global_table():
    return Table(3)
