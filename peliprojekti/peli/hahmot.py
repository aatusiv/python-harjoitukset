class Kissa():

    def __init__(self, name, score, bag, location):
        self.name = name
        self.score = score
        self.bag = bag
        self.location = location

    def move(self, room):
        self.location = room

    def pick_item(self, item):
        self.bag.append(item)

if __name__ == "__main__":
    # Testit
    kissa = Kissa("Testinimi", 34, ["kissanminttu", "lankapallo"], "olohuone")
    print(kissa.name, kissa.score, kissa.bag, kissa.location)
    kissa.move("makuuhuone")
    kissa.pick_item("lamppu")
    print(kissa.name, kissa.score, kissa.bag, kissa.location)