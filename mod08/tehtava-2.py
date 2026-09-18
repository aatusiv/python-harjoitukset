all_names = set()

while True:
    name = input("Anna nimi: ")
    if name == "":
        print(all_names)
        print("Ohjelma lopetetaan.")
        break

    if name in all_names:
        print("Aiemmin syötetty nimi.")
    else:
        all_names.add(name)
        print("Uusi nimi.")