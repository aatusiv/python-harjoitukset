import os, json

FILE_NAME = f"peli/data/tallennus.json"

def save_game(ernesti, time, name, age):
    saved_data = {"nimi" : name, "ikä" : age, "kello" : time, "sijainti" : ernesti.location, "pisteet" : ernesti.score, "reppu" : list(ernesti.bag), "sammutetut" : list(ernesti.devices_off)}
    
    # Tallennetaan JSONiin
    with open(FILE_NAME, "w", encoding="UTF-8") as file:
        json.dump(saved_data, file, indent=4, ensure_ascii=False)
        
    print("\nPeli tallennettu.")


def lataa_peli():
    # Tarkistetetaan tallennus
    if not os.path.exists(FILE_NAME):
        #print("\nTallennusta ei löytynyt")
        return None # Jos epäonnistuu, palauta none
        
    # Avataan tiedosto
    with open(FILE_NAME, "r", encoding="UTF-8") as file:
        ladattu_data = json.load(file)
    print(ladattu_data)
    print("\nPeli ladattu onnistuneesti!")
    return ladattu_data # Palautetaan data main.py 