#FUNKCJE

#fkcja1
# def dodaj(x,y):
#     suma = x + y
#     return suma
#
# wynik = dodaj(2,3)
#
# print(wynik)

# 2. Napisz funkcję, powtarzającą słowo x razy (2 parametry - slowo oraz ile razy powtorzyc)
# (bedzie potrzebna petla for in oraz klasa range)

# def repeat_n_times (word, times_to_repeat):
#     for i in range(times_to_repeat):
#        # return (word) - zwraca jeden wynik funcji
#        # print(word) - jesli chcemy wyprintowac wynik wiele razy
#
#
# result = repeat_n_times('test',5)
# print(result)

#fkcja 3

def split_sentence_to_words(sentence):
    return sentence.split(" ")

print(split_sentence_to_words("Python Day Four"))