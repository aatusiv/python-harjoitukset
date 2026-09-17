class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


car = Auto("ABC-123", 233)

print(car.rekisteritunnus, car.huippunopeus, car.nopeus, car.matka)