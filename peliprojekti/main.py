import pelaajatiedot, valikko, random, subprocess
from peli import hahmot, huoneet, kayttoliittyma

def main():
    age_check = pelaajatiedot.kysy_tiedot()
    if age_check is True:
        valikko.menu()
        ernesti = hahmot.Kissa(name="Ernesti", score=0, bag=[], location="makuuhuone") # Luo pelin päähahmon, aloitus paikkana aina makuuhuone

        while True:

            # Puhdistaa näytön ja printtaa statuksen
            subprocess.run("clear")
            kayttoliittyma.printStats(ernesti.location, "02:00", ernesti.score, ernesti.bag)

            selection = input("Anna valinta: ")
            if selection == "1":
                ernesti.move(huoneet.makuuhuone.nearby_rooms["etelä"])

            
if __name__ == "__main__":
    main()