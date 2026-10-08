class Huone():

    def __init__(self, name, desc, nearby_rooms, items, devices):
        self.name = name
        self.desc = desc
        self.nearby_rooms = nearby_rooms
        self.items = items
        self.devices = devices

makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat... Pitää olla hiljaa.", {"etelä" : "olohuone"}, [], [])
olohuone = Huone("olohuone", "Televisio on päällä illalta päälle....", {"pohjoinen" : "makuuhuone", "länsi" : "työhuone", "itä" : "keittiö"}, ["kissanminttu"],  ["televisio"])
työhuone = Huone("työhuone", "Työhuoneessa on tietokone, joka on unohtunut päälle.", {"itä" : "olohuone"}, ["koiranluu", "lankakerä"], ["tietokone"])
keittiö = Huone("keittiö", "Keittiössä on pöydälle jäänyt nakkeja.", {"länsi" : "olohuone", "pohjoinen" : "kodinhoitohuone"}, ["nakki", "raksuja"], [])
kodinhoitohuone = Huone("kodinhoitohuone", "Kodinhoitohuonetta vartioi koira, sitä pitää harhauttaa.", {"etelä" : "keittiö"}, ["kinkkuviipale"], [])
vessa = Huone("vessa", "Vessassa on hämärää ja lattialla paperirulla.", {"etelä" : "kodinhoitohuone"}, ["vessapaperi"], [])

all_rooms = {"makuuhuone" : makuuhuone, "olohuone" : olohuone, "keittiö" : keittiö, "työhuone" : työhuone, "kodinhoitohuone" : kodinhoitohuone, "vessa": vessa}


if __name__ == "__main__":
    # Testit
    makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat", {"pohjoinen" : "keittiö"}, ["kissanminttu"])
    print(makuuhuone.name, makuuhuone.desc, makuuhuone.nearby_rooms["pohjoinen"], makuuhuone.items)