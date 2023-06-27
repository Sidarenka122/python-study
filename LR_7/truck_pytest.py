import pytest
from LR_4.problem_table_truck import Truck


@pytest.fixture
def local_truck():
    return Truck(2)


def test_truck_free_space(global_truck):
    assert global_truck.free_space == 15


def test_add_cargo(global_truck, global_table):
    assert global_truck.add_cargo(global_table.weight) == Truck.SUCCESS
    assert global_truck.add_cargo(global_table.weight) == Truck.SUCCESS
    assert global_truck.add_cargo(global_table.weight) == Truck.SUCCESS
    assert global_truck.add_cargo(global_table.weight) == Truck.SUCCESS

    assert global_truck.add_cargo(global_table.weight) == Truck.FULL


def test_add_cargo_that_takes_more_space_than_expected(global_truck):
    assert global_truck.add_cargo(16) == Truck.DOESNT_FIT


def test_unload_truck(global_truck):
    global_truck.add_cargo(15)
    assert global_truck.free_space == 0
    global_truck.unload_truck()
    assert global_truck.free_space == 15


def test_trucks_are_loaded_independently(global_truck, local_truck):
    global_truck.add_cargo(15)

    assert local_truck.free_space == 2
