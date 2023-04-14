class Bus:
    def __init__(self, speeds, maxkol, maxSpeeds, passajirs, svobodapopugaem, seats):
        self.speeds = speeds
        self.maxkol = maxkol
        self.maxSpeeds = maxSpeeds
        self.passajirs = passajirs
        self.svobodapopugaem = svobodapopugaem
        self.seats = seats

    def add_passenger(self, name):
        if len(self.passajirs) < self.maxkol:
            self.passajirs.append(name)
            print(f"{name} has been added to the bus.")
        else:
            print("The bus is full.")

    def remove_passenger(self, name):
        if name in self.passajirs:
            self.passajirs.remove(name)
            print(f"{name} has been removed from the bus.")
        else:
            print(f"{name} is not on the bus.")

    def increase_speed(self, speed):
        if (self.speeds + speed) <= self.maxSpeeds:
            self.speeds += speed
            print(f"The speed has been increased by {speed}.")
        else:
            print("The maximum speed has been reached.")

    def decrease_speed(self, speed):
        if (self.speeds - speed) >= 0:
            self.speeds -= speed
            print(f"The speed has been decreased by {speed}.")
        else:
            print("The minimum speed has been reached.")

    def __contains__(self, name):
        return name in self.passajirs

    def __iadd__(self, name):
        if len(self.passajirs) < self.maxkol:
            self.passajirs.append(name)
            print(f"{name} has been added to the bus.")
        else:
            print("The bus is full.")
        return self

    def __isub__(self, name):
        if name in self.passajirs:
            self.passajirs.remove(name)
            print(f"{name} has been removed from the bus.")
        else:
            print(f"{name} is not on the bus.")
        return self

bus = Bus(50, 20, 100, [], True, {"1A": None, "1B": None})
bus.add_passenger("John")
bus.add_passenger("Jane")
bus.add_passenger("Bob")
bus.remove_passenger("John")
bus.increase_speed(20)
bus.decrease_speed(10)
print("Bob" in bus)