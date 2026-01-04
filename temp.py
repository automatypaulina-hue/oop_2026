class Pojazd:
    def jedz (self):
        print("jade...")
    def hamuj (self):
        print("hamuj...")

class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Honda(Samochod):
    def __init__(self, marka):
        super().__init__(marka: "Honda", model)


