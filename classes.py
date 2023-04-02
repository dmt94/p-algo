class Car:
    # car_type = "Tesla"           class attribute
    def __init__(self, name, color):
        self.name = name         # instance attribute
        self.color = color

    def run(self):
        return f"{self.name}: I am running!"

Tesla = Car("Tesla", "red")
print(Tesla.run())