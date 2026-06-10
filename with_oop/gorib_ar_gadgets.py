class Laptop:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        print(f"{self.brand} laptop is running.")


class Phone:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        print(f"{self.brand} phone is running.")

    def call(self):
        print(f"{self.brand} phone is making a call.")


class Camera:
    def __init__(self, brand, price, color, resolution):
        self.brand = brand
        self.price = price
        self.color = color
        self.resolution = resolution

    def run(self):
        print(f"{self.brand} camera is running.")

    def take_photo(self):
        print(f"{self.brand} camera is taking a photo.")