from main.Util import Util
from main.point import point
from organisms.Zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(4, 4, 0, "ANTYLOPA", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Antylopa(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.lista.sort()
        print("Urodzila sie mala antylopa!")

    def czyOdbilAtak(self, atakujacy):
        if Util.losuj(0,1) == 1:
            self.reallocate()
            return True
        else:
            return False

    def ruch(self):
        tmp = point()

        ruch = Util.losuj(0, 3)
        if ruch == 0:
            tmp.y -= 2
        elif ruch == 1:
            tmp.y += 2
        elif ruch == 2:
            tmp.x -= 2
        elif ruch == 3:
            tmp.x += 2

        return tmp
