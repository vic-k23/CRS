"""Testing of module car.

Tests creating of car with correct and incorrect parameters.
"""
from collections.abc import Mapping
from pytest import mark, raises, fixture

from app.car import Car


@fixture
def car() -> Car:
    """Fixture of a Car object."""
    car_params = {"brand": "Toyota", "model": "Camry", "number": "A333AA21RUS", "seats_count": 3}
    return Car(**car_params)

@mark.parametrize("params", [
    {"brand": "Toyota", "model": "Camry", "number": "A333AA21RUS", "seats_count": 3},
])
def test_car_create_ok(params: Mapping[str, str | int]):
    """Testing of creating car with correct parameters."""
    Car(**params)

@mark.parametrize("params, expected", [
    ({"brand": "Lada", "model": "Priora"}, KeyError),
])
def test_car_create_failed(params: Mapping[str, str | int], expected: type[Exception]):
    """Testing of creating car with incorrect parameters."""
    with raises(expected):
        Car(**params)

@mark.parametrize("occupied", [1, 2, 3])
def test_seats_occupy(car: Car, occupied: int):
    """Testing of occupying seats."""
    car.seats_occupied = occupied

    assert car.seats_occupied == occupied
