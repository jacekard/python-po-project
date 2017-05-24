from _operator import attrgetter

from organisms.Antylopa import Antylopa
from organisms.Barszcz import Barszcz
from organisms.Cyberowca import Cyberowca
from organisms.Czlowiek import Czlowiek
from organisms.Guarana import Guarana
from organisms.Jagody import Jagody
from organisms.Lis import Lis
from organisms.Mlecz import Mlecz
from organisms.Owca import Owca
from organisms.Wilk import Wilk
from organisms.Trawa import Trawa
from organisms.Zolw import Zolw

class Swiat:
    def __init__(self, WIDTH=None, HEIGHT=None):
        self.width = WIDTH
        self.height = HEIGHT

        self.lista = []

        self.world = []
        for i in range(self.height):
            x = []
            for j in range(self.width):
                x.append(None)
            self.world.append(x)



        self.player = Czlowiek(self)

        self.lista.append(self.player)

        LICZBA_ZWIERZAT = 1
        LICZBA_ROSLIN = 2
        for x in range(LICZBA_ZWIERZAT):
            self.lista.append(Cyberowca(self))
            self.lista.append(Wilk(self))
            self.lista.append(Zolw(self))
            self.lista.append(Owca(self))
            self.lista.append(Lis(self))
            self.lista.append(Antylopa(self))

        for x in range(LICZBA_ROSLIN):
            self.lista.append(Trawa(self))
            self.lista.append(Mlecz(self))
            self.lista.append(Barszcz(self))
            self.lista.append(Guarana(self))
            self.lista.append(Jagody(self))

        self.turnCount = 0
        self.czyKoniec = False
        self.czySave = False
        self.czyLoad = False
        self.tarczaAlzura = False
        self.ifKeyWasPressed = False

        for obj in self.lista:
            if obj.getWiek() == -1:
                self.lista.remove(obj)

        self.sortuj()

    def wykonajTure(self):
        for obj in self.lista:
            if obj.getWiek() != -1:
                obj.akcja()

        for obj in self.lista:
            if obj.getWiek() == -1:
                self.lista.remove(obj)

        self.addTurn()

    def setTarcza(self, bool):
        self.tarczaAlzura = bool

    def addTurn(self):
        self.turnCount+=1

    def setKoniec(self):
        self.czyKoniec = True

    def sortuj(self):
        sorted(self.lista, key=attrgetter('inicjatywa'))

    def save(self):

        with open("saves/save.txt", "w") as file:
            for obj in self.lista:
                file.write("%s %d %d\n" % (obj.getRodzaj(), obj.getPosx(), obj.getPosy()))

        file.close()

    def load(self):

        self.lista = []
        self.player = None
        self.world = []

        for i in range(self.height):
            x = []
            for j in range(self.width):
                x.append(None)
            self.world.append(x)

        file = open("saves/save.txt", "r")

        for line in file:
            typ, _x, _y = line.split()
            _x = int(_x)
            _y = int(_y)
            self.addNewOrganism(typ, _x, _y)


    def addNewOrganism(self, rodzaj, x, y):
        if rodzaj == "CZLOWIEK":
            self.player = Czlowiek(self, x, y)
            self.lista.append(self.player)
        elif rodzaj == "WILK":
            self.lista.append(Wilk(self, x, y))
        elif rodzaj == "OWCA":
            self.lista.append(Owca(self, x, y))
        elif rodzaj == "CYBEROWCA":
            self.lista.append(Cyberowca(self, x, y))
        elif rodzaj == "LIS":
            self.lista.append(Lis(self, x, y))
        elif rodzaj == "ZOLW":
            self.lista.append(Zolw(self, x, y))
        elif rodzaj == "ANTYLOPA":
            self.lista.append(Antylopa(self, x, y))
        elif rodzaj == "TRAWA":
            self.lista.append(Trawa(self, x, y))
        elif rodzaj == "MLECZ":
            self.lista.append(Mlecz(self, x, y))
        elif rodzaj == "JAGODY":
            self.lista.append(Jagody(self, x, y))
        elif rodzaj == "GUARANA":
            self.lista.append(Guarana(self, x, y))
        elif rodzaj == "BARSZCZ":
            self.lista.append(Barszcz(self, x, y))