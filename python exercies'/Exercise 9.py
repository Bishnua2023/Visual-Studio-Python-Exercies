class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return f"Registration Number: {self.registration_number}\nMax Speed: {self.max_speed} km/h\nCurrent Speed: {self.current_speed} km/h\nTravelled Distance: {self.travelled_distance} km"


# Creating a new car
new_car = Car("ABC-123", 142)

# Printing out all properties of the new car
print(new_car)
