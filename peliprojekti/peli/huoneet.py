class Huone():

    def __init__(self, name, desc, nearby_rooms, items):
        self.name = name
        self.desc = desc
        self.nearby_rooms = nearby_rooms
        self.items = items

makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat...", {"etelä" : "olohuone"}, [])
olohuone = Huone("olohuone", "Televisio on päällä.", {"pohjoinen" : "makuuhuone", "länsi" : "työhuone", "itä" : "keittiö"}, ["kissanminttu"])
keittiö = Huone("keittiö", "Keittiössä on foo...", {"länsi" : "keittiö", "pohjoinen" : "kodinhoitohuone"}, [])
työhuone = Huone("työhuone", "Työhuoneessa on tietokone", {"itä" : "olohuone"}, [])
kodinhoitohuone = Huone("kodinhoitohuone", "Kodinhoitohuoneessa on jotain", {"etelä" : "keittiö"}, [])
vessa = Huone("vessa", "Vessassa ei ole mitään", {"etelä" : "kodinhoitohuone"}, [])

if __name__ == "__main__":
    # Testit
    makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat", {"pohjoinen" : "keittiö"}, "kissanminttu")
    print(makuuhuone.name, makuuhuone.desc, makuuhuone.nearby_rooms["pohjoinen"], makuuhuone.items)