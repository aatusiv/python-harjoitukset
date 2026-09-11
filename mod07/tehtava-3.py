def liter_to_gallons(liters):
    return liters * 3.785

def main():
    while True:
        liters = float(input("Anna litrojen määrä: "))
        gallons = liter_to_gallons(liters)
        if gallons < 0:
            print("Ohjelma sulkeutuu.")
            break

        print(f"{liters} litraa on {gallons} gallonaa.")


if __name__ == "__main__":
    main()