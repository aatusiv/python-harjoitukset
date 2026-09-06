import random

answer = random.randint(1,10)
print("Arvaa lukuja väliltä 1-10 kunnes saat oikein")

while True:
    guess = int(input("Arvaa lukua: "))
    if guess == answer:
        print("Arvasit oikein.")
        break
    elif guess > answer:
        print("Liian suuri arvaus.")
    else:
        print("Liian pieni arvaus.")