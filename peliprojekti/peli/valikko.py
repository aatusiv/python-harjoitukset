from peli import tallennus, hahmot, kayttoliittyma
import os, subprocess

def menu():

    while True:

        # Puhdistaa näytön ja printtaa statuksen, tarkastaa käyttiksen
        kayttoliittyma.clear_screen()


        selection = input("1. Aloita peli\n2. Lataa peli\n3. Tarkasta pelaajan tiedot\n4. Vaihda pelaajan tiedot\n0. Lopeta peli\n")
        if selection == "1":
            kayttoliittyma.clear_screen()
            input("Onnea peliin! Enter aloittaaksesi pelin")
            return None

        elif selection == "2":
            # Ladataan tiedot JSON filusta
            loaded_data = tallennus.lataa_peli()
            
            if loaded_data is not None:
                ernesti = hahmot.Kissa(name="Ernesti", score=loaded_data["pisteet"], bag=[], location=loaded_data["sijainti"])
                ernesti.bag = set(loaded_data["reppu"])
                ernesti.devices_off = set(loaded_data["sammutetut"])
                time = loaded_data["kello"]
                items = loaded_data["esineet"]
                return ernesti, time, items
            else:
                input("Tallennuksen lataaminen epäonnistui.")


        elif selection == "3":
            kayttoliittyma.clear_screen()
            check_playerinfo()
            input()

        elif selection == "4":
            age_check = change_playerinfo()
            if age_check is False:
                print("Olet alaikäinen, peli sammuu.")
                return False

        elif selection == "0":
            print("\nPeli sammuu. Kiitos pelaamisesta")
            return False


def check_playerinfo():
    try:
        with open("pelaaja-tiedot.txt", "r") as file:
            name, age = file.read().split(", ")
            print(f"Nimi: {name}\nIkä: {age}")

    except FileNotFoundError:
        print("Tiedostoa ei löydy.")

    except IOError:
        print("Tiedoston käsittelyssä oli virhe.")


def change_playerinfo():
    kayttoliittyma.clear_screen()
    name = input("Anna uusi nimi: ")
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
