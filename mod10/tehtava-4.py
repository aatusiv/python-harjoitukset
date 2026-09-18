import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeus):
        if nopeus > 0:
            if self.nopeus + nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
                # print(f"Nopeus on nyt huipussaan: {self.nopeus}km/h.")
            else:
                self.nopeus += nopeus
                # print(f"Nopeus on nyt: {self.nopeus}km/h.")

        elif nopeus < 0:
            # matematiikan säännöt ex. 150 + (-200)
            if self.nopeus + nopeus <= 0:
                self.nopeus = 0
                # print(f"Nopeus on nyt nolla: {self.nopeus}km/h.")
            else:
                self.nopeus += nopeus
                # print(f"Nopeus on nyt: {self.nopeus}km/h.")

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
        # print(f"Kuljettu matka: {self.matka}km.")

class Kilpailu:
    def __init__(self, nimi, kilometrimäärä, autolista):
        self.nimi = nimi
        self.kilometrimäärä = kilometrimäärä
        self.autolista = autolista


    def tunti_kuluu(self):
        # Muuttaa nopeutta satunnaisesti -10 ja 15kmh väliltä
        for x in range(len(self.autolista)):
            self.autolista[x].kiihdytä(random.randint(-10,15))
        # Kuljettaa tunnin ajan
        for x in range(len(self.autolista)):
            self.autolista[x].kulje(1)

    def tulosta_tilanne(self):
        for y in range(len(self.autolista)):
            print(f"Rekisteritunnus: {self.autolista[y].rekisteritunnus}, huippunopeus: {self.autolista[y].huippunopeus}km/h, nopeus: {self.autolista[y].nopeus}km/h, matka: {self.autolista[y].matka}km")

    def kilpailu_ohi(self):
        # Tarkastaa kuljetun matkan
        for x in range(len(self.autolista)):
            if self.autolista[x].matka >= 8000:
                print(f"{self.autolista[x].rekisteritunnus} on voittanut kilpailun")
                self.tulosta_tilanne()
                return True
        return False
cars = []

# Luo auto-oliot
for x in range(10):
    cars.append(Auto(f"ABC-{x}", random.randint(100,200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, cars)

# Luodaan "lippu"
winner = False
tunnit = 0

while winner is False:
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit >= 10:
        kilpailu.tulosta_tilanne()
        print("\n")
        tunnit = 0
    winner = kilpailu.kilpailu_ohi()