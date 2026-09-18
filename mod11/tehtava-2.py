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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti # Kilowattitunteina
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottori(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki # Litroina
        super().__init__(rekisteritunnus, huippunopeus)


def main():
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttoauto = Polttomoottori("ACD-123", 165, 32.3)

    sähköauto.kiihdytä(80)
    polttoauto.kiihdytä(50)

    sähköauto.kulje(3)
    polttoauto.kulje(3)

    print(f"Sähköauton kuljettu matka: {sähköauto.matka}km\nPolttomoottori auton kuljettu matka: {polttoauto.matka}km")

if __name__ == "__main__":
    main()