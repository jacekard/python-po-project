from main.Util import Util
from organisms.Roslina import Roslina
from organisms.Zwierze import Zwierze


class Barszcz(Roslina):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(10, 0, 0, "BARSZCZ", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Barszcz(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.sortuj()

    def kolizja(self, other):
        if other.getRodzaj() != "CYBEROWCA":
            print(other.getRodzaj() + " ginie otruty przez " + self.rodzaj)
            self.swiat.world[other.getOldPosy()][other.getOldPosx()] = None
            other.die()
            self.swiat.world[self.pos.y][self.pos.x] = None
            self.die()
        else:
            self.die()
            self.swiat.world[other.old_pos.y][other.old_pos.x] = None
            self.swiat.world[self.pos.y][self.pos.x] = other



    def akcja(self):
        self.grow()
        if Util.losuj(1, 50) == 1:
            if self.rozsiewanie() == True:
                self.rozmnazanie()

        if self.czyPozycjaX(self.pos.x+1) == True:
            if isinstance(self.swiat.world[self.pos.y][self.pos.x+1], Zwierze):
                other = self.swiat.world[self.pos.y][self.pos.x + 1]
                if other.getRodzaj() != "CYBEROWCA":
                    other.die()
                    print(other.getRodzaj() + "jest otruty przez barszcz!")

        if self.czyPozycjaX(self.pos.x - 1) == True:
            if isinstance(self.swiat.world[self.pos.y][self.pos.x - 1], Zwierze):
                other = self.swiat.world[self.pos.y][self.pos.x - 1]
                if other.getRodzaj() != "CYBEROWCA":
                    other.die()
                    print(other.getRodzaj() + "jest otruty przez barszcz!")

        if self.czyPozycjaY(self.pos.y - 1) == True:
            if isinstance(self.swiat.world[self.pos.y - 1][self.pos.x], Zwierze):
                other = self.swiat.world[self.pos.y - 1][self.pos.x]
                if other.getRodzaj() != "CYBEROWCA":
                    other.die()
                    print(other.getRodzaj() + "jest otruty przez barszcz!")

        if self.czyPozycjaY(self.pos.y + 1) == True:
            if isinstance(self.swiat.world[self.pos.y + 1][self.pos.x], Zwierze):
                other = self.swiat.world[self.pos.y + 1][self.pos.x]
                if other.getRodzaj() != "CYBEROWCA":
                    other.die()
                    print(other.getRodzaj() + "jest otruty przez barszcz!")
