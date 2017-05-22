from organisms.Roslina import Roslina

class Jagody(Roslina):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(99, 0, 0, "JAGODY", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Jagody(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        #self.swiat.sortujInicjatywa()

    def kolizja(self, other):
        print(other.getRodzaj() + " ginie otruty przez " + self.rodzaj)
        self.swiat.world[other.getOldPosy()][other.getOldPosx()] = None
        other.die()
        self.swiat.world[self.pos.y][self.pos.x] = None
        self.die()
