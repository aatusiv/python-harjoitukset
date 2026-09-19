class Kissa():

    def __init__(self, name, score, bag, location):
        self.name = name
        self.score = score
        self.bag = bag
        self.location = location

    def move(self):
        pass

    def pick_item(self):
        pass

if __name__ == "__main__":
    # Testit
    kissa = Kissa("Testinimi", 34, ["kissanminttu", "lankapallo"], "olohuone")
    print(kissa.name, kissa.score, kissa.bag, kissa.location)