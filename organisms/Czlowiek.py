from main.point import point
from organisms.Roslina import Roslina
from organisms.Zwierze import Zwierze

class Czlowiek(Zwierze):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(5, 4, 0, "CZLOWIEK", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()
        self.coolDown = 0
        self.skillEnabled = 5

    def rozmnazanie(self):
        pass

    def akcja(self):
        self.skillEnabled-=1
        if self.skillEnabled < 0:
            self.swiat.setTarcza(False)


        if self.swiat.world[self.pos.y][self.pos.x] is not None:
            if self.swiat.tarczaAlzura is False:
                self.swiat.world[self.pos.y][self.pos.x].kolizja(self)
            elif isinstance(self.swiat.world[self.pos.y][self.pos.x], Roslina):
                self.swiat.world[self.pos.y][self.pos.x].reallocate()
                self.swiat.world[self.old_pos.y][self.old_pos.x] = None
                self.swiat.world[self.pos.y][self.pos.x] = self
            else:
                self.swiat.world[self.old_pos.y][self.old_pos.x] = None
                self.swiat.world[self.pos.y][self.pos.x] = self
        else:
            self.swiat.world[self.old_pos.y][self.old_pos.x] = None
            self.swiat.world[self.pos.y][self.pos.x] = self

        self.old_pos = point(self.pos.x, self.pos.y)

        self.grow()
        self.coolDown-=1

    def skill(self):
        if self.swiat.tarczaAlzura is False and self.coolDown <= 0:
            self.coolDown = 11
            self.skillEnabled = 5
            self.swiat.tarczaAlzura = True
            self.skillEnabled -= 1

    def czyOdbilAtak(self, atakujacy):
        if self.swiat.tarczaAlzura == True:
            atakujacy.reallocate()
            return True
        else:
            return False







