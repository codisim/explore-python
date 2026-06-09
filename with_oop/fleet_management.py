class Company:
    def __init__(self, name, address):
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counters = []
        self.managers = []
        self.supervisors = []
        self.fares = []


class Driver:
    def __init__(self, name, age, license):
        self.name = name
        self.age = age
        self.license = license

class Counter:
    def __init__(self):
        pass

    def purchase_ticket(self, start, distination):
        pass


        