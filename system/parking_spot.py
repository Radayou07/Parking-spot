class ParkingSpot:
    
    def __init__(self, id, size, is_occupied):
        self.id = id
        self.size = size
        self.is_occupied = is_occupied

class CompactSpot(ParkingSpot):
    pass

class  LargeSpot(ParkingSpot):
    pass

