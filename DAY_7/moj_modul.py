#ostateczna wersja sprawdzania co jest plikiem/katalogiem/listuje zawartosc katalogu:
#stworzyc z modulu funkcje definiujemy funcje + robimy wciecia TABem
#dobra praktyka jest budowanie funkcji z modulu

#przerabiamy funkcje zeby zwracala wartosc, a nie robila print
#return zwraca tylko jeden wynik - pierwszy
#zmienna zeby pozbierac dane z for'a

import os

def show_dir():

    list = os.listdir()

    if len(list) == 0:
        return 'Katalog jest pusty 1'

    new_list = []

    for item in list:
        if os.path.isfile(item):
            new_list.append(f"Pliki: {item}\n")
        elif os.path.isdir(item):
            new_list.append(f"Katalogi: {item}\n")
    return new_list