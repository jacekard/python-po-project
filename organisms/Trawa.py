from organisms.Roslina import Roslina

class Trawa(Roslina):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(0, 0, 0, "TRAWA", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Trawa(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        #self.swiat.sortujInicjatywa()



