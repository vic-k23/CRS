"""Module for working with target."""

from typing import Unpack, TypedDict, NotRequired

from app.coordinates import Coordinates


class Address(TypedDict):
    """Target address."""

    organization_name: str
    city: str
    street: str
    building: str
    office: NotRequired[int | None]
    office_name: NotRequired[str | None]
    coordinates: NotRequired[Coordinates | None]


class Target:
    """
    A place, where you going to drive.

    This class describes a place, where you a person is going to drive by
    corporative car.
    """

    def __init__(self, /, **kwargs: Unpack[Address]) -> None:
        """Creating an object description.

        Args:
            organization_name (str): a name of organization where one going to drive.
            city (str): a name of the city, where the target is.
            street (str): a street of the target address.
            building (str): a building number with building or block.
            office (int, optional): an office number.
                                    (one of office number or office name MUST be)
            office_name (str, optional): an office name.
                                        (one of office number or office name MUST be)
            coordinates (Coordinates, optional): geographical coordinates of the target.
        """
        self._organization_name = kwargs["organization_name"]
        self._city = kwargs["city"]
        self._street = kwargs["street"]
        self._building = kwargs["building"]
        if all(
            (
                "office" not in kwargs,
                "office_name" not in kwargs,
            )
        ):
            raise KeyError("At least one of office number or office name MUST be declared.")
        if "office" in kwargs and isinstance(kwargs["office"], int):
            self._office = kwargs["office"]
        else:
            self._office = -1
        if "office_name" in kwargs and isinstance(kwargs["office_name"], str):
            self._office_name = kwargs["office_name"]
        else:
            self._office_name = ""
        if "coordinates" in kwargs:
            self._coordinates = kwargs["coordinates"]
        else:
            self._coordinates = Coordinates()
