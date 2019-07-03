# old_number = 4
# new_number = old_number
# old_number = 6
#
# print(old_number)
# print(new_number)

# old_list = [1,2,3,]
# new_list = old_list
#
# old_list[0] = 4
# #old_list[1] = 6


#kopiowanie listy
# new_list = old_list.copy()
# new_list = list(old_list)
# new_list = old_list[:]
#
# print(old_list)
# print(new_list)

#zadanie1
#wygenerowac liste wykorzystujac fkce range(), druga lista ma miec kwadraty pierwszej

#tworzymy pusta liste, dopiero pozniej przypisuje do niej elementy
# old_list = []
# old_list = list(range(9))
# print(old_list)
#
# new_list = []
#
# for i in old_list:
#     new_list.append(i**2)
#
# print(new_list)


#zadanie - kwadrat losty - przyklad
# list_numbers = range(10)
# list_of_squares = []
#
# # list_of_squares.append(2)
# # list_of_squares.append(13)
#
# #1 sposob
# for number in list_numbers:
#     list_of_squares.append(number**2)
#
# #2 sposob
# list_of_squares_2 = list(list_numbers[:])
# for index, number in enumerate(list_numbers):
#     list_of_squares_2[index] = (number**2)
#
#
# #3 sposb
# last_list_of_squares = [x**2 for x in list_numbers]
#
# words = ["iTs", "mE", "PytHon"]
# new_words = [word.upper() for word in words]
#
# print(new_words)
# print(words)
#
# print(last_list_of_squares)
#
#
# print(list(list_numbers))
# print(list_of_squares)
# print(list_of_squares_2)

#zagniezdzona lista
# import copy
#
# nested_list = [ [ [1,2,3],2,3 ] ]
# new_list = copy.deepcopy(nested_list)
# nested_list[0][0][1] = 36
#
# print(nested_list)
# print(new_list)

# result
# [[[1, 36, 3], 2, 3]]
# [[[1, 2, 3], 2, 3]]

#zip

#tworzymy dwie rozne listy
#tworzymy trzecia pusta liste, do ktorej bedziemy wpisywali wynik - dodawanie elementow z listy 1 i 2
#append dodaje kolejny element do listy

list_1 = list(range(2,30))
list_2 = list(range(14,19))
list_3 = []

print(list_1)
print(list_2)


for a, b in zip(list_1,list_2):
    list_3.append(a+b)

print(list_3)

