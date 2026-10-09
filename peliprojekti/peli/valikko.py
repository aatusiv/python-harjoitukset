from peli import tallennus, hahmot, kayttoliittyma, pelaajatiedot
import os, subprocess

def menu():


    # Kysyy pelaajan tiedot
    name, age = pelaajatiedot.kysy_tiedot()
    
    while True:

        # Puhdistaa näytön ja printtaa statuksen, tarkastaa käyttiksen
        kayttoliittyma.clear_screen()

        selection = input("1. Aloita uusi peli\n2. Lataa peli\n3. Tarkasta pelaajan tiedot\n4. Vaihda pelaajan tiedot\n0. Lopeta peli\n")

        if selection == "1":

            ernesti = hahmot.Kissa("Ernesti", 0, [], "makuuhuone")
            time = 120
            tallennus.save_game(ernesti, time, name, age)

            kayttoliittyma.clear_screen()
            input("Onnea peliin! Enter aloittaaksesi pelin")

            return ernesti, time, name, age

        elif selection == "2":
            # Ladataan tiedot JSON filusta
            loaded_data = tallennus.lataa_peli()
            
            if loaded_data is not None:

                ernesti = hahmot.Kissa("Ernesti", loaded_data["pisteet"], set(loaded_data["reppu"]), loaded_data["sijainti"])
                ernesti.devices_off = set(loaded_data["sammutetut"])
                time = loaded_data["kello"]

                return ernesti, time
            else:
                kayttoliittyma.clear_screen()
                input("Tallennuksen lataaminen epäonnistui.")


        elif selection == "3":
            kayttoliittyma.clear_screen()
            loaded_data = tallennus.lataa_peli()

            if loaded_data is not None:
                print(f"Nimi: {loaded_data["nimi"]}\nIkä: {loaded_data["ikä"]}\nPisteet: {loaded_data["pisteet"]}\nSijainti: {loaded_data["sijainti"]}")
                input()
            else:
                kayttoliittyma.clear_screen()
                input("Tallennuksen lataaminen epäonnistui.")

        elif selection == "4":
            name, age = change_playerinfo()


        elif selection == "0":
            print("\nPeli sammuu. Kiitos pelaamisesta")
            return None


def change_playerinfo():
    kayttoliittyma.clear_screen()
    name, age = pelaajatiedot.kysy_tiedot()
    return name, age

def main():
    menu()


if __name__ == "__main__":
    main()
