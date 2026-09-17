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


hissi = Hissi()

while True:
    selection = int(input("Valitse kerros: "))
    if selection <= 0:
        print("Ohjelma lopetetaan.")
        break

    hissi.siirry_kerrokseen(selection)
