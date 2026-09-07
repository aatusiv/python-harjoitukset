import random

dice_amount = int(input("Anna noppien lukumäärä: "))
total = 0

for x in range(dice_amount):
    dice_number = random.randint(1,6)
    total += dice_number
print(f"Silmälukujen summa on: {total}")