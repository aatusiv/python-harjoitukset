class Hissi:
    def __init__(self):
        self.kerros = 0

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Kerros on: {self.kerros}.")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Kerros on: {self.kerros}.")

    def siirry_kerrokseen(self, kerros_nro):
        if self.kerros < kerros_nro:    
            for x in range(kerros_nro-self.kerros):
                self.kerros_ylös()
        else:
            for x in range(self.kerros - kerros_nro):
                self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissi_lkm = hissi_lkm

        self.hissit = []
        for x in range(self.hissi_lkm):
            self.hissit.append(Hissi())

    def aja_hissiä(self, hissi_nro, kohdekerros):
        self.hissit[hissi_nro].siirry_kerrokseen(kohdekerros)

talo = Talo(1,9,5)

while True:
    hissi_selection = int(input("Valitse hissinumero: "))
    if hissi_selection <= 0:
        print("Ohjelma lopetetaan.")
        break
    floor_selection = int(input("Valitse kerros: "))

    talo.aja_hissiä(hissi_selection-1, floor_selection)