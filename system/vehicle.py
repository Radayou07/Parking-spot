from enum import Enum

class Size(Enum):
    COMPACT = 1
    LARGE = 2

class Vehicle:
    """Base class for vehicles"""

    def __init__(self, license_plate: str, size: Size):
        self._license = license_plate
        self.size = size

    def get_license(self):
        return self._license