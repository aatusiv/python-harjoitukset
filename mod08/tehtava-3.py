airports = {}

while True:
    print("1. Uusi lentoasema\n2. Hae lentoaseman tiedot\n3. Lopeta ohjelma")
    selection = int(input("Anna valinta: "))
    if selection == 1:
        code = input("Anna ICAO-koodi: ")
        name = input("Anna lentoaseman nimi: ")
        airports[code] = name
        
    elif selection == 2:
        code = input("Anna lentoaseman ICAO-koodi: ")
        print("\nLentokenttä on: " + airports[code] + "\n")
    else:
        print("Ohjelma lopetetaan.")
        break