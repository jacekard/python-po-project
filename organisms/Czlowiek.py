from organisms.Zwierze import Zwierze

class Czlowiek(Zwierze):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(5, 9, 0, "CZLOWIEK", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()



