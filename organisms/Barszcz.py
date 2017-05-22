from main.Util import Util
from organisms.Roslina import Roslina

class Barszcz(Roslina):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(99, 0, 0, "BARSZCZ", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Barszcz(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        #self.swiat.sortujInicjatywa()

    def kolizja(self, other):
        if other.getRodzaj() != "CYBER-OWCA":
            print(other.getRodzaj() + " ginie otruty przez " + self.rodzaj)
            self.swiat.world[other.getOldPosy()][other.getOldPosx()] = None
            other.die()
            self.swiat.world[self.pos.y][self.pos.x] = None
            self.die()
        else:
            self.die()

    #DOPISAC AKCJE
    def akcja(self):
        self.grow()
        if Util.losuj(1, 50) == 1:
            if self.rozsiewanie() == True:
                self.rozmnazanie()
