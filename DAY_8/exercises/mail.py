import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#tworzymy obiekt MIMEMultipart, który za nas dokona odpowiedniego utworzenia źródła maila do wysłania
msg = MIMEMultipart()

#otwieramy plik którego zawartość chcemy wysłać jako treść maila
textfile = 'adresy.csv'
with open(textfile, 'r') as fp:
    #tworzymy obiekt MIMEText w paramatrze podając zawartość pliku
    #jest to obiekt odpowiadający za treść maila
    text = MIMEText(fp.read())

#dołączamy treść maila do naszej wiadomości
msg.attach(text)

#ustawiamy nagłówki niezbędne do poprawnej wysyłki maila
#temat
msg['Subject'] = 'The contents of ' + textfile
#nadawca
msg['From'] = 'isapy@o2.pl'
#odbiorca
msg['To'] = 'isapy@o2.pl'

#tworzymy obiekt dzięki któremy wyślemy wiadomość
#w konstruktorze podajemy adres serwera dzięki któremy będziemy wysyłać wiadomość
s = smtplib.SMTP('poczta.o2.pl')

#podany serwer wymaga uwierzytelnienia więc wywołujemy metodę do logowania
s.login('isapy@o2.pl', 'isapython')

#wywłamy wiadomość, moetoda msg.as_string() zamienia obiekt MIMEMultipart ze wszystkim załącznikami
#na wiadomość zgodną z RFC do wysłania wiadomośći
s.sendmail(msg['From'], [msg['To']], msg.as_string())

#zamykamy nasze połaczenie z serwerem
#analogicznie do otwierania plików można użyć tutaj konstrukcji with-as
#dzięki czemu s.quit() wykona się samo po wyjściu z bloku with i nie trzeba tej metody jawnie wykonywać
s.quit()
