# 1 stwórz słownik, którego kluczem będą słowa, natomiast wartością znaczenie tych słów
#
# words_dict = {"Word1": "Definition of the word number one", "Word2": "Definition of the word number two", "Word3": "Definition of the word number three"}
#
# for key, value in words_dict.items():
#     print(f"Pod slowem {key} jest definicja: {value}")
#
###################################################################################################################
#
# 2 zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# np kasiora - Opis slowa kasiora, w nowej linii nastepna para
#
# words_dict = {"Word1": "Definition of the word number one", "Word2": "Definition of the word number two", "Word3": "Definition of the word number three"}
#
# with open("words.txt", "w") as file:
#     for key, value in words_dict.items():
#         file.write(f"{key} - {value}\n")
#
####################################################################################################################
#
# 3 zapisz slownik slangu miejskiego do pliku csv, gdzie klucz (slowo) i wartosc (wyjasnienie slowa)
# beda oddzielone pionową linią pipe (|) - przyklad zapisu pliku csv w Day6\exercises\cs_example
#
# words_dict = {"Word1": "Definition of the word number one", "Word2": "Definition of the word number two", "Word3": "Definition of the word number three"}
#
# import csv
#
# with open("words.csv", newline='', mode="w") as csvfile:
#     writer = csv.writer(csvfile, delimiter="|")
#     for key, value in words_dict.items():
#         writer.writerow([key, value])
#
###################################################################################################################
#
# 4 zapisz slownik slangu miejskiego jako pickle - przyklad w Day6\exercises\pickle_1.py
# odczytaj plik i sprawdz czy poprawnie zapisano dane
#
# import pickle
#
# words_dict = {"Word1": "Definition of the word number one", "Word2": "Definition of the word number two", "Word3": "Definition of the word number three"}
#
# #zapisujemy caly slownik
# with open ("words_dict.pckl", "wb") as file:
#     pickle.dump(words_dict, file)
#
# # otwieramy slownik
# read_words_dict = None
#
# with open ("words_dict.pckl", "rb") as file:
#     read_words_dict = pickle.load(file)
#
# print(read_words_dict)
#
###################################################################################################################
#
# 5 odczytaj plik article.txt w calosci - plik umieszczony w Day5\exercises\article.txt
# pozwol uzytkownikowi na podanie slowa i policz ile razy dane slowo wystepuje w artykule
# (powiedz uzytkownikowi ile razy wystepuje)
#
# word = input("The word is: ")
# words_count = 0
#
# with open ("article.txt", "r") as file:
#     article_content = file.read()
#     print(article_content)
#     if word in article_content:
#         words_count = article_content.count(word)
#         print(words_count)
#     print(f"The word: '{word}' appears in that file {words_count} time(s).")

# 6 utwórz program, w ktorym uzytkownik bedzie mogl powiekszac baze slow slangu miejskiego
# na poczatku programu zaladuj slownik z pliku pickle
# (sprawdz czy plik istnieje, albo po wykonaniu zadania 4 uzyj istniejacego pliku)
# napisz program tak, aby uzytkownik mogl dodawac slowa i ich wyjasnienie, dopoki nie zechce wyjsc z programu
# (moze byc krotkie pytanie czy chcesz dodac slowo do slownika? TAK/NIE)
# na koncu programu zapisz slownik ponownie do pliku pickle, aby zapisac zmiany
#
# import pickle
#
# with open("words_dict.pckl", "rb") as file:
#     words_dict = pickle.load(file)
#
# question = input("Do you want to add new values to a dictionary? Please enter YES or NO: ")
#
# if question == 'YES':
#     key = input('Key: ')
#     value = input('Value: ')
#     words_dict[key] = value
#     print('The new values are now in a dictionary')
# else:
#     print("The user doesn't want to add new values to a dictionary")
#
#
# with open ("words_dict.pckl", "wb") as file:
#     pickle.dump(words_dict, file)