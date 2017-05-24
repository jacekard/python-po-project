from organisms.Roslina import Roslina

class Guarana(Roslina):
    def __init__(self, swiat, x=0, y=0):
        super().__init__(0, 0, 0, "GUARANA", swiat)
        if x != 0 and y != 0:
            self.pos.x = x
            self.pos.y = y
        self.allocate()

    def rozmnazanie(self):
        child = Guarana(self.swiat, self.pos.x, self.pos.y)
        self.swiat.lista.append(child)
        self.swiat.sortuj()

    def kolizja(self, other):
        other.setSila(other.getSila() + 3)
        super().kolizja(other)

