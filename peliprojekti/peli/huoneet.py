class Huone():

    def __init__(self, name, desc, nearby_rooms, items):
        self.name = name
        self.desc = desc
        self.nearby_rooms = nearby_rooms
        self.items = items

makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat...", {"etelä" : "olohuone"}, [])
olohuone = Huone("olohuone", "Televisio on päällä.", {"pohjoinen" : "makuuhuone", "länsi" : "työhuone", "itä" : "keittiö"}, ["kissanminttu"])
työhuone = Huone("työhuone", "Työhuoneessa on tietokone", {"itä" : "olohuone"}, ["koiranluu", "lankakerä"])
keittiö = Huone("keittiö", "Keittiössä on foo...", {"länsi" : "olohuone", "pohjoinen" : "kodinhoitohuone"}, ["nakki", "raksuja"])
kodinhoitohuone = Huone("kodinhoitohuone", "Kodinhoitohuoneessa on jotain", {"etelä" : "keittiö"}, ["kinkkuviipale"])
vessa = Huone("vessa", "Vessassa ei ole mitään", {"etelä" : "kodinhoitohuone"}, ["vessapaperi"])

all_rooms = {"makuuhuone" : makuuhuone, "olohuone" : olohuone, "keittiö" : keittiö, "työhuone" : työhuone, "kodinhoitohuone" : kodinhoitohuone, "vessa": vessa}


if __name__ == "__main__":
    # Testit
    makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat", {"pohjoinen" : "keittiö"}, ["kissanminttu"])
    print(makuuhuone.name, makuuhuone.desc, makuuhuone.nearby_rooms["pohjoinen"], makuuhuone.items)