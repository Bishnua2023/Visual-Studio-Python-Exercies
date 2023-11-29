import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    
    def accelerate(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(new_speed, self.max_speed))
    
    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)  # Each car drives for one hour

    def print_status(self):
        print(f"Race: {self.name} - Distance: {self.distance} km")
        print("| Registration | Max Speed | Current Speed | Travelled Distance |")
        print("-" * 63)
        for car in self.cars:
            print(f"| {car.registration_number:<13} | {car.max_speed:>9} km/h | {car.current_speed:>13} km/h | {car.travelled_distance:>18} km |")
        print("-" * 63)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


# Creating cars for the race
cars_for_race = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

# Creating the race
grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars_for_race)

# Simulating the race progression
hour = 0
while not grand_demolition_derby.race_finished():
    if hour % 10 == 0:
        grand_demolition_derby.print_status()
    grand_demolition_derby.hour_passes()
    hour += 1

# Printing final status at the end of the race
grand_demolition_derby.print_status()
