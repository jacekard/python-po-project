from main.Util import Util
from organisms.Roslina import Roslina

class Mlecz(Roslina):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(0, 0, 0, "MLECZ", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Mlecz(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.sortuj()

    def akcja(self):
        self.grow()
        for i in range(3):
            if Util.losuj(1, 50) == 1:
                if self.rozsiewanie() == True:
                    self.rozmnazanie()