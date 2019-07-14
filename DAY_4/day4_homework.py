# # 3. Napisz funkcje, ktora rozbije zdanie na slowa i kazde z nich wypisze w nowej linii (bedzie potrzebna petla for in)
#
# def split_to_words(sentence):
#     words = sentence.split(" ")
#     for word in words:
#         print(word)
#
# split_to_words("ala ma kota hhh")
#
#
# # #rozbija zdanie do listy
# def split_to_words(sentence):
#     return sentence.split(" ")
#
# print(split_to_words("ala ma kota"))
#
# # 4. Napisz funkcję, która przyjmuje dowolną ilość parametrów - zaloz ze beda podawane liczbowe, funkcja ma wypisywac te parametry, uzywajac petli for in
#
# def var_arg(*args):
#     for a in args:
#         print (a)
#
# var_arg(1,2,8,55,99,2,113,587)

# 5. Zmodyfikuj funkcje z zadania wyzej tak, aby na koncu wypisala sume liczb podanych do funckji

def var_arg_sum(*args):
    sum = 0
    for a in args:
        sum += a
    print(a)

var_arg_sum(1,2,8,55,99,2,113,587)