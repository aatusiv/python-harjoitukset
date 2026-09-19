class Huone():

    def __init__(self, name, desc, nearby_rooms, items):
        self.name = name
        self.desc = desc
        self.nearby_rooms = nearby_rooms
        self.items = items

makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat...", {"etelä" : "olohuone"}, [])
olohuone = Huone("olohuone", "Televisio on päällä.", {"itä" : "keittiö"}, ["kissanminttu"])
if __name__ == "__main__":
    # Testit
    makuuhuone = Huone("makuuhuone", "Ihmiset nukkuvat", {"pohjoinen" : "keittiö"}, "kissanminttu")
    print(makuuhuone.name, makuuhuone.desc, makuuhuone.nearby_rooms["pohjoinen"], makuuhuone.items)