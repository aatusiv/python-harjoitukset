def print_rules():

    # Printtaa pelin ohjeet
    with open("peli/ohjeet.txt", "r", encoding="utf-8") as file:
        instructions = file.read()
    print(instructions)
    input("Enter jatkaaksesi.")

def print_intro():

    # Printtaa pelin intron
    with open("peli/intro.txt", "r", encoding="utf-8") as file:
        instructions = file.read()
    print(instructions)
    input("Enter jatkaaksesi.")

if __name__ == "__main__":
    print_rules()
    print_intro()