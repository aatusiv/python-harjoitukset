import random

dots = int(input("Anna pisteiden kokonaismäärä: "))
dots_in = 0
counter = 0

while counter < dots:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if (x**2 + y**2) < 1:
        dots_in += 1

    counter += 1

print(4*dots_in/dots)