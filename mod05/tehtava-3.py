values = []

while True:
    value = input("Anna luku: ")
    if value == "":
        break
    else:
        values.append(int(value))

values.sort()
try:
    print(f"Pienin luku on {values[0]} ja suurin luku on {values[-1]}.")
except:
    print("Et ole antanut lukuja.")
    