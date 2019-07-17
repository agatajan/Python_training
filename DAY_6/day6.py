rekordy = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
{"imie": "Anna", "nazwisko":"nowak", "wiek":23},
{"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
{"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]
#
# dict_of_person = {}
#
# for indeks, rekord in enumerate(rekordy):
#     print (f"Pod indeksem {indeks} rekord: {rekordy}")
#     dict_of_person[indeks+1001] = rekord
#
# print(dict_of_person)
################################################################################################################
#tworzymy pusty slownik
#tworzymy dwa slowniki 1999 i 2000
#do pierwszego slownika dopisujemy nowa wartosc tu: Film numer 4

# #
# movie_dict = {}
# movie_dict[1999] = ["Film numer 1", "Film numer 2"]
# movie_dict[2000] = ["Film numer 3"]
#
# movie_dict[1999].append("Film numer 4")
# #zeby dodac wiecej niz jeden element korzystajac z append mozemy stworzyc liste i dodac nieskonczona ilosc elementow
# #movie_dict[1999].append(["Film numer 4", "aaaaa"])
#
# for key, value in movie_dict.items():
#     print(f"W roku {key} powstal: {value}")
#
# #printujemy klucz i wartosci ze slownika z enterem i wcieciami (tabulatory)
# for key, value in movie_dict.items():
#     print(f"{key}\n\t{value}")



# sciezka = "text1.txt"
#
# # otwieramy plik w trybie tekstowym, tylko do odczytu
# plik = open(sciezka, 'r')
#
# # read() czyta zawartość, od miejsca w któym jest kursor
# # aż do kocńa pliku
# tresc = plik.read()
# print(tresc)
#
# # pamiętać o zamykaniu pliku
# plik.close()

#
# sciezka = "text1.txt"
#
# with open(sciezka, 'a') as plik:
#     print(plik.tell())
#
#     plik.write("\nMoja kolejna linijka")

# sciezka = "text1.txt"
#
# tekst = """To jest mój tekst. To
# jest kolejna linijka tekstu,
#         a to kolejna."""
#
# with open(sciezka, 'r+') as plik:
#     print(plik.tell())
#     # # plik.write(tekst)
#     plik.seek(0)
#     print(plik.read())
################################################################################################################
# sciezka = "text1.txt"
#
# tekst = "Ten tekst jest zawsze w nowej linii"
# with open(sciezka, "r+") as plik:
#     # print(plik.tell())
#     # idziemy kursorem na koniec pliku
#     plik.read()
#
#     # bierzemy numer ostatniej pozycji
#     # i cofamy kursor na przedostatnią pozycję
#     pozycja = plik.tell()
#     plik.seek(pozycja - 1)
#
#     # odczytujemy ostatni znak
#     ostatni_znak = plik.read()
#     print(ostatni_znak)
#
#     # teraz wiemy, że jeśli ostatni znak nie jest znakiem nowej linii
#     # to w pliku nie ma na końcu pustego wiersza
#     if ostatni_znak != '\n':
#         plik.write('\n' + tekst + '\n')
#     # a tu był znak nowej linii, czyli plik miał pusty wiersz
#     else:
#         plik.write(tekst + '\n')

################################################################################################################

#otworz i zapisz do pliku filmy - kazdy film  w nowym wierszu (linijce pliku)
#1
list_of_movies = ["Film1", "Film2","Film3", "Film4"]

with open("movie.txt", "w") as file:
    for movie in list_of_movies:
        file.write(movie + '\n')

#2
# movie_dict = {}
# movie_dict[1999] = ["Film numer 1", "Film numer 2"]
# movie_dict[2000] = ["Film numer 3"]
#
# movie_dict[1999].append("Film numer 4")
#
# with open("movie_new.txt", "w") as file:
#     for key, value in movie_dict.items():
#         print(key)
#         for movie in value:
#             print(f"\t{movie}")

3
# movie_dict = {}
# movie_dict[1999] = ["Film numer 1", "Film numer 2"]
# movie_dict[2000] = ["Film numer 3"]
#
# #movie_dict[1999].append("Film numer 4")
#
# with open("movie_new.txt", "w") as file:
#     for key, value in movie_dict.items():
#         file.write(str(key) + "\n")
#         for movie in value:
#             file.write(f"\t{movie}\n")
#             # for movie in value:
#             #     file.write(f"{key}\n\t{value}\n")

# with open("D:\!_Python_trainig\scripts_IS\movies.txt", "w") as plik:
#    for key, value in movies_dict.items():
#        plik.write(str(key) + "\n")
#        for movie in value:
#            plik.write(f"\t{movie}\n")

# for key, value in movie_dict.items():
#     print(f"{key}\n\t{value}")

#piszemy tam gdzie moze wystapic wyjatek
try:
    #zmienna = 0/2
    zmienna = 1/2
    print("jjdsjds")
except ZeroDivisionZero:
    print("Wystapil blad dzielenia przez zero")
else:
    print("Nie wystapil wyjatek")
finally:
    print("Zakonczenie programu ....... ;)")