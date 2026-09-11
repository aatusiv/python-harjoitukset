import math
def pizza_value(diameter, price):
    area = 0.25 * math.pi * pow(diameter, 2)
    price_per_sqcm = price / area
    # A = 1/4*pi*diameter**2
    # price / A = price per 1sqcm^2
    return price_per_sqcm

def main():
    while True:
        diameter = float(input("Anna pizzan halkaisija: "))

        if diameter < 0:
            print("Ohjelma sulkeutuu.")
            break

        price = float(input("Anna pizzan hinta: "))
        first_pizza = pizza_value(diameter, price)


        diameter = float(input("Anna pizzan halkaisija: "))
        price = float(input("Anna pizzan hinta: "))
        second_pizza = pizza_value(diameter, price)

        if first_pizza > second_pizza:
            # Math for % difference (x-y) / x * 100
            print(f"Toinen pizza on {((first_pizza - second_pizza) / first_pizza)*100:.2f}% halvempi. ({first_pizza:.2f}sqcm^2 vs. {second_pizza:.2f}sqcm^2)")
        elif first_pizza < second_pizza:
            print(f"Eka pizza on {((second_pizza - first_pizza) / second_pizza)*100:.2f}% halvempi ({first_pizza:.2f}sqcm^2 vs. {second_pizza:.2f}sqcm^2).")
        else:
            print("Pizzat ovat samanhintaisia.")

if __name__ == "__main__":
    main()