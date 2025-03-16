from pytest import mark, raises
from app.coordinates import Coordinates


@mark.parametrize("lat, lon", [
    (56.3434664, 34.986378),
    (0.3435, 0.0)])
def test_coordinates_ok(lat: float, lon: float) -> None:
    try:
        coords = Coordinates(lat, lon)
    except ValueError:
        coords = None

    assert isinstance(coords, Coordinates)


@mark.parametrize("lat, lon", [
    (234.235395, -0.4546),
    (-1.3446849, 300.098)])
def test_coordinates_failed(lat: float, lon: float) -> None:
    with raises(ValueError) as v_err:
        Coordinates(lat, lon)

    assert isinstance(v_err.value, ValueError)


@mark.parametrize("lat, lon, is_north, is_east", [
    (34.23425, 110.098, True, True),
    (34.23425, 110.098, False, False),
    (34.23425, 110.098, True, False),
    (34.23425, 110.098, False, True),
])
def test_coordinates_bool_attributes(lat: float, lon: float,
                                     is_north: bool, is_east: bool) -> None:
    coordinates = Coordinates(lat, lon,
                              is_north, is_east)

    assert coordinates.isNorth == is_north
    assert coordinates.isEast == is_east
