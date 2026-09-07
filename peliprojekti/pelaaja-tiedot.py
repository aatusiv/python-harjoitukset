import random

name = input("Anna nimesi: ")
age = int(input("Anna ikäsi: "))

if age < 12:
    print("Olet alaikäinen, peli sammuu.")
else:
    print(f"Hei, {name}")
    while True:
        print("- Kolikko\n- Kahvi\n- Villapaita\n- Lopeta")
        selection = input("Kirjoita komento: ").lower()
        if selection == "lopeta":
            print("Suljetaan peli.")
            break
        elif selection == "kolikko":
            result = random.choice(["kruuna", "klaava"])
            print(f"\nKolikon heiton tulos: {result}!\n")
        elif selection == "kahvi":
            jokes = ["Miksi kutsutaan isoa töppäystä Pauligilla?\n– Juhlamokaksi.",
                     "Tarjoilija koputti hotellihuoneen oveen ja kysyi:\n– Haluatteko kahvia vuoteeseen?Asukas vastasi: \n– Tuota, mieluummin kuppiin, kiitos.",
                     "Miten kahvi ja opiskelija eroavat toisistaan?\n– Kahvi suodattuu, opiskelija ei välttämättä."]
            result = random.choice(jokes)
            print(f"\n{result}\n")
        elif selection == "villapaita":
            print("\nSakarin\n")
        else:
            print("Tuntematon komento. Yritä uudelleen.")