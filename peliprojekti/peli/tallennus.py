import os, json

FILE_NAME = "tallennus.json"

def save_game(ernesti, time):
    saved_data = {"kello" : time, "sijainti" : ernesti.location, "pisteet" : ernesti.score, "reppu" : list(ernesti.bag), "sammutetut" : list(ernesti.devices_off)}
    
    # Tallennetaan JSONiin
    with open(FILE_NAME, "w") as file:
        json.dump(saved_data, file, indent=4)
        
    print("\nPeli tallennettu.")


def lataa_peli():
    # Tarkistetetaan tallennus
    if not os.path.exists(FILE_NAME):
        print("\nTallennusta ei löytynyt")
        return None # Jos epäonnistuu, palauta none
        
    # Avataan tiedosto
    with open(FILE_NAME, "r") as file:
        ladattu_data = json.load(file)
        
    print("\nPeli ladattu onnistuneesti!")
    return ladattu_data # Palautetaan data main.py 