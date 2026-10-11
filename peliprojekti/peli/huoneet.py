class Huone():

    def __init__(self, name, desc, nearby_rooms, items, devices):
        self.name = name
        self.desc = desc
        self.nearby_rooms = nearby_rooms
        self.items = items
        self.devices = devices


# Luodaan huone-oliot
makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat... Pitää olla hiljaa, jotta he eivät herää.", {"etelä" : "olohuone", "itä" : "kodinhoitohuone"}, [], [])
olohuone = Huone("olohuone", "Saavut olohuoneeseen, kuu paistaa ikkunasta sisään.", {"pohjoinen" : "makuuhuone", "etelä" : "takkahuone", "länsi" : "työhuone", "itä" : "keittiö"}, ["kissanminttu"],  ["televisio"])
työhuone = Huone("työhuone", "Työhuoneessa on tietokone, ihmisten likaisia kahvikuppeja sekä kirjoja lattialla.", {"itä" : "olohuone"}, ["koiranluu", "lankakerä"], ["tietokone"])
keittiö = Huone("keittiö", "Keittiössä on pöydälle jäänyt nakkeja.", {"länsi" : "olohuone", "pohjoinen" : "kodinhoitohuone"}, ["nakki", "raksuja"], [])
kodinhoitohuone = Huone("kodinhoitohuone", "Kodinhoitohuonetta vartioi koira, mutta hän on liian kiireinen luun kanssa huomatakseen Ernestiä.", {"etelä" : "keittiö", "pohjoinen" : "vessa", "itä" : "makuuhuone"}, ["kinkkuviipale"], [])
vessa = Huone("vessa", "Vessassa on hämärää ja lattialla paperirulla.", {"etelä" : "kodinhoitohuone"}, ["vessapaperi"], [])
takkahuone = Huone("takkahuone", "Takassa on vielä edellisen illan hiillokset.", {"pohjoinen" : "olohuone", "länsi" : "vaatehuone"}, ["lelu"], [])
vaatehuone = Huone("vaatehuone", "Vaatekorissa on likaisia vaatteita.", {"itä" : "takkahuone"}, [], ["valot"])

all_rooms = {"makuuhuone" : makuuhuone, "olohuone" : olohuone, "keittiö" : keittiö, "työhuone" : työhuone, "kodinhoitohuone" : kodinhoitohuone, "vessa": vessa, "takkahuone" : takkahuone, "vaatehuone" : vaatehuone}


if __name__ == "__main__":
    # Testit
    makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat", {"pohjoinen" : "keittiö"}, ["kissanminttu"], [])
    print(makuuhuone.name, makuuhuone.desc, makuuhuone.nearby_rooms["pohjoinen"], makuuhuone.items)