from vehicle import Vehicle, Size
from spot_state import SpotState

class ParkingSpot:
    '''Base class for parking spots.'''

    '''We want to know if the vehicle can fit in the spot or not,
        also the status of the spot (available, occupied, reserved) of that spot'''

    def __init__(self, id: int, size: Size, is_occupied: SpotState):
        self.id = id
        self.size = size
        self.is_occupied = is_occupied
    def exited(self):
        '''When a vehicle exits the parking spot'''
        self.is_occupied = SpotState.AVAILABLE

    def parked(self):
        '''When a vehicle parks in the parking spot'''
        self.is_occupied = SpotState.OCCUPIED
    def reserved(self):
        '''When a parking spot is reserved'''
        self.is_occupied = SpotState.RESERVED

    def can_fit(self, vehicle: Vehicle) -> bool:
        '''Check if the vehicle size is fit or not'''
        return vehicle.size.value <= self.size.value

    def status(self):
        '''Check the status of the parking spot'''
        return self.is_occupied

     # Placeholder method to be overridden in subclasses
class CompactSpot(ParkingSpot):
    '''Compact parking spot class'''
    
    
    def can_fit(self, vehicle: Vehicle) -> bool:
        if self.status() is SpotState.AVAILABLE:
            return vehicle.size == Size.COMPACT and vehicle.size.value <= self.size.value
        return False

class LargeSpot(ParkingSpot):
    '''Large parking spot class'''
    
    def can_fit(self, vehicle: Vehicle) -> bool:
        if self.status() is SpotState.AVAILABLE:
            return vehicle.size == Size.LARGE and vehicle.size.value <= self.size.value
        return False