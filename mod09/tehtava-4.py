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

        else:
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

cars = []

# Luo auto-oliot
for x in range(10):
    cars.append(Auto(f"ABC-{x}", random.randint(100,200)))

# Luodaan "lippu"
winner = False
while winner is False:

    # Muuttaa nopeutta satunnaisesti -10 ja 15kmh väliltä
    for x in range(len(cars)):
        cars[x].kiihdytä(random.randint(-10,15))

    # Kuljettaa tunnin ajan
    for x in range(len(cars)):
        cars[x].kulje(1)

    # Tarkastaa kuljetun matkan
    for x in range(len(cars)):
        if cars[x].matka >= 10000:
            print(f"{cars[x].rekisteritunnus} on voittanut kilpailun")
            for y in range(len(cars)):
                print(f"Rekisteritunnus: {cars[y].rekisteritunnus}, huippunopeus: {cars[y].huippunopeus}km/h, nopeus: {cars[y].nopeus}km/h, matka: {cars[y].matka}km")
            winner = True