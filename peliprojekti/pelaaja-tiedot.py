name = input("Anna nimesi: ")
age = int(input("Anna ikäsi: "))

if age < 12:
    print("Olet alaikäinen, peli sammuu.")
else:
    print(f"Hei, {name}")
    while True:
        print("1. Aloita\n2. Lopeta")
        selection = input("Kirjoita komento: ")
        if selection == "Lopeta":
            break
# print(f"Nimesi on {name} ja ikäsi {age}.")