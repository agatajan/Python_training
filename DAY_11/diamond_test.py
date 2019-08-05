class Zwierze(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def mow(self):
        print(f"Zwierzak {self.nazwa} nie mówi")

    def ruszaj_sie(self):
        print(f"Zwierz {self.nazwa} rusza się.")


class Kon(Zwierze):
    def __init__(self, nazwa, umaszczenie):
        # lepiej podawać jawnie skąd ma być dziedziczone
        # super().__init__(nazwa)
        Zwierze.__init__(self, nazwa)
        self.umaszczenie = umaszczenie

    def mow(self):
        print(f"Koń {self.nazwa} mówi: iiiii-haaaaa")

    def ruszaj_sie(self):
        print(f"Koń {self.nazwa} hasa po łące.")


class Osiol(Zwierze):
    def __init__(self, nazwa, st_uparotsci):
        super().__init__(nazwa)
        self.st_upartosci = st_uparotsci

    def ruszaj_sie(self):
        print(f"Osioł {self.nazwa} nie chce sie ruszyc"
              f" przez najbliższe {self.st_upartosci} minuty.")

    def wypisz_upartosc(self):
        print(f"Upartość: {self.st_upartosci} minuty.")


class Mul(Kon, Osiol):
    def __init__(self, nazwa, umaszczenie):
        # jawnie używamy inicjalizator pierwszego rodzica
        Kon.__init__(self, nazwa, umaszczenie)

zwierzak = Zwierze("pantofelek")
zwierzak.mow()
zwierzak.ruszaj_sie()
print(15 * '-')
kucyk = Kon("Rafal", "brązowy")
kucyk.mow()
kucyk.ruszaj_sie()
print(15 * '-')
osiolek = Osiol("uparciuch", 4)
osiolek.mow()
osiolek.ruszaj_sie()
print(15 * '-')

mul_1 = Mul("siwuch", "siwy")
mul_1.mow()
mul_1.ruszaj_sie()

print(help(Mul))
