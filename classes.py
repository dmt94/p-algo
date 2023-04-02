class Car: # parent class
    # car_type = "Tesla"           class attribute
    def __init__(self, name, color, mileage):
        self.name = name         # instance attribute
        self.color = color
        self.mileage = mileage

    def run(self):
        return f"{self.name}: I am running!"
    
    def description(self):
        return f"I am a {self.color} car named {self.name}..."


Tesla = Car("Tesla", "red")
print(Tesla.run())

# Inheritance
# procedure, one class inherits the attributes and methods # of another class

class Audi(Car): #child class
    pass

class Bentley(Car):
    def description(self):
        return "I am a bentley!"

my_bentley = Bentley("Baby B", "red", 55.2)
print(my_bentley.description())


