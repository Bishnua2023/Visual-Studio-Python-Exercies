class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    
    def __str__(self):
        return f"Registration Number: {self.registration_number}\nMax Speed: {self.max_speed} km/h\nCurrent Speed: {self.current_speed} km/h\nTravelled Distance: {self.travelled_distance} km"
    
    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

# Creating an ElectricCar and a GasolineCar instance
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Selecting speeds for both cars
electric_car.current_speed = 120
gasoline_car.current_speed = 140

# Making both cars drive for three hours
electric_car.drive(3)
gasoline_car.drive(3)

# Printing the values of their kilometer counters
print("Electric Car Kilometer Counter:", electric_car.travelled_distance, "km")
print("Gasoline Car Kilometer Counter:", gasoline_car.travelled_distance, "km")