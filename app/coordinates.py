class Coordinates:
    """
    Класс для работы с координатами.
    """

    # Cheboksary is the default: latitude - 56.139918, longitude - 47.247728
    def __init__(self, latitude: float = 56.139918,
                 longitude: float = 47.247728,
                 is_north: bool = True,
                 is_east: bool = True) -> None:
        if 0.0 <= latitude <= 90.0:
            self.__latitude = latitude
        else:
            raise ValueError("Latitude must be only more or equal 0.0 "
                             "and less or equal 90.0")
        if 0.0 <= longitude <= 180.0:
            self.__longitude = longitude
        else:
            raise ValueError("Longitude must be more or equal 0.0 "
                             "and less or equal 180.0")
        self.__is_north = is_north
        self.__is_east = is_east

    @property
    def isNorth(self) -> bool:
        """Флаг Северной широты

        Returns:
            bool: Северной широты (True), или Южной (False)
        """
        return self.__is_north

    @property
    def isEast(self) -> bool:
        """Флаг Восточной долготы

        Returns:
            bool: Восточной долготы (True), или Южной (False)
        """
        return self.__is_east
