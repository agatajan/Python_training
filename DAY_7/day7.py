import os

#printuje liste plikow w katalogu
#print(os.listdir())

#os.path.isdir()
#os.path.isfile()

#sprawdzamy co jest plikiem, a co katalogiem


#do pracy na liscie najlepiej wykorzystac petle for
#definiujemy pusta liste
#solution1
# list = os.listdir()
#
# for item in list:
#     if os.path.isfile(item):
#         print(f"Pliki: {item}")
#     elif os.path.isdir(item):
#         print(f"Katalogi: {item}")

# #solution2 - tu przy pustej liscie nie wyprintuje wyniku
# list = []
#
# #sprawdzenie czy lista nie jest pusta - spraedzamy najpierw pierwszy element z listy, ale:
# #dla pierwszego if wurzuci blad - nie moze sprawdzic pierwszego ideksu na pustej liscie: list []
# if (list[0] is not None):
#     print('Error')
#     exit()
#
# for item in list:
#     if os.path.isfile(item):
#         print(f"Pliki: {item}")
#     elif os.path.isdir(item):
#         print(f"Katalogi: {item}")

# solution3 - tu przy pustej liscie nie wyprintuje wyniku
# list = []
#
# # sprawdzenie czy lista nie jest pusta - spraedzamy najpierw pierwszy element z listy, ale:
# #lapanie wyjatkow od szczegolu do ogolu
# try:
#     list[0]
# except IndexError:
#     print('Katalog jest pusty')
#     exit()
#
# for item in list:
#     if os.path.isfile(item):
#         print(f"Pliki: {item}")
#     elif os.path.isdir(item):
#         print(f"Katalogi: {item}")

# #solution4 - dla przypaku kiedy mamy jakis element w liscie
# #sprawdzanie pustej listy przy pomocy try/ecept
#
# list = ['test']
#
# try:
#     list[0]
#     wynik = 10 / 0
# except IndexError:
#     print('Katalog jest pusty')
#     exit()
# except ZeroDivisionError:
#     print('Nie dziel przez zero')
#     exit()
# except:
#     print('Nieznany mi blad')
#     exit()
#
#
# for item in list:
#     if os.path.isfile(item):
#         print(f"Pliki: {item}")
#     elif os.path.isdir(item):
#         print(f"Katalogi: {item}")

#solution5 - z wykorzystaniem if

# list = []
#
# if not list:
#     print('Katalog jest pusty')

#solution6 - z wykorzystaniem if

# list = []
# #not sparwdza czy istnieje zmienna i czy ma jakas zawartosc
# #3 sposoby sprawdzenia czy lista jest pusta
# if len(list) == 0:
#     print('Katalog jest pusty 1')
#
# if not list:
#     print('Katalog jest pusty 2')
#
# if list is False:
#     print('Katalog jest pusty 2')


#ostateczna wersja sprawdzania co jest plikiem/katalogiem:
# import os
#
# list = os.listdir()
#
# if len(list) == 0:
#     print('Katalog jest pusty 1')
#
# for item in list:
#     if os.path.isfile(item):
#         print(f"Pliki: {item}")
#     elif os.path.isdir(item):
#         print(f"Katalogi: {item}")

# dokladamy funkcje do modulu:
# tu wystarczy zdefiniowac funkcje def show_dir() + zrobic wciecia TABem

import os

def show_dir():

    list = os.listdir()

    if len(list) == 0:
        print('Katalog jest pusty 1')
    for item in list:
        if os.path.isfile(item):
            print(f"Pliki: {item}")
        elif os.path.isdir(item):
            print(f"Katalogi: {item}")

#ze zmienna, ktora jest lista
#tworzymy pusta liste/pustego stringa
import os

def show_dir():

    list = os.listdir()

    if len(list) == 0:
        return 'Katalog jest pusty 1'

    x = []

    for item in list:
        if os.path.isfile(item):
            x.append(f"Pliki: {item}")
        elif os.path.isdir(item):
            x.append(f"Katalogi: {item}")
    return x
##############################################################333
import os

def show_dir():

    list = os.listdir()

    if len(list) == 0:
        return 'Katalog jest pusty 1'

    new_list = ''

    for item in list:
        if os.path.isfile(item):
            new_list += f"Pliki: {item}\n"
        elif os.path.isdir(item):
            new_list += f"Katalogi: {item}\n"
    return new_list