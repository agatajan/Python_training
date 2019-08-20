#
# #example
# # numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Declaring the tuple
# # count_odd = 0
# # count_even = 0
# # for x in numbers:
# #     if not x % 2:
# #         count_even += 1
# #     else:
# #         count_odd += 1
# # print("Number of even numbers :", count_even)
# # print("Number of odd numbers :", count_odd)
#
# ##################################################################################################################
#
# # zakres = list(range(1, 16))
# # print(zakres)
# # for liczba in zakres:
# #     if (liczba % 3 == 0) and (liczba % 5 == 0):
# #         print(liczba, "FizzBuzz")
# #     elif liczba % 3 == 0:
# #         print(liczba, 'Fizz')
# #     elif liczba % 5 == 0:
# #         print(liczba, "Buzz")
# #     else:
# #         print(liczba,"Not Division by 3 or 5")
#
# # 2 zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# # np kasiora - Opis slowa kasiora, w nowej linii nastepna para
# #
# # words_dict = {"Word1": "Definition of the word number one", "Word2": "Definition of the word number two", "Word3": "Definition of the word number three"}
# #
# # for key, value in words_dict.items():
# #     print(f"{key} - {value}\n")
#
# import pickle
#
# with open("words_dict.pckl", "rb") as file:
#     words_dict = pickle.load(file)
#
# question = input("Do you want to add new values to a dictionary? Please enter YES or NO: ")
#
# for x in question:
#     if x == 'YES':
#         key = input('Key: ')
#         value = input('Value: ')
#         words_dict[key] = value
#         print('The new values are now in a dictionary')
#     else:
#         print("The user doesn't want to add new values to a dictionary")
#
#
# with open ("words_dict.pckl", "wb") as file:
#
#
# pickle.dump(words_dict, file)

# osoby = {0: 'Ola', 1: 'Ala', 2: 'Ewa'}
# osoby.update({4: 'Ala'})
# print(osoby)

# wynik = 3
# a = ['ala', 'jeden', wynik]
# wynik = 43
# b = a.copy()
# a.append('ola')
#
# print(a)
# print(b)
#
# for i in range (0,99,33):
#     print (i)
#
# imie = "ola"
# def duza(imie='ala'):
#     imie = imie.capitalize()
#     return imie
#
# print(duza())
#
# imie = 'Joanna'
# print(imie[6])

# lista_a = [1, 2,‘trzy’4]
# # #lista_b = list('jeden', 'dwa', 3, 4) - bledna lista (fkcja list przyjmuje tylko jeden paranetr
# # #lista_c = lista_b[::-1]
# #
# # print(lista_a)

# indeks = 0
# for litera in 'Kotek':
#     print('Litera nr {} to {}'.format(indeks, litera))
#     break
#     indeks +=1
# print(indeks)

# try:
#     with open ('dane.csv', 'r+')as plik:
#         line = plik.readline()
#         print('To nie jest kod....')
# except FileNotFoundError:
#     print ('Nie prawda')
# except IOError:
#     print('Jednak nie mozna')
# finally:
#     print('Plik mozna')

# imie = 'Kamila'
#
# if imie[0].isupper() and not imie[-1].isupper():
#     print('Ala ma kota')
# elif imie == 'Kamila':
#     print('Kamila ma psa')
# else:
#     print('Pis i kot')

# nazwisko = 'Kowalski' #uwaga na przedzial otwarty - ostatnia litera sie nie liczy, wyprintuje 'oas'
# print(nazwisko[1:7:2])

# Jaka bedzie wartosc a
# a = 5
# b = 6
# a == 7
# b = 8
#
# print(a)
# imie = 'Joanna'
# print(imie[6])

#Jakim jezykiem jest Python
#W jakim systemie zapisywane sa dane na komputerze - binarnym
#Alorytm - skonczony zestaw infrukcji do wykonania zadnia

################Wynik:18/22 --> 82%##########################################

# i = 100
# while i >= 100:
#     print(i)
# i-= 1
# print(i)
#
# for i in range(0, 99, 33):
#     print(i)

# grupa = ['mlody', 'sredni', 'dojrzaly']
# # # wiek = 30
# # #
# # # if wiek < 30:
# # #     grupa_osoby = grupa[0]
# # # elif 30<=wiek<60:
# # #     grupa_osoby = grupa[1]
# # # else:
# # #     grupa_osoby = grupa[2]
# # #
# # # print(grupa_osoby)

# grupa = ['mlody', 'sredni', 'dojrzaly']
# wiek = 30
#
# def okresl_grupa():
#     if wiek < 30:
#         grupa_osoby = grupa[0]
#     elif 30<=wiek<60:
#         grupa_osoby = grupa[1]
#     else:
#         grupa_osoby = grupa[2]
#
# okresl_grupa(wiek)
# print(grupa_osoby)

# class Zwierz(object):
#     def mow(self):
#         print('Jestem Zwierz')
#
# class Orka(Zwierz):
#     def mow(self):
#         print('Jestem orka')
#
# class Dellfin(Zwierz):
#     def mow(self):
#         print('Jestem delfin')
#
# class Orkin(Orka, Dellfin):
#     pass
#
# x = Orkin()
# x.mow()

# class Samochod(object):
#     def __init__(self, marka, kolor):
#         self.producent = marka
#         self.kolor = kolor
#
# auto1 = Samochod('Volvo','czarny')
# auto1.model = 'XC60'
#
# print(auto1.model)

