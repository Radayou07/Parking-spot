from vehicle import Vehicle, Size
from parking_spot import CompactSpot, LargeSpot
from spot_state import SpotState

def main():
    # Create some vehicles
    car = Vehicle("ABC123", Size.COMPACT)
    truck = Vehicle("XYZ789", Size.LARGE)

    # Create parking spots
    compact_spot = CompactSpot(id=1, size=Size.COMPACT, is_occupied=SpotState.AVAILABLE)
    large_spot = LargeSpot(id=2, size=Size.LARGE, is_occupied=SpotState.AVAILABLE)

    # Test compact spot
    print("Compact spot tests:")
    print("Car fits?", compact_spot.can_fit(car))      # True
    print("Truck fits?", compact_spot.can_fit(truck))  # False

    # Park the car
    compact_spot.parked()
    print("Compact spot status after parking:", compact_spot.status())

    # Exit the car
    compact_spot.exited()
    print("Compact spot status after exit:", compact_spot.status())

    # Test large spot
    print("\nLarge spot tests:")
    print("Car fits?", large_spot.can_fit(car))        # True
    print("Truck fits?", large_spot.can_fit(truck))    # True

    # Reserve the large spot
    large_spot.reserved()
    print("Large spot status after reservation:", large_spot.status())

if __name__ == "__main__":
    main()