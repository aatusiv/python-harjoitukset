sukupuoli = input("Anna sukupuoli: ").upper()
hgl_arvo = float(input("Anna hemoglobiini arvo: "))

if sukupuoli == 'MIES':
    if hgl_arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hgl_arvo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == 'NAINEN':
    if hgl_arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hgl_arvo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
else:
    print("Virheellinen sukupuoli.")