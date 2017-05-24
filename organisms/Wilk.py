from organisms.Zwierze import Zwierze

class Wilk(Zwierze):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(5, 9, 0, "WILK", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Wilk(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.sortuj()
        print("Urodzil sie maly wilk!")




