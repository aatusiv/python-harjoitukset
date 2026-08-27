# Tavaroiden painot grammoissa vakiona
LUOTI = 13.3
NAULA = LUOTI * 32
LEIVISKA = NAULA * 20

# Kysyy käyttäjältä lukuarvot
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Laskee painon
yhteispaino = leiviskat*LEIVISKA + naulat*NAULA + luodit*LUOTI
kilot = yhteispaino / 1000
grammat = yhteispaino % 1000

# Tulostaa arvot
print(f"Massa nykymittjoen mukaan:\n{kilot:.0f} kilogrammaa ja {grammat:.2f} grammaa.")