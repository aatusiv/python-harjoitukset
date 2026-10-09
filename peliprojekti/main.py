import subprocess, os
from peli import hahmot, huoneet, kayttoliittyma, tallennus, pelaajatiedot, valikko, ohjeet

def main():

    # Puhdistaa näytön ja printtaa statuksen, tarkastaa käyttiksen
    kayttoliittyma.clear_screen()

    data = valikko.menu() # Jos tallennus olemassa, palauttaa ernestin + ajan

    # Lopettaa pelin (valikko.menu() palauttaa False, jos käyttäjä valitsee 0)
    if data == False:
        return

    if isinstance(data, tuple):
        ernesti = data[0]
        time = data[1]
        items = data[2]
    else:
        ernesti = hahmot.Kissa(name="Ernesti", score=0, bag=[], location="makuuhuone")
        time = 120


    # Tulostaa ohjeet sekä intron pelaajalle
    kayttoliittyma.clear_screen()
    ohjeet.print_rules()
    
    kayttoliittyma.clear_screen()
    ohjeet.print_intro()


    while True:

        # Ajan formatointi
        time_hours = time // 60
        time_min = time % 60
        print_time = f"{time_hours:02d}:{time_min:02d}"

        if time >= 420:
            print("Kello löi 07:00, ihmiset heräsivät ja jäit kiinni. Hävisit pelin.")
            break
        if ernesti.location == "makuuhuone" and ernesti.score >= 50:
            print("Voitit pelin, keräsit herkut ja ehdit ajoissa nukkumaan.")
            break


        kayttoliittyma.printStats(ernesti.location, print_time, ernesti.score, ernesti.bag)
        current_room = huoneet.all_rooms[ernesti.location]
        print(f"\n{current_room.desc}\n")

        if len(current_room.devices) > 0:
            for dev_name in current_room.devices:
                if dev_name not in ernesti.devices_off:
                    print(f"Huomaat, että {dev_name} on jäänyt päälle turhaan.")
            print()

        # Huoneissa olevat esineet
        # Printtaa vain esineet joita ernesti ei ole ottanut
        if len(current_room.items) > 0:
            missing_items = []

            for item in current_room.items:
                if item not in ernesti.bag:
                    missing_items.append(item)
            
            if missing_items:
                print("Huoneessa on seuraavat esineet:")
                for item in missing_items:
                    print(f" - {item}")
                print()




        
        print("Mahdolliset suunnat:")
        for direction, room_key in current_room.nearby_rooms.items():
            target_room = huoneet.all_rooms[room_key]
            print(f"- {direction} ({target_room.name})")
        print("\n" + "="*30)

        selection = input("Mitä Ernesti tekee? (liiku/ota/sammuta/tallenna/lopeta): ")

        if selection == "lopeta":
            print("\nPeli päättyi.\n")
            break

        elif selection == "tallenna":
            tallennus.save_game(ernesti, time)
            input("\nEnter jatkaaksesi.")

        # Tarkistaa suunnan + liikuttaa ernestin
        elif selection.startswith("liiku"):
            try:
                direction = selection.split(" ")[1]
                if direction in current_room.nearby_rooms:
                    new_loc = current_room.nearby_rooms[direction]

                    if new_loc == "kodinhoitohuone" and "koiranluu" not in ernesti.bag:
                        input("Koira vartioi kodinhoitohuoneessa, tarvitset luun jatkaaksesi. Enter jatkaaksesi.")
                    else:
                        if new_loc == "kodinhoitohuone" and "koiranluu" in ernesti.bag:
                            input("Ernesti heittää luun harhauttaakseen koiraa.")
                            ernesti.bag.remove("koiranluu")
                        ernesti.move(new_loc)
                        time += 15
                else:
                    input(f"Ei voi liikkua suuntaan {direction}. Enter jatkaaksesi.")
            except IndexError:
                input("Anna lisäksi sijainnin suunta. Enter jatkaaksesi.")

        elif selection.startswith("ota"):
            try:
                # Parsee käyttäjän antaman inputin komennosta ja esineen nimestä
                item = selection.split(" ")[1]

                if item in current_room.items:
                    ernesti.pick_item(item)
                    current_room.items.remove(item)
                    time += 15
                else:
                    input(f"Ei ole esinettä: {item}. Enterr jatkaaksesi.")
            except IndexError:
                input("Anna lisäksi esineen nimi. Enter jatkaaksesi.")

        elif selection.startswith("sammuta"):
            try:
                # Parsee käyttäjän antaman inputin komennosta ja laitteen nimestä
                dev_name = selection.split(" ")[1]

                if dev_name in current_room.devices:
                    ernesti.turn_off(dev_name)
                    time += 15
                else:
                    input(f"Huoneessa ei ole laitetta {dev_name}.")
            except IndexError:
                input("Anna lisäksi laitteen nimi. Enter jatkaaksesi.")

        else:
            input("Virheellinen komento. Enter jatkaaksesi")
            
if __name__ == "__main__":
    main()