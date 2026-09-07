while True:
    number = int(input("Anna luku: "))

    # Ohjelman voi sulkea nollalla.
    if number == 0:
        print("Ohjelma suljetaan.")
        break

    if number < 2:
        print("Luku ei ole alkuluku.")
    else:
        for x in range(2, number):
            if number % x == 0:
                print("Luku ei ole alkuluku.")
                break
        else:
            print("Luku on alkuluku.")