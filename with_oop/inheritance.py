


class Device:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        print(f"{self.brand} device is running.")




class Laptop(Device):
    def __init__(self, memory, ssd):
        super().__init__()
        self.memory = memory
        self.ssd = ssd


class Phone:
    def __init__(self, memory):
        self.memory = memory

    def ___repr__(self):
        return f"Phone(brand={self.brand}, price={self.price}, color={self.color}, memory={self.memory})"


    def call(self):
        print(f"{self.brand} phone is making a call.")


class Camera:
    def __init__(self, resolution):
        self.resolution = resolution


    def take_photo(self):
        print(f"{self.brand} camera is taking a photo.")




my_phone = Phone("Samsung", 500, "Black", "128GB")
print(my_phone)