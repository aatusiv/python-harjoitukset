import pelaajatiedot, valikko, hahmot, huoneet, random

def main():
    age_check = pelaajatiedot.kysy_tiedot()
    if age_check is True:
        valikko.menu()
        ernesti = hahmot.Kissa(name="Ernesti", score=0, bag=[], location="")
        while True:
            print(f"Sijainti: {huoneet.makuuhuone.name}")
            break

                

            
if __name__ == "__main__":
    main()