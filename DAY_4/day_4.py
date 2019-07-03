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
old_list = []
old_list = list(range(9))
print(old_list)

new_list = []

for i in old_list:
    new_list.append(i**2)

print(new_list)
