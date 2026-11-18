class Vehicle:
    def __init__(self, maximum_speed, mileage):
        self.maximum_speed = maximum_speed
        self.mileage = mileage

Ferrari = Vehicle(280,15)
Bmw = Vehicle(200, 24)
print("The top speed of the Ferrari is",Ferrari.maximum_speed)
print("The mileage of the Ferrari is", Ferrari.mileage)
print("The top speed of the BMW is",Bmw.maximum_speed)