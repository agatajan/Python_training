import requests
import csv
import folium

#pobiera dane i wrzuca plik na dysk
def download_data():

    data_url = 'https://raw.githubusercontent.com/infoshareacademy/isa-python12/master/Day8/exercises/airports.csv?token=AGMZVYOFLTW6SJTOMBVPTRS5HCKJ2'

    airports_data = requests.get(data_url)

    #print(airports_data.content)
    csv_data = airports_data.content

    #przypisujemy nazwe pliku do zmiennej
    csv_filename = 'airports.csv'

    with open (csv_filename, 'wb') as csv_file:
        csv_file.write(csv_data)

download_data()

#pbieramy dane z pliku, kazdy wiersz jest czytany osobno jako lista
#linijka po linijce zczytujemy i wtedy mozemy dodac do mapy
#za pomoca indeksu mozemy wyciagnac konkretne pozycje z listy

#gotowy modul do tworzenia mapy
#punkt w folium - Marker - wartosci musza byc w liscie []

map = folium.Map()

#zestaw ikon do sciagniecia - jesli ocon jest poza petla for - wtedy pokazuje tylko jeden punkt
#icon = folium.Icon(icon='bicycle', prefix='fa', color="blue")

with open('airports.csv', 'r') as csv_file:
    data = csv.reader(csv_file)
    for airport in data:
        icon = folium.Icon(icon='plane', prefix='fa', color="blue")
        point = folium.Marker(location=[airport[5], airport[6]], tooltip = airport[1], icon = icon)
        map.add_child(point)


#do zapisania mapy na dysku

map.save('map.html')


# #wysylanie danych na maila
#
# #smtplib - do wyslania danych  na maila (modul od poczty polskiej ;))))
# #minemultipart - list - sklada sie z zalacznikow i tresic
#
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# #tworzymy obiekt MIMEMultipart, który za nas dokona odpowiedniego utworzenia źródła maila do wysłania
# msg = MIMEMultipart()
#
# #otwieramy plik którego zawartość chcemy wysłać jako treść maila
# textfile = 'adresy.csv'
# with open(textfile, 'r') as fp:
#     #tworzymy obiekt MIMEText w paramatrze podając zawartość pliku
#     #jest to obiekt odpowiadający za treść maila
#     text = MIMEText(fp.read())
#
# #dołączamy treść maila do naszej wiadomości
# msg.attach(text)
#
# #ustawiamy nagłówki niezbędne do poprawnej wysyłki maila
# #temat
# msg['Subject'] = 'The contents of ' + textfile
# #nadawca
# msg['From'] = 'isapy@o2.pl'
# #odbiorca
# msg['To'] = 'isapy@o2.pl'
#
# #tworzymy obiekt dzięki któremy wyślemy wiadomość
# #w konstruktorze podajemy adres serwera dzięki któremy będziemy wysyłać wiadomość
# s = smtplib.SMTP('poczta.o2.pl')
#
# #podany serwer wymaga uwierzytelnienia więc wywołujemy metodę do logowania
# s.login('isapy@o2.pl', 'isapython')
#
# #wywłamy wiadomość, moetoda msg.as_string() zamienia obiekt MIMEMultipart ze wszystkim załącznikami
# #na wiadomość zgodną z RFC do wysłania wiadomośći
# s.sendmail(msg['From'], [msg['To']], msg.as_string())
#
# #zamykamy nasze połaczenie z serwerem
# #analogicznie do otwierania plików można użyć tutaj konstrukcji with-as
# #dzięki czemu s.quit() wykona się samo po wyjściu z bloku with i nie trzeba tej metody jawnie wykonywać
# s.quit()



