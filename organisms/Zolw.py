from main.Util import Util
from main.point import point
from organisms.Zwierze import Zwierze

class Zolw(Zwierze):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(4, 4, 0, "ZOLW", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Zolw(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.lista.sort()
        print("Urodzil sie maly zolw!")

    def czyOdbilAtak(self, atakujacy):
        if(atakujacy.getSila() < 5):
            atakujacy.setPosx(atakujacy.getOldPosx())
            atakujacy.setPosy(atakujacy.getOldPosy())
            print("Zolw odbija atak!")
            return True
        else:
            return False


    def ruch(self):
        tmp = point()

        if Util.losuj(0,3) == 2:

            ruch = Util.losuj(0,3)
            if ruch == 0:
                tmp.y-=1
            elif ruch == 1:
                tmp.y+=1
            elif ruch == 2:
                tmp.x-=1
            elif ruch == 3:
                tmp.x+=1

            return tmp

