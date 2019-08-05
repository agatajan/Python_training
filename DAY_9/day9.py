#1. wersja podstawowa
bike_types = {"cross": "Cross bicykle", "road": "Road bicykle"}

#dodajemy domyslne wartosci: kierownica-handlerbar, siodelko-seat
#czesc obiektow nie zostanie przeazana - back whhel, fron wheel, frame, ale chcmemy je zapisac
#dobrze jest tworzyc dokumentacje

class Bike(object):
    def __init__(self, color, type, front_wheel, back_wheel, frame, handlebar = "fitness", seat = "classic, stock, seat"):
        self.handlebar = handlebar
        self.seat = seat
        self.color = color
        self.type = type
        self.front_wheel = front_wheel
        self.back_wheel = back_wheel
        self.frame = frame

class Wheel(object):
    def __init__(self, size, color):
        self.size = size
        self.color = color

class Frame(object):
    def __init__(self, size, color, geometry):
        self.size = size
        self.color = color
        self.geometry = geometry


#2. co robi rower ???? -edytujemy modul - dodajemy metody ride, ring_bell

bike_types = {"cross": "Cross bicykle", "road": "Road bicykle"}

#dodajemy domyslne wartosci: kierownica-handlerbar, siodelko-seat
#czesc obiektow nie zostanie przeazana - back whhel, fron wheel, frame, ale chcmemy je zapisac
#dobrze jest tworzyc dokumentacje

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

class Wheel(object):
    def __init__(self, size, color):
        self.size = size
        self.color = color

class Frame(object):
    def __init__(self, size, color, geometry):
        self.size = size
        self.color = color
        self.geometry = geometry


#1. empl wersja podstawowa

class Employee(object):
    """creates new Employee"""
    def __init__(self, imie, nazwisko = "Kowalski"):
        self.name = imie
        self.surname = nazwisko

    def say_hello(self):
        """Say Hello"""
        print(f"Hello, My name is {self.name} {self.surname}")

#2. dodajemy pensje i dajemy podwyzke

class Employee(object):
    """creates new Employee"""
    def __init__(self, imie, salary, nazwisko = "Kowalski"):
        self.name = imie
        self.surname = nazwisko
        self.salary = salary

    def say_hello(self):
        """Say Hello"""
        print(f"Hello, My name is {self.name} {self.surname}")

    def increase_salary(self, percentage):
        """increase salary"""
        self.salary = (1 + percentage / 100) * self.salary