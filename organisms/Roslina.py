from main.point import point
from organisms.Organizm import Organizm
from main.Util import Util

class Roslina(Organizm):
    def __init__(self, sila, inicjatywa, wiek, rodzaj, swiat):
        super().__init__(sila, inicjatywa, wiek, rodzaj, swiat)

    def akcja(self):
        self.grow()
        if Util.losuj(1, 50) == 1:
            if self.rozsiewanie() == True:
                self.rozmnazanie()

    def kolizja(self, other):
        print(other.getRodzaj() + " zjada " + self.rodzaj)
        self.swiat.world[self.pos.y][self.pos.x] = other
        self.swiat.world[other.getOldPosy()][other.getOldPosx()] = None
        self.die()

    def rozsiewanie(self):
        tmp = self.ruch()

        if ((self.pos.x + tmp.x < self.swiat.width - 1 and self.pos.y + tmp.y > 1)
                and (self.pos.y + tmp.y < self.swiat.height - 1 and self.pos.y + tmp.y > 1)):
            if (self.swiat.world[self.pos.y + tmp.y][self.pos.x + tmp.x] is None):
                return True

        return False