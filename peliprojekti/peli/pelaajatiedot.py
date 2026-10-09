def kysy_tiedot():

    while True:
        try:
            name = input("Anna nimesi: ")
            if name == "":
                print("Nimi ei voi olla tyhjä.")
                continue

            age = int(input("Anna ikäsi: "))
            if age < 0:
                print("Ikä ei voi olla negatiivinen.")
                continue 
            break

        except ValueError:
            print("Anna ikäsi numerona.")

    if age < 12:
        print("Olet alaikäinen, peli sammuu.")
        return False
    else:
        try:
            with open("pelaaja-tiedot.txt", "w") as file:
                file.write(f"{name}, {age}")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")
        return True

def main():
    kysy_tiedot()

if __name__ == "__main__":
    main()