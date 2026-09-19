inv = []

def menu():

    while True:
        selection = input("\n1. Lisää esineitä varastoon\n2. Näytä esineet\n3. Tarkasta pelaajan tiedot\n4. Vaihda pelaajan tiedot\n0. Lopeta peli\n")
        if selection == "1":
<<<<<<< HEAD
            inventory()
=======
            print("Onnea peliin!")
            break
>>>>>>> 6436a12 (Korjattu iäntarkistus, lisätty luokat ja muutettu valikkoa)

        elif selection == "2":
            print_inventory()

        elif selection == "3":
            check_playerinfo()

        elif selection == "4":
            age_check = change_playerinfo()
            if age_check is False:
                print("Olet alaikäinen, peli sammuu.")
                break

        elif selection == "0":
            print("\nPeli sammuu. Kiitos pelaamisesta")
            break

def check_playerinfo():
    try:
        with open("pelaaja-tiedot.txt", "r") as file:
            name, age = file.read().split(", ")
            print(f"\nNimi: {name}\nIkä: {age}")

    except FileNotFoundError:
        print("Tiedostoa ei löydy.")

    except IOError:
        print("Tiedoston käsittelyssä oli virhe.")

def change_playerinfo():
    name = input("\nAnna uusi nimi: ")
    age = int(input("Anna uusi ikä: "))

    if age < 12:
        return False

    try:
        with open("pelaaja-tiedot.txt", "w") as file:
            file.write(f"{name}, {age}")
    except IOError:
        print("Tiedoston käsittelyssä oli virhe.")

def main():
    menu()


if __name__ == "__main__":
    main()
