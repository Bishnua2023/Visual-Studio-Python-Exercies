class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("Invalid floor!")
            return

        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        elevator = self.elevators[elevator_num - 1]  # Elevator numbers start from 1
        elevator.go_to_floor(destination_floor)


# Testing the Building class
building = Building(1, 10, 3)  # Example: Building with 3 elevators from floors 1 to 10

# Running elevators in the building
building.run_elevator(1, 5)  # Run elevator 1 to floor 5
building.run_elevator(2, 8)  # Run elevator 2 to floor 8
building.run_elevator(3, 3)  # Run elevator 3 to floor 3
