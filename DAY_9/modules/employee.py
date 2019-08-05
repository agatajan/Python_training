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


