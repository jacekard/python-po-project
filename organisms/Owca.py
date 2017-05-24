from organisms.Zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(4, 4, 0, "OWCA", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Owca(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.sortuj()
        print("Urodzila sie mala owca!")

