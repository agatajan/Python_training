# 4. Napisz funkcję, która przyjmuje dowolną ilość parametrów - zaloz ze beda podawane liczbowe, funkcja ma wypisywac te parametry, uzywajac petli for in

# def arguments(*args):
#     for a in args:
#       print(a)
#
# (arguments(1,5,8,6,9,112))

# 5. Zmodyfikuj funkcje z zadania wyzej tak, aby na koncu wypisala sume liczb podanych do funckji
#
# def sum_arguments(*args):
#     sum = 0
#
#     for a in args:
#       sum += a
#       print(a)
#
#     print(sum)
#
# sum_arguments(1, 2, 3, 4, 10)

# 6. Inside - out - napisz dwie funckje - dodawanie (np o nazwie add) oraz mnozenie dwoch liczb (np o nazwie multiply), nastapnie wywolaj operację
# multiply(add(2, 6), 2)

# def add(number1, number2):
#   return number1 + number2
#
# def multiply(number1, number2):
#   return number1 * number2
#
#
# print(add(1, 2))
# print(multiply(3, 5))
# print(multiply(add(2, 6), 2))

# 7. Napisz funkcję rozbijajaca zdanie na slowa (ma zwracac liste ze slowami) oraz funkcje sortujaca liste slow, nastepnie wywolaj sortowanie na slowach podanego przez uzytkownika zdania
#sort_words(split_sentence_to_words(sentence))

#solution1 --> split_to_words
# def split_to_words(sentence):
#     words = sentence.split(" ")
#     for word in words:
#         print(word)
#
# split_to_words("ala ma kota")

#solution2
# def split_to_words(sentence):
#   return sentence.split(" ")
#
# #print(split_to_words("Napisz funkcje rozbijajaca zdanie na slowa"))
#
# def sort_words(list_of_words):
#   return list_of_words.sort()
#
# sentence = "Napisz funkcje rozbijajaca zdanie na slowa"
#
# words = split_to_words(sentence)
# sort_words(words)
# print(words)
