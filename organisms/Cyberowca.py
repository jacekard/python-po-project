from math import sqrt

from main.Util import Util
from main.point import point
from organisms.Zwierze import Zwierze

class Cyberowca(Zwierze):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(11, 4, 0, "CYBEROWCA", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()
        self.nearestBarszcz = None

    def ruch(self):

        if self.nearestBarszcz is None:
            self.nearestBarszcz = self.LocateBarszcz()

        if self.nearestBarszcz is None:
            tmp = super().ruch()
        else:
            tmp = point(0, 0)

            if self.pos.x < self.nearestBarszcz.getOldPosx():
                tmp.x += 1
            elif self.pos.x > self.nearestBarszcz.getOldPosx():
                tmp.x -= 1

            if self.pos.y < self.nearestBarszcz.getOldPosy():
                tmp.y += 1
            elif self.pos.y > self.nearestBarszcz.getOldPosy():
                tmp.y -= 1

            self.nearestBarszcz = None

        return tmp

    def LocateBarszcz(self):
        isFirst = True
        dist1 = 0
        barszcz = None

        for obj in self.swiat.lista:
            if obj.getRodzaj() == "BARSZCZ":
                dX = abs(obj.getPosx() - self.pos.x)
                dY = abs(obj.getPosy() - self.pos.y)

                if isFirst == True:
                    barszcz = obj
                    dist1 = sqrt(pow(dX, 2) + pow(dY, 2))
                    isFirst = False
                else:
                    dist2 = sqrt(pow(dX, 2) + pow(dY, 2))

                    if dist2 <= dist1:
                        barszcz = obj
                        dist1 = dist2

        return barszcz

    def rozmnazanie(self):
        child = Cyberowca(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.sortuj()
        print("Urodzila sie cyber owca!")

