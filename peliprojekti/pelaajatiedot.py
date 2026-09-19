def kysy_tiedot():

    name = input("Anna nimesi: ")
    age = int(input("Anna ikäsi: "))

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