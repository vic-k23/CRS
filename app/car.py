"""In this module there is a class, describing a company car."""

from typing import Unpack, TypedDict


class CarCreationParameters(TypedDict):
    """Parameters for Car class initializer.

    Args:
        brand (str): brand of the car manufacturer
        model (str): model of the car
        number (str): the state registration number
        sits_count (int): number of passengers who can be placed in the car.
    """

    brand: str
    model: str
    number: str
    seats_count: int


class Car:
    """A car of a company."""

    def __init__(self, **kwargs: Unpack[CarCreationParameters]) -> None:
        """Initializing of the car object.

        Args:
            brand (str): brand of the car manufacturer
            model (str): model of the car
            number (str): the state registration number
            seats_count (int): number of passengers who can be placed in the car.
        """
        self._brand = kwargs["brand"]
        self._model = kwargs["model"]
        self._number = kwargs["number"]
        self._seats_count = kwargs["seats_count"]
        self._seats_occupied = 0
        self._is_available = True
        self._is_on_the_way = False

    def __repr__(self) -> str:
        """A representation of a Car object."""
        return (
            f"Car(brand={self._brand}, model={self._model},"
            f"number={self._number}, seats_count={self._seats_count})"
        )

    def __str__(self) -> str:
        """String representation of the car object."""
        return (
            f"Car(brand={self._brand}, model={self._model},"
            f"number={self._number}, seats_count={self._seats_count},"
            f"seats_free={self.seats_free}, is_on_the_way={self._is_on_the_way},"
            f"is_available={self._is_available})"
        )

    @property
    def brand(self) -> str:
        """The brand of the car object."""
        return self._brand

    @property
    def model(self) -> str:
        """The model of the car object."""
        return self._model

    @property
    def number(self) -> str:
        """The state registration number of the car object."""
        return self._number

    @property
    def seats_count(self) -> int:
        """The number of the sits of the car object."""
        return self._seats_count

    @property
    def seats_free(self) -> int:
        """The number of free seats in the car object."""
        return self._seats_count - self._seats_occupied

    @property
    def seats_occupied(self) -> int:
        """The number of the sits occupied in the car object."""
        return self._seats_occupied

    @seats_occupied.setter
    def seats_occupied(self, value: int) -> None:
        """
        The number of sits occupied in the car object setter.

        Args:
            value (int): occupied number of the sits. Can't be more
                        then there are sits count in the car object.

        Raises:
            ValueError: when the value is more then there are sits in the car object
                        or left free.
        """
        if value > self._seats_count:
            raise ValueError("You can't take up more seats then there are in the car.")
        if self.seats_free - value < 0:
            raise ValueError("You can't take up more seats than there are left free in the car.")
        self._seats_occupied = value

    @property
    def is_on_the_way(self) -> bool:
        """Is the car on the way?"""
        return self._is_on_the_way

    @is_on_the_way.setter
    def is_on_the_way(self, value: bool):
        """Is the car on the way?

        If True, then is_available will be set to False.

        Args:
            value (bool): the answer on the question.
        """
        self._is_on_the_way = value
        if value:
            self._is_available = False

    @property
    def is_available(self) -> bool:
        """Is the car available?"""
        return self._is_available

    @is_available.setter
    def is_available(self, value: bool):
        """Is the car available?

        If the car on the way this property can't be set.

        Args:
            value (bool): is the car available True or False.
        """
        if not self._is_on_the_way:
            self._is_available = value

    def increase_occupied(self) -> int:
        """Increase occupied seats.

        Returns:
            int: seats, left free.
        """
        if self.seats_free:
            self._seats_occupied += 1
        return self.seats_free
