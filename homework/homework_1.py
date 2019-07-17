# #HOMEWORK_day2#
# #homework1
# float_but_int = 50/2
# print(float_but_int)
# print(type(float_but_int))
# # tutaj jeszcze o to chodzilo
# print(float_but_int.is_integer())
#
# #homework2
# 11011010
# bit_8 = 0+2+0+8+16+0+64+128
# print(bit_8)
# #bit_8 = 218
#
# #homework3
# var1 =  "Sun"
# var2 =  "is"
# var3 = "setting"
# print(var1+'\n\t' + var2 + '\n\t\t' +var3)
# print(f"{var1}\n\t{var2}\n\t\t{var3}")
#
# #homework4
# #1
# y = int(input('Wstaw liczbe:'))
# print('Szescian liczby' + ' ' + str(y) + ' ' 'wynosi ' + str(y**3) + ' natomiast kwadrat ' + str(y**2))
# #2
# y = int(input('Wstaw liczbe:'))
# print('Szescian liczby y wynosi '+ str(y**3) +' natomiast kwadrat '+ str(y**2))
#
# #homework5
# z = int(input ("Podaj aktualna temperature:"))
# temp1=10
# temp2=20
# temp3=30
# if z<temp1:
#    print('Jest zimno')
# elif z > temp1 and z< temp2:
#    print('Jest cieplo')
# else:
#    print('Jest goraco')

# Oblicz silnie z podanej przez uzytkownika (metoda input) liczby - wyszukaj algorytm na silnie i napisz - przydadza sie zmienne, warunek if, operator *=
# source_number = int(input('Podaj liczbę, aby obliczyć silnię:\n>'))
# ​
# if source_number == 0:
#     print(f'Silnia liczby {source_number} wynosi 1')
# else:
#     result = 1
#     while(source_number>=1):
#         result = result * source_number
#         source_number = source_number-1
#     print(f'Silnia liczby {source_number} wynosi {result}')