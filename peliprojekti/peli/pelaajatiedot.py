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
        return name, age

if __name__ == "__main__":
    kysy_tiedot()