#1_if_else_ex
# oblicz czy rok jest przestępny
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

####UWAGA#### ---> a,b, c moga byc w funkcji?????? czy na zewnatrz?????

def rok_przestepny():

    rok = int(input('Podaj rok: '))

    if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        print('To jest rok przestepny')
    else:
        print('To nie jest rok przestepny')

#rok_przestepny()

##################################################################################################################

# 2_if_else_ex
# 8. podane 3 boki trojkata, okresl
# czy uda sie narysowac trojkata
#* dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
# czy jest to tr. roznoboczny, rownoramienny czy rownoboczny


def trojkat():

    a = int(input('Podaj bok a: '))
    b = int(input('Podaj bok b: '))
    c = int(input('Podaj bok c: '))

    if (a < b + c) and (b < a + c) and (c < a + b):
        print('Zbudowanie trójkąta jest możliwe')
        if a == b == c:
            print('To jest trójkąt równoboczny')
        elif (a == b != c) or (a == c != b) or (c == b !=a):
            print('To jest trójkąt równoramienny')
        else:
            print('To jest trójkąt róznoboczny')

#trojkat()

##################################################################################################################
# 3_if_else_ex
# 10. zamiana temperatury
# wejscie: temperatura w C lub F, np: "35C" "100F"
# wyjście "Temperatura w {typ} to {xxx} stopni" - jezeli podano w F to wypisz w C i odwrotnie
# C = (F - 32) * (5/9)
# F = C * (9 / 5) + 32


def temperatura():

    temp = input('Podaj tempereture: ')

    if 'F' in temp:
        C = round((int(temp.replace('F', '')) - 32) * (5 / 9),2)
        print(f'Temperatura w {temp} to {C}C')
    else:
        F = round((int(temp.replace('C', '')) * (9 / 5) + 32),2)
        print(f'Temperatura w {temp} to {F}F')

#temperatura()

# 4_for_loops_ex
#obl. ilość l. parzystych i nieparzystych w zakresie

def spr_parzyste():

    zakres = range(23746)

    parzyste = 0
    nieparzyste = 0

    for i in zakres:
        if i % 2 ==0:
            parzyste += 1
        else:
            nieparzyste += 1

    return(f"Liczb parzystych: {parzyste}, liczb nieparzystych: {nieparzyste}")

#print(spr_parzyste())

###################################################################################################################

# # 5_for_loops
# # policz samogloski i spolgloski

def zliczanie_liter():

    zdanie = input("Podaj jakieś zdanie: ")

    samogloski = 0
    spolgloski = 0

    lista_samoglosek = "aeiouyąęóAEIOYĄĘÓ"
    lista_spolglosek = "bcdfghjklmnpqrstvwzćńłśżźBCDFGHJKLMNPQRSTWZĆŃŁŚŻŹ"

    for x in zdanie:
        if x in lista_samoglosek:
            samogloski += 1
        elif x in lista_spolglosek:
            spolgloski +=1
        else:
            continue

    return(f"Samoglosek: {samogloski}, spółgłosek: {spolgloski}")

#print(zliczanie_liter())

##################################################################################################################

#6_for_loops

# fizz buzz
# wypisac liczby od 1 do 100 (włącznie)
# zamiast l. podzielnych przez 3 wypisz Fizz
# zamiast liczb podzielnych przez 5 wypisz Buzz
# zamist liczb podzielnych przez 3 i 5 wypisz FizzBuzz

def numbers_divided_by():

    zakres = (range(1, 101))

    for liczba in zakres:
        if (liczba % 3 == 0) and (liczba % 5 == 0):
            print(liczba, "FizzBuzz")
        elif liczba % 3 == 0:
            print(liczba, 'Fizz')
        elif liczba % 5 == 0:
            print(liczba, "Buzz")
        else:
            print(liczba,"Not Divided by 3 or 5")

#numbers_divided_by()

##################################################################################################################

#7_while_loops
# program, ktory wypisze liczby (z zakresu 0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
#

def fibonaccie():

    zakres = range(0, 100)

    fib_list = []

    for i in zakres:
        if i == 0:
            fib_list.append(i)
        elif i == 1:
            fib_list.append(i)
        elif i == 2:
            fib_list.append(1)
        else:
            i = fib_list[-1] + fib_list[-2]
            fib_list.append(i)

    print(fib_list)

#fibonaccie()

##################################################################################################################

#8_func_1
# napisz funkcje obliczajaca pole kwadratu

def pole_kwadratu():

    a = int(input('Podaj dlugosc boku kwadratu: '))

    pole = a ** 2
    return f"Pole kwadratu wynosi: {pole}"

#print(pole_kwadratu())