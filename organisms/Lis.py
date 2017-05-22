from main.point import point
from organisms.Zwierze import Zwierze

class Lis(Zwierze):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(3, 7, 0, "LIS", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Lis(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.lista.sort()
        print("Urodzil sie maly lis!")


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

        if (self.swiat.world[self.pos.y][self.pos.x] is not None
            and self.swiat.world[self.pos.y][self.pos.x].getSila() > self.sila):
            self.reallocate()

        if(self.swiat.world[self.pos.y][self.pos.x] is not None
           and self.swiat.world[self.pos.y][self.pos.x] != self):
            self.swiat.world[self.pos.y][self.pos.x].kolizja(self)
        else:
            self.swiat.world[self.old_pos.y][self.old_pos.x] = None
            self.swiat.world[self.pos.y][self.pos.x] = self

