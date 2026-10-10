from peli import tallennus, hahmot, kayttoliittyma, pelaajatiedot

def menu():


    # Kysyy pelaajan tiedot
    age = pelaajatiedot.ask_age()
    if age == False:
        return None
    while True:

        # Puhdistaa näytön ja printtaa statuksen, tarkastaa käyttiksen
        kayttoliittyma.clear_screen()

        selection = input("1. Aloita uusi peli\n2. Lataa peli\n3. Tarkasta pelaajan tiedot\n4. Vaihda pelaajan tiedot\n0. Lopeta peli\n")

        if selection == "1":
            name = pelaajatiedot.ask_name()
            ernesti = hahmot.Kissa("Ernesti", 0, [], "makuuhuone")
            time = 120
            tallennus.save_game(ernesti, time, name.lower())

            kayttoliittyma.clear_screen()
            input("Onnea peliin! Enter aloittaaksesi pelin")

            return ernesti, time, name

        elif selection == "2":
            # Ladataan tiedot JSON filusta
            name = pelaajatiedot.ask_name()
            loaded_data = tallennus.lataa_peli(name.lower())
            
            if loaded_data is not None:

                ernesti = hahmot.Kissa("Ernesti", loaded_data["pisteet"], set(loaded_data["reppu"]), loaded_data["sijainti"])
                ernesti.devices_off = set(loaded_data["sammutetut"])
                time = loaded_data["kello"]
                name = loaded_data["nimi"]

                print("\nPeli ladattu onnistuneesti!")
                return ernesti, time, name, age
            else:
                kayttoliittyma.clear_screen()
                input("Tallennuksen lataaminen epäonnistui.")


        elif selection == "3":
            kayttoliittyma.clear_screen()
            name = pelaajatiedot.ask_name()
            try:
                kayttoliittyma.clear_screen()
                loaded_data = tallennus.lataa_peli(name.lower())
                if loaded_data is not None:
                    print(f"Nimi: {loaded_data["nimi"]}\nPisteet: {loaded_data["pisteet"]}\nAika: {loaded_data["kello"]// 60:02d}:{loaded_data["kello"]% 60:02d}\nSijainti: {loaded_data["sijainti"]}")
                    input()
                else:
                    print(f"Nimi: {name}\nPisteet: Ei tallennusta\nAika: Ei tallennusta\nSijainti: Ei tallennusta")
                    input()
            except UnboundLocalError:
                print("Nimellä ei löydy tallennusta.")
                input()

        elif selection == "4":
            name = change_playerinfo()


        elif selection == "0":
            print("\nPeli sammuu. Kiitos pelaamisesta")
            return None


def change_playerinfo():
    kayttoliittyma.clear_screen()
    name = pelaajatiedot.ask_name()
    return name

def main():
    menu()


if __name__ == "__main__":
    main()
