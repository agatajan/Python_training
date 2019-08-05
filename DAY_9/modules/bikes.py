bike_types = {"cross": "Cross bicykle", "road": "Road bicykle"}

#dodajemy domyslne wartosci: kierownica-handlerbar, siodelko-seat
#czesc obiektow nie zostanie przeazana - back whhel, fron wheel, frame, ale chcmemy je zapisac
#dobrze jest tworzyc dokumentacje

#DZIEDZICZENIE
#class ElectricBike(Bike)


class Bike(object):
    def __init__(self, color, type, front_wheel, back_wheel, frame, handlebar = "fitness", seat = "classic, stock, seat"):
        self.handlebar = handlebar
        self.seat = seat
        self.color = color
        self.type = type
        self.front_wheel = front_wheel
        self.back_wheel = back_wheel
        self.frame = frame

    def ride(self):
        """Ride this bike"""
        print(f"I'm riding {self.color} bike")

    def ring_bell(self):
        print(f"Riding on {self.color} bike its ringing a bell")

# #dziedziczenie --> rower elekrtyczny , ktory dziedziczy wszystkie cechy z Bike
class ElectricBike(Bike):

    def ring_bell(self):
        print("cos cos cos")

    def increase_motor_power(self):
        print("Motor power increased!")

class Wheel(object):
    def __init__(self, size, color):
        self.size = size
        self.color = color

class Frame(object):
    def __init__(self, size, color, geometry):
        self.size = size
        self.color = color
        self.geometry = geometry