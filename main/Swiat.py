from organisms.Wilk import Wilk
from organisms.Trawa import Trawa


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



        player = Trawa(self)

        self.lista.append(player)

        LICZBA_ZWIERZAT = 4
        LICZBA_ROSLIN = 10
        #for x in range(LICZBA_ZWIERZAT):
            # self.lista.append(Wilk(self))

        #for x in range(LICZBA_ROSLIN):
            # self.lista.append(Trawa(self))

        self.turnCount = 0
        self.czyKoniec = False
        self.czySave = False
        self.czyLoad = False
        self.tarczaAlzura = False
        self.ifKeyWasPressed = False

        #for i in range(lista.__len__()):
            #if lista.index(i).getWiek() == -1:
                #lista.pop(i)

        #sortujInicjatywa

    def wykonajTure(self):
        for obj in self.lista:
            if obj.getWiek() != -1:
                obj.akcja()
                print(obj)


        for obj in self.lista:
            if obj.getWiek() == -1:
                self.lista.remove(obj)

        self.addTurn()


    def addTurn(self):
        self.turnCount+=1

    def setKoniec(self):
        self.czyKoniec = True
