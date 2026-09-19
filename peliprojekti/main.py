import pelaajatiedot, valikko

def main():
    age_check = pelaajatiedot.kysy_tiedot()
    if age_check is True:
        valikko.menu()
        
if __name__ == "__main__":
    main()