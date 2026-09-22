class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}\nPäätoimittaja: {self.päätoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.sivumäärä = sivumäärä
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumäärä} sivua")

def main():
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    lehti.tulosta_tiedot()
    print()
    kirja.tulosta_tiedot()


if __name__ == "__main__":
    main()