# Kysyy kolme kokonaislukua
eka_luku, toka_luku, kolmas_luku = map(int, input("Anna kolme kokonaislukua: ").split())

# Laskee summan, tulon ja keskiarvon
summa = eka_luku + toka_luku + kolmas_luku
tulo = eka_luku * toka_luku * kolmas_luku
keskiarvo = summa / 3

# Tulostaa arvot
print(f"Lukujen summa: {summa}\ntulo: {tulo}\nKeskiarvo: {keskiarvo:.2f}")