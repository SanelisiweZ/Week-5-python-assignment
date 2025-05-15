# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I use {self.power}!")

# Inherited class
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h! ✈️")

# Inherited class
class StrengthHero(Superhero):
    def __init__(self, name, power, origin, lift_capacity):
        super().__init__(name, power, origin)
        self.lift_capacity = lift_capacity

    def lift(self):
        print(f"{self.name} can lift {self.lift_capacity} tons! 💪")

# Test the classes
hero1 = FlyingHero("SkyBlaze", "Wind Control", "Sky City", 800)
hero2 = StrengthHero("Titan", "Super Strength", "Earth Base", 100)

hero1.introduce()
hero1.fly()

hero2.introduce()
hero2.lift()




