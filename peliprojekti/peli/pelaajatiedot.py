from peli import kayttoliittyma

def ask_age():

    while True:
        try:
            kayttoliittyma.clear_screen()
            age = int(input("Anna ikäsi: "))
            if age < 0:
                input("Ikä ei voi olla negatiivinen.")
                continue 
            break

        except ValueError:
            print("Anna ikäsi numerona.")

    if age < 12:
        print("Olet alaikäinen, peli sammuu.")
        return False
    else:
        return age

def ask_name():
    while True:
        kayttoliittyma.clear_screen()
        name = input("Anna nimesi: ")
        if name == "" or name.isdigit():
            input("Nimi ei voi olla tyhjä tai numeroita.")
            continue
        return name

if __name__ == "__main__":
    ask_age()