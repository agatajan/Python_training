from DAY_9.modules.employee import Employee
#from DAY_9.modules.bikes import bike_types, Bike, Frame, Wheel
from DAY_9.modules.bikes import bike_types, Bike, Frame, Wheel, ElectricBike

# #wersja podstowa nr 1
# new_employee = Employee("Mateusz", "Cebula")
# another_new_employee = Employee("Jan")
# another_new_employee.say_hello()

#wersja nr 2 --. dodane salary
new_employee = Employee("Mateusz", 2000, "Cebula")
new_employee.increase_salary(25)
print(new_employee.salary)

######################################################################################################
front_wheel = Wheel(28, "black")
back_wheel = Wheel(28, "black")
frame = Frame(19, "red", "sport")

#ctr + spacja - do podejrzenia wartosci w slowniku
#ctr + p - pokazuje parametry
#ctrl + najezdzamy np. na Bike - przeniesie nas do definicji
bike = Bike ("red", bike_types["cross"], front_wheel, back_wheel, frame)


# dopisana ElectricBike do importu - inaczej nie widzi nowej definicji
electric_bike = ElectricBike("red", bike_types["cross"], front_wheel, back_wheel, frame)

#zwkly pront nie wyprintuje wyniku, python nie wie jak to wypisac
#print(bike)

print(bike.handlebar)

#metoda ride, ring_bell - rozszerzamy o kolejne metody
bike.ride()
bike.ring_bell()

#wywolanie electric bike - nowe definicje
electric_bike.ring_bell()

######################################################################################################