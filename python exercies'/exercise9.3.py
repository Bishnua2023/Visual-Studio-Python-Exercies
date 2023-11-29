class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    
    def __str__(self):
        return f"Registration Number: {self.registration_number}\nMax Speed: {self.max_speed} km/h\nCurrent Speed: {self.current_speed} km/h\nTravelled Distance: {self.travelled_distance} km"
    
    def accelerate(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(new_speed, self.max_speed))
    
    def drive(self, hours):
        # Calculate distance traveled at constant speed
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

# Creating a new car
new_car = Car("ABC-123", 142)

# Increasing the speed by +30 km/h, +70 km/h, and +50 km/h
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

# Printing out the current speed of the car
print("Current Speed after acceleration:", new_car.current_speed, "km/h")

# Using emergency brake (-200 km/h change)
new_car.accelerate(-200)

# Printing out the final speed after applying emergency brake
print("Speed after emergency brake:", new_car.current_speed, "km/h")

# Driving for 1.5 hours
new_car.drive(1.5)

# Printing out the updated travelled distance
print("Travelled Distance after driving:", new_car.travelled_distance, "km")
