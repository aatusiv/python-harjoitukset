import subprocess
def printStats(location, time, score, bag):

    # Formatoitu status ikkuna josta voi seurata pisteitä, aikaa, huonetta sekä reppua(esineitä) 
    loc_text = f"Sijainti: {location}"
    score_text = f"Pisteet: {score}"
    print("=" * 140)
    print(f"| {loc_text:^65} | Aika: {time:^63}|\n| {score_text:^65} | Reppu: {", ".join(bag):^62}|")
    print("=" * 140)


if __name__ == "__main__":
    printStats("olohuone", "02:00", 30, ["virveli", "imuri", "kissanminttu", "tuoli", "auto", "kirja"])