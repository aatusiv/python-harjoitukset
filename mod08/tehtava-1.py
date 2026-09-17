months = ('talvi', 'talvi', 'kevät', 'kevät', 'kevät', 'kesä', 'kesä', 'kesä', 'syksy', 'syksy', 'syksy', 'talvi')

while True:
    month_num = int(input("Anna kuukauden numero: "))
    if month_num < 0:
        print("Ohjelma lopetetaan.")
        break

    print(months[month_num-1])

