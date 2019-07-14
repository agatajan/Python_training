# #zakres zmiennych
#
# imie = "Jola"
# def zmien_imie():
#     imie = "Teresa"
#
# print(imie)
# print(zmien_imie())
#

# #docstring --> printuje dokumentacje
def give_square(x):
    """Return square of given number

    (number) -> number
    """
    return x ** 2

print(give_square.__doc__)

# zadanie1 --> napisz funkcję sumująca wszystkie elementy w liscie

def sum_list(list_of_numbers):
    """
    Return list of numbers from given
    number list (integers)
    :param list_of_numbers:
    :return: sum_of_list
    (list) --> int
    """
    suma = 0
    for number in list_of_numbers:
        suma = suma + number

    return suma

print(sum_list([11,2,3]))
print(sum_list.__doc__)

# zadanie2 --> znajdz najwiekszy / najmniejszy element w liscie - napisz dwie funkcje
# 2 sposoby - najpierw ręcznie, następnie sprytnie

# lista = [6,2,56,9,7,36,36,10,125,12]

#1sposob_max_min
def min_list_number(list_of_numbers):
    copy_list = list_of_numbers[:]
    copy_list.sort()
    return copy_list[0]

def max_list_number(list_of_numbers):
    copy_list = list_of_numbers[:]
    copy_list.sort()
    return copy_list[-1]

print(min_list_number(lista))
print(max_list_number(lista))

#2sposob_max_min
def min_number(list_of_numbers):
    smallest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if smallest_number > number:
            smallest_number = number

    return smallest_number

def max_number(list_of_numbers):
    highest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if highest_number < number:
            highest_number = number

    return highest_number

print(min_number(lista))
print(max_number(lista))


# zadanie3 --> funkcja ktory zmieni zdanie w liste wyrazow

# zdanie = "Ala ma kota, kot ma Ale"

def split_to_words(sentence):
    return sentence.split(" ")

print(split_to_words(zdanie))

#zadanie4
# napisz funckję przyjmujaca liste stringow,
# a zwracakaca liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2
#na wyjciu bedzie integer
#najpierw nalzey przejrzec wszystkie stringi - for
#count() --????
#
# def how_many_valid_strings(list_of_strings):
#     counter = 0
#
#     for word in list_of_strings:
#         if len(word) == 2 and word[0] == word[-1]:
#             counter +=1
#
#     return counter
#
# print(how_many_valid_strings(['aba', 'sdsda', '12221', 'bbbbb']))


#copy
def how_many_valid_strings(list_of_strings):
   counter = 0

   for word in list_of_strings:
       if (len(word) >= 2 and word[0] == word[-1]):
           counter += 1

   return counter

print(how_many_valid_strings(['aba', 'sdsda', '12221', 'bbbbb']))

# program znajdujacy wartosci, ktre wystepuja tylko raz
#lista_a = [10,20,30,20,10,50,60,40,80,50,40]
# 1.przegladam liste - polecenie for
# 2. sprawdzam ile razy ma wystepowac - tu raz (metoda count)
# 4. jesli sie pojawia raz to wrzucam go na kontener, pozniej pojawi sie to w liscie
# 3. musimy stworzyc pusta liste, do ktorej bedziemy dokladac kolejne elementy (deklaracja kontenera, w ktorym pojawia sie kolejne elementy)

def get_numbers_occured_once(list_of_numbers):
   list_of_valid_numbers = []

   for number in list_of_numbers:
       if list_of_numbers.count(number) == 1:
           list_of_valid_numbers.append(number)

   return list_of_valid_numbers


lista_a = [10,20,30,20,10,50,60,40,80,50,40]
print(get_numbers_occured_once(lista_a))

# zadanie wybierz losowo element z listy
# wskazowka - import random

"""
import random
for x in range(10):
  print(random.randint(1,101))
"""

# #from random import *
# import random
# def random_number():
#     number = random()
#     return number
#
# print(random_number)


# #slownik1
# simple_dict = {1: "jeden", 2: "dwa"}
# for key, value in simple_dict.items():
#     print(f"pod kluczem {key} jest wartosc: {value}")
#
# #podmienia wartosc w slowniku - na drugiej pozycji
# simple_dict[1] = "trzy"
#
# for key, value in simple_dict.items():
#     print(f"pod kluczem {key} jest wartosc: {value}")

#slownik2
#
# movie_dict = {1999: "Film numer 1", 2000: "Film numer 2", 2001: "Film numer 2"}
# for key, value in movie_dict.items():
#     print(f"W roku {key} powstal: {value}")

