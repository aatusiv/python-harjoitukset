import os, json

def save_game(ernesti, time, name, age):
    saved_data = {"nimi" : name, "ikä" : age, "kello" : time, "sijainti" : ernesti.location, "pisteet" : ernesti.score, "reppu" : list(ernesti.bag), "sammutetut" : list(ernesti.devices_off)}
    
    # Tallennetaan JSONiin
    with open(f"peli/data/tallennus_{name}.json", "w", encoding="UTF-8") as file:
        json.dump(saved_data, file, indent=4, ensure_ascii=False)
        
    print("\nPeli tallennettu.")


def lataa_peli(name):
    # Tarkistetetaan tallennus
    if not os.path.exists(f"peli/data/tallennus_{name}.json"):
        return None # Jos epäonnistuu, palauta none
        
    # Avataan tiedosto
    with open(f"peli/data/tallennus_{name}.json", "r", encoding="UTF-8") as file:
        ladattu_data = json.load(file)

    
    return ladattu_data # Palautetaan data main.py 