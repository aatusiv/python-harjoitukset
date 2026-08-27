# Kysyy käyttäjältä kalan pituuden senttimetreinä
kalan_pituus = float(input("Mikä on kuhan pituus senttimetreinä: "))

if kalan_pituus < 37:
    print("Kuha on alamittainen, päästä takaisin järveen\nAlin sallittu pituus on 37cm.")
else:
    print("Kuha on sopivan mittainen.")