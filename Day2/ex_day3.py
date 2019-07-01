
#1 wypisz co druga literę z napisu - uzyj petli for:
# text = "Python is a fantastic snake"
# # for x in text:
# #     print(text[::2])
# #     break

# 1.1 wypisz co druga literę
# text = "Python is a fantastic snake"
# print(text[::2])

# 1.2 wypisz teraz co trzecią literę
# text = "Python is a fantastic snake"
# print(text[::3])

# 2 wyszukaj w dokumentacji jak rozbić powyższy tekst na listę słów a nastepnie wydrukuj ta liste (for slowo in lista)
# text = "Python is a fantastic snake"
# words = text.split()
#
# for i in words:
#     print(i)

# #cwiczenie
# text = "Python is a fantastic snake"
# how_many_chars = len(text)
#
# list_of_indexes = range(0,how_many_chars,2)
#
# for idx in list_of_indexes:
#     print(text[idx], end="")

# #enumerate
# months = ["Jan", "Feb", "March"]
# for index, value in enumerate(months):
#     print(f"Na indeksie {index} znajduje sie {value}")

# 3 zmien program z punktu drugiego tak, aby uzytkownik sam wpisal jakis tekst, ktory program mu rozbije na liste slow
text = input("Wpisz zdanie: ")
words = text.split()

for i in words:
    print(i)