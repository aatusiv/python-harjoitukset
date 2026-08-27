import random

eka_sarja = ""
toka_sarja = ""

for x in range(0,3):
    eka_sarja += str(random.randint(0,9))
    toka_sarja += str(random.randint(1,6))
print(eka_sarja)
print(toka_sarja)