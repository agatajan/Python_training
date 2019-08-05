import requests
from bs4 import BeautifulSoup

#zapisujemy adres strony do zmiennej
#Przyda się jeśli w źródle strony adresy będą względne czyli zaczynające się od "/"
#zamiast bezwzględne czyli zawierające cały adres z domeną i protokołem
adres_url = "https://wallpaperlist.com"

#za pomocą modułu request łączymy się do strony metodą get() i pobieramy jej zawartość
#z pola "content"
zrodlo_strony = requests.get(adres_url).content

#za pomocą modułu BeautifulSoup parsujemy żróðło strony dzięki czemu
#otrzymamy obiekt na którym będziemy mogli dokonywać dodatkowych opracji
sparsowane_zrodlo = BeautifulSoup(zrodlo_strony, 'html.parser')

#na obiekcie BeautifulSoup wykonujemy metodę find_all() która wyszukuje nam wszystkie
#określone znaczniki HTML w źródle
wszystkie_znaczniki_img = sparsowane_zrodlo.find_all('img')

#iterujemy po wszyskich znaleźionych znacznikach
for img in wszystkie_znaczniki_img:
    #w prosty sposób pobieramy atrybut "src" który w htmlu zawiera adres do obrazka
    #i doklejamy adres domeny by mieć w pełni działający adres url
    adres_obrazka = adres_url + img['src']

    #rozdzielamy adres po każdym "/" i wybieramy ostatnią wartość z listy
    #w ten sposób do zmiennej przypisaliśmy sobie nazwe pliku
    nazwa_obrazka = adres_obrazka.split('/')[-1]

    #pobieramy zawartość obrazka za pomocą znanego już nam modułu i metody :)
    obrazek = requests.get(adres_obrazka).content

    with open('obrazki/' + nazwa_obrazka, 'wb+') as plik:
        #zapisujemy ściągniętą zawartość do plik
        #UWAGA, tryb pliku musi być binarny, oraz zakładamy, że katalog "obrazki" istnieje
        plik.write(obrazek)

#po wykonaniu programu w katalgou obrazki będziemy mieli zapisane wszystkie obrazki z w.w. strony