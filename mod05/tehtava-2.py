while True:
    inches = float(input("Anna tuumat: "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(f"{inches} tuumaa on {cm:.2f} senttimetreinä.")