class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, destination):
        if destination < self.bottom_floor or destination > self.top_floor:
            print(f"Invalid floor: {destination}. Must be between {self.bottom_floor} and {self.top_floor}.")
            return

        while self.current_floor < destination:
            self.floor_up()
        while self.current_floor > destination:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [
            Elevator(bottom_floor, top_floor) for _ in range(num_elevators)
        ]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print(f"Invalid elevator number: {elevator_number}")


# 🧪 Main Program
if __name__ == "__main__":
    # Create a building with floors 1–10 and 3 elevators
    my_building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

    # Run elevator 0 to floor 5
    my_building.run_elevator(0, 5)

    # Run elevator 2 to floor 9
    my_building.run_elevator(2, 9)
