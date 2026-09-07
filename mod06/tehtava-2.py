numbers_list = []
counter = 0

while True:
    number = input("Anna luku: ")
    if number == "":
        print("Ohjelma sulkeutuu.")
        break
    numbers_list.append(int(number))
    counter += 1

numbers_list.sort(reverse=True)

print("Antamastasi luvuista suurimmat ovat: ")
for x in range(5 if counter > 5 else counter):
    print(f"{numbers_list[x]}")
