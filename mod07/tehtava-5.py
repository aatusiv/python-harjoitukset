def remove_uneven(numbers):
    new_lista = []
    for x in numbers:
        if numbers[x-1] % 2 == 0:
            new_lista.append(x)
    return new_lista
        

def main():
    numbers = [1,2,3,4,5,6,7,8]
    new_lista = remove_uneven(numbers)
    print(new_lista)
if __name__ == "__main__":
    main()