import subprocess
def printStats(location, time, score, bag):
    try:
        result = subprocess.run("clear", check=True, capture_output=True, text=True) # Puhdistaa terminalin jokaisen tulostuksen välissä
    except subprocess.CalledProcessError as e:
        print(f"Komento epäonnistui: {e.returncode}") 
        print(f"Error message: {e.stderr.strip()}")


    # Formatoitu status ikkuna josta voi seurata pisteitä, aikaa, huonetta sekä reppua(esineitä) 
    loc_text = f"Sijainti: {location}"
    score_text = f"Pisteet: {score}"
    print("=" * 140)
    print(f"| {loc_text:^65} | Aika: {time:^63}|\n| {score_text:^65} | Reppu: {", ".join(bag):^62}|")
    print("=" * 140)


if __name__ == "__main__":
    printStats("olohuone", "02:00", 30, ["virveli", "imuri", "kissanminttu", "tuoli", "auto", "kirja"])