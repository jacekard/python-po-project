from main.point import point
from organisms.Organizm import Organizm
from main.Util import Util

class Zwierze(Organizm):
    def __init__(self, sila, inicjatywa, wiek, rodzaj, swiat):
        super().__init__(sila, inicjatywa, wiek, rodzaj, swiat)

    def akcja(self):
        self.grow()

        tmp = self.ruch()

        if (self.pos.x + tmp.x > self.swiat.width - 1
            or self.pos.x + tmp.x < 1):
            tmp.x = 0
        if (self.pos.y + tmp.y > self.swiat.height - 1
            or self.pos.y + tmp.y < 1):
            tmp.y = 0

        self.old_pos = point(self.pos.x, self.pos.y)

        self.pos.x += tmp.x
        self.pos.y += tmp.y

        if(self.swiat.world[self.pos.y][self.pos.x] is not None
           and self.swiat.world[self.pos.y][self.pos.x] != self):
            self.swiat.world[self.pos.y][self.pos.x].kolizja(self)
        else:
            self.swiat.world[self.old_pos.y][self.old_pos.x] = None
            self.swiat.world[self.pos.y][self.pos.x] = self


    def kolizja(self, other):

        if (other == self):
            return

        rodzaj = other.getRodzaj()

        if (self.czyRozmnazanie(other)):
            self.rozmnazanie()
        elif (rodzaj == self.rodzaj):
            return
        elif (self.czyOdbilAtak(other) == False):
            if (other.getSila() >= self.sila):
                if (self.rodzaj == "CZLOWIEK"):
                    print(self.rodzaj + " ginie z reki " + rodzaj + "A!")
                    #swiat.komentuj(" + " + this.rodzaj + " ginie z reki " + rodzaj + "A! + ");
                else:
                    print(self.rodzaj + " ginie w paszczy " + rodzaj)
                    #swiat.komentuj(" + " + this.rodzaj + " ginie w paszczy " + rodzaj + "! + ");

                self.swiat.world[self.pos.y][self.pos.x] = other
                self.swiat.world[other.getOldPosy()][other.getOldPosx()] = None
                self.die()

            else:
                if (self.rodzaj == "CZLOWIEK"):
                    print(rodzaj + " ginie z reki " + self.rodzaj + "A!")
                else:
                    print(rodzaj + " ginie w paszczy " + self.rodzaj)
                self.swiat.world[other.getOldPosy()][other.getOldPosx()] = None
                other.die()


    def czyOdbilAtak(self, atakujacy):
        return False

    def czyRozmnazanie(self, other):
        if (self.rodzaj == other.getRodzaj()):
            if (Util.losuj(1, 4) == 2):
                if (other.getWiek() > 15 and self.wiek > 15):
                    return True
        else:
            return False


