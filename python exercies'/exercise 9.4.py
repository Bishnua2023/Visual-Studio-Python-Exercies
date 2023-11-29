import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    
    def __str__(self):
        return f"| {self.registration_number:<8} | {self.max_speed:>10} km/h | {self.current_speed:>13} km/h | {self.travelled_distance:>16} km |"

    def accelerate(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(new_speed, self.max_speed))
    
    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

# Function to create a list of cars
def create_cars(num_cars):
    cars = []
    for i in range(1, num_cars + 1):
        registration_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(registration_number, max_speed)
        cars.append(car)
    return cars

# Create 10 cars
cars = create_cars(10)

# Start the race
race_complete = False
hours_elapsed = 0

while not race_complete:
    # Increment hours
    hours_elapsed += 1
    
    # Update each car's  between -10 km/h and +15 km/h
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        
        car.drive(1)  # Each car drives for one hour
    
    # Check if any car travelled 10,000 km
    for car in cars:
        if car.travelled_distance >= 10000:
            race_complete = True
            break

print("| Registration | Max Speed | Current Speed | Travelled Distance |")
print("-" * 63)
for car in cars:
    print(car)
