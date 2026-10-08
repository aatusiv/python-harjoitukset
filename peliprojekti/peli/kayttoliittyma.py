import subprocess, os
def printStats(location, time, score, bag):
    clear_screen()
    # Formatoitu status ikkuna josta voi seurata pisteitä, aikaa, huonetta sekä reppua(esineitä) 
    loc_text = f"Sijainti: {location}"
    score_text = f"Pisteet: {score}"
    time_text = f"Aika: {time}"
    bag_text = f"Reppu: {", ".join(bag)}"
    print("=" * 140)
    print(f"| {loc_text:^65} | {time_text:^68} |\n| {score_text:^65} | {bag_text:^68} |")
    print("=" * 140)

def clear_screen():
    # Puhdistaa näytön ja printtaa statuksen, tarkastaa käyttiksen
    if os.name == "nt":
        cmd = "cls"
    else:
        cmd = "clear"
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    printStats("olohuone", "02:00", 30, ["virveli", "imuri", "kissanminttu", "tuoli", "auto", "kirja"])