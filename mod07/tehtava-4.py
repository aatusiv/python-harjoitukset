def list_total(luku_lista):
    total = 0
    for x in luku_lista:
        total += x
    return total

def main():
    import random
    luku_lista = []
    for x in range(1,6):
        luku_lista.append(random.randint(1,100))
    print(list_total(luku_lista))


if __name__ == "__main__":
    main()