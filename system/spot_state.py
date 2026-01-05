from enum import Enum

class SpotState(Enum):
    '''State of a parking spot'''
    AVAILABLE = 1
    OCCUPIED = 2
    RESERVED = 3