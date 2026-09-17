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
                print(f"Nopeus on nyt huipussaan: {self.nopeus}km/h.")
            else:
                self.nopeus += nopeus
                print(f"Nopeus on nyt: {self.nopeus}km/h.")

        elif nopeus < 0:
            # matematiikan säännöt ex. 150 + (-200)
            if self.nopeus + nopeus <= 0:
                self.nopeus = 0
                print(f"Nopeus on nyt nolla: {self.nopeus}km/h.")
            else:
                self.nopeus += nopeus
                print(f"Nopeus on nyt: {self.nopeus}km/h.")

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
        print(f"Kuljettu matka: {self.matka}km.")


car = Auto("ABC-123", 233)
car.kiihdytä(30)
car.kulje(0.5)
car.kiihdytä(70)
car.kulje(1)
car.kiihdytä(50)
car.kulje(2)
car.kiihdytä(-200)
