import random

def throw_dice(faces):
    return random.randint(1,faces)

max_faces = int(input("Anna tahkojen määrä: "))

while True:
    number = throw_dice(max_faces)
    print(f"Silmäluku: {number}")
    if number == max_faces:
        break