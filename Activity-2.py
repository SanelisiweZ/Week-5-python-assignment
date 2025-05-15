class Vehicle:
    def move(self):
        print("This vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚢")

# Function that uses polymorphism
def travel(vehicle):
    vehicle.move()

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    travel(v)
