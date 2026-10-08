from peli import tallennus, hahmot

def menu():

    while True:
        selection = input("\n1. Aloita peli\n2. Lataa peli\n3. Tarkasta pelaajan tiedot\n4. Vaihda pelaajan tiedot\n0. Lopeta peli\n")
        if selection == "1":
            print("Onnea peliin!")
            return None

        elif selection == "2":
            # Ladataan tiedot JSONista
            loaded_data = tallennus.lataa_peli()
            
            if loaded_data is not None:

                ernesti = hahmot.Kissa(name="Ernesti", score=loaded_data["pisteet"], bag=loaded_data["reppu"], location=loaded_data["sijainti"])
                ernesti.devices_off = set(loaded_data["sammutetut"])
                time = loaded_data["kello"]
                return ernesti, time
            else:
                print("Tallennuksen lataaminen epäonnistui.")

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
