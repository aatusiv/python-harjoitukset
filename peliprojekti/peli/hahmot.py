class Kissa():

    def __init__(self, name, score, bag, location):
        self.name = name
        self.score = score
        self.bag = set(bag)
        self.location = location
        self.devices_off = set()

    def move(self, room):
        self.location = room

    def pick_item(self, item):
        if item not in self.bag:
            self.bag.add(item)
            given_points = item_scores.get(item, 0)
            self.score += given_points
            input(f"\nErnesti otti esineen: {item}. +{given_points} pistettä")
        else:
            input(f"\nEsine '{item}' on jo otettu.")

    def turn_off(self, device):
        if device not in self.devices_off:
            self.devices_off.add(device)
            self.score += 10
            input(f"\nErnesti sammutti laitteen: {device}. +10 pistettä")
        else:
            input(f"\nLaite '{device}' on jo sammutettu.")


item_scores = {"kinkkuviipale" : 20, "nakki" : 15, "kissanminttu" : 10, "raksuja" : 5, "lankakerä" : 2, "vessapaperirulla" : 2, "koiranluu" : 0}


if __name__ == "__main__":
    # Testit
    kissa = Kissa("Testinimi", 34, ["kissanminttu", "lankapallo"], "olohuone")
    print(kissa.name, kissa.score, kissa.bag, kissa.location)
    kissa.move("makuuhuone")
    kissa.pick_item("lamppu")
    print(kissa.name, kissa.score, kissa.bag, kissa.location)