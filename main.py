import datetime
class Osoba:
    #konštruktor
    def __init__(self, meno, priezvisko, rok):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    #metóda pozdrav
    def pozdrav(self):
        print("Ahoj ja som", self.meno, self.priezvisko, "a mám", self.vek, "rokov.")

    def vypis_vek(self):
        print(self.vek)

    #trieda Ucitel dedi z triedy Osoba
class Ucitel(Osoba):
    def __init__(self, meno, priezvisko, rok, titul, predmet):
        super().__init__(meno, priezvisko, rok)    #môže byť aj Osoba.__init__(meno, priezvisko, rok)
        self.titul = titul
        self.predmet = predmet
    def pozdrav(self):
        print("Dobrý deň, som učiteľ", self.titul, self.meno, self.priezvisko, ", mám", self.vek, "rokov a učím predmet", self.predmet)


jan = Osoba("Ján", "Jablko", 2004)
jozo = Ucitel("Jozef", "Hruška", 1995, "Ing.", "Programovanie")
jozo.pozdrav()
jan.pozdrav()

