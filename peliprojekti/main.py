import pelaajatiedot, valikko, subprocess, os
from peli import hahmot, huoneet, kayttoliittyma

def main():
    age_check = pelaajatiedot.kysy_tiedot()
    if age_check is True:
        valikko.menu()
        ernesti = hahmot.Kissa(name="Ernesti", score=0, bag=[], location="makuuhuone") # Luo pelin päähahmon, aloituspaikkana aina makuuhuone

        time = 120

        while True:

            time_hours = time // 60
            time_min = time % 60
            print_time = f"{time_hours:02d}:{time_min:02d}"

            if time >= 420:
                print("Kello löi 07:00, ihmiset heräsivät ja jäit kiinni. Hävisit pelin.")
                break
            if ernesti.location == "makuuhuone" and ernesti.score >= 50:
                print("Voitit pelin, keräsit herkut ja ehdit ajoissa nukkumaan.")
                break

            # Puhdistaa näytön ja printtaa statuksen
            if os.name == "nt":
                cmd = "cls"
            else:
                cmd = "clear"
            subprocess.run(cmd, shell=True)
            kayttoliittyma.printStats(ernesti.location, print_time, ernesti.score, ernesti.bag)

            current_room = huoneet.all_rooms[ernesti.location]
            print(f"\n{current_room.desc}\n")

            # Lattialla olevat esineet
            if len(current_room.items) > 0:
                print("Huoneessa on seuraavat esineet:")
                for item in current_room.items:
                    print(f" - {item}")
                print()
            
            print("Mahdolliset suunnat:")
            for direction in current_room.nearby_rooms:
                print(f"- {direction}")
            print("\n" + "="*30)

            selection = input("Mihin suuntaan Ernesti liikkuu? (tai lopeta): ")

            if selection == "lopeta":
                print("Peli päättyi. Hyvää yötä!")
                break

            # Tarkistaa suunnan + liikuttaa ernestin
            elif selection in current_room.nearby_rooms:
                new_loc = current_room.nearby_rooms[selection]
                ernesti.move(new_loc) 
                time += 15

            elif selection.startswith("ota"):
                item = selection.split(" ")[1]

                if item in current_room.items:
                    ernesti.pick_item(item)
                    current_room.items.remove(item)
                    time += 15
                else:
                    input(f"Ei ole esinettä: {item}. Enterr jatkaaksesi.")
            
            else:
                input("Virheellinen suunta. Enter jatkaaksesi")
            
if __name__ == "__main__":
    main()