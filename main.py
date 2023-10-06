import datetime
class Osoba:
    #konštruktor
    def __init__(self, meno_param, priezvisko_param, rok_param):
        self.meno = meno_param
        self.priezvisko = priezvisko_param
        self.rok = rok_param
        self.vek = datetime.date.today().year - self.rok
    #metóda pozdrav

    def pozdrav(self):
        print("Ahoj ja som", self.meno, self.priezvisko, "a mám", self.vek, "rokov.")

    def vypis_vek(self):
        print(self.vek)


matus = Osoba("Matúš", "Budoš", 2005)
matus.pozdrav()
matus.vypis_vek()
jano = Osoba("Janko", "Hruška", 2000)
jano.pozdrav()
jano.vypis_vek()
