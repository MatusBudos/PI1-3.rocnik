import random
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
     def __init__(self, meno, priezvisko, rok, titul, predmet, trieda):
         super().__init__(meno, priezvisko, rok)    #môže byť aj Osoba.__init__(self, meno, priezvisko, rok)
         self.titul = titul
         self.predmet = predmet
         self.trieda = trieda
     def pozdrav(self):
         print("Dobrý deň, som učiteľ", self.titul, self.meno, self.priezvisko, ", mám", self.vek, "rokov a učím predmet,", self.predmet, "som triedny učiteľ", self.trieda, "triedy.")

class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
         Osoba.__init__(self, meno, priezvisko, rok)
         self.trieda = trieda
    def pozdrav(self):
        Osoba.pozdrav(self)
        print("Som študent", self.trieda, "triedy.")

# matus = Student("Matúš", "Budoš", 2005, "3.AT")
# jan = Osoba("Ján", "Jablko", 2004)
# jozo = Ucitel("Jozef", "Hruška", 1995, "Ing.", "Programovanie")
# jozo.pozdrav()
# jan.pozdrav()
# matus.pozdrav()

pocet_studentov = 10
pocet_ucitelov = 5
studenti = list()
ucitelia = list()

for i in range (pocet_studentov):

    with open("mena.txt", "r", encoding="utf-8") as t:
        mena = tuple(t)
    meno = random.choice(mena)
    meno = meno[:-1]
    with open("priezviska.txt", "r", encoding="utf-8") as s:
        priezviska = tuple(s)
    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]
    rok = random.randint(2005, 2008)
    if rok == 2005:
        trieda = "IV."
    elif rok == 2006:
        trieda = "III."
    elif rok == 2007:
        trieda = "II."
    else:
        trieda = "I."

    trieda = trieda + random.choice(("A", "B", "C"))

    studenti.append(Student(meno, priezvisko, rok, trieda))
print("Študenti:")
for i in range(pocet_studentov):
    print(i+1, studenti[i].meno, studenti[i].priezvisko, studenti[i].vek, studenti[i].rok, studenti[i].trieda)
studenti[1].pozdrav()

for i in range (pocet_ucitelov):

    with open("mena.txt", "r", encoding="utf-8") as t:
        mena = tuple(t)
    meno = random.choice(mena)
    meno = meno[:-1]
    with open("priezviska.txt", "r", encoding="utf-8") as s:
        priezviska = tuple(s)
    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]
    rok = random.randint(1958, 2004)

    predmet = random.choice(("Programovanie", "Matematika", "Fyzika"))
    titul = random.choice(("Ing.", "Mgr.", "Bc."))
    trieda = random.choice(("I.", "II.", "III.", "IV.")) + random.choice(("A", "B", "C"))
    ucitelia.append(Ucitel(meno, priezvisko, rok, titul, predmet, trieda))
print("---------------------------\n")
print("Učitelia:")
for i in range(len(ucitelia)):
    print(i+1, ucitelia[i].meno, ucitelia[i].priezvisko, ucitelia[i].rok, ucitelia[i].titul, ucitelia[i].predmet, ucitelia[i].trieda)
ucitelia[1].pozdrav()