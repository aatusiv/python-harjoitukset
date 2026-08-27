# Tavaroiden painot grammoissa vakiona
LUOTI_PAINO = 13.3
NAULA_PAINO = LUOTI_PAINO * 32
LEIVISKA_PAINO = NAULA_PAINO * 20

# Kysyy käyttäjältä lukuarvot
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Laskee painon
yhteispaino = leiviskat*LEIVISKA_PAINO + naulat*NAULA_PAINO + luodit*LUOTI_PAINO
kilot = yhteispaino / 1000
grammat = yhteispaino % 1000

# Tulostaa arvot
print(f"Massa nykymittjoen mukaan:\n{kilot:.0f} kilogrammaa ja {grammat:.2f} grammaa.")