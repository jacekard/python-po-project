from main.point import point
from main.Util import Util
from abc import ABC, abstractmethod

class Organizm:
    def __init__(self, sila, inicjatywa, wiek, rodzaj, swiat):
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.wiek = wiek
        self.rodzaj = rodzaj
        self.pos = point()
        self.old_pos = point()
        self.swiat = swiat
        self.pos.x = Util.losuj(1, swiat.width - 1)
        self.pos.y = Util.losuj(1, swiat.height - 1)
        self.old_pos = point(self.pos.x, self.pos.y)

    @abstractmethod
    def rozmnazanie(self):
        pass

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, other):
        pass

    #getters
    def getPosx(self):
        return self.pos.x

    def getOldPosx(self):
        return self.old_pos.x

    def getPosy(self):
        return self.pos.y

    def getOldPosy(self):
        return self.old_pos.y

    def getSila(self):
        return self.sila

    def getInicjatywa(self):
        return self.inicjatywa

    def getRodzaj(self):
        return self.rodzaj

    def getWiek(self):
        return self.wiek

    #setters
    def setPosx(self, x):
        self.pos.x = x

    def setPosy(self, y):
        self.pos.x = y

    def setSila(self, sila):
        self.sila = sila

    def czyDozwolonyRuch(self, poz):
        correctX = True
        correctY = True

        if(poz.x > self.swiat.width - 1 or poz.x < 0):
            correctX = False

        if(poz.y > self.swiat.height - 1 or poz.y < 0):
            correctY = False

        if(correctX and correctY):
            return True
        else:
            return False

    def czyPozycjaX(self, x):
        if (x > self.swiat.width - 1 or x < 0):
            return False
        else:
            return True

    def czyPozycjaY(self, y):
        if (y > self.swiat.height - 1 or y < 0):
            return False
        else:
            return True

    def grow(self):
        self.wiek += 1

    def die(self):
        if(self.rodzaj == "CZLOWIEK"):
            self.swiat.setKoniec()
        else:
            self.wiek = -1

    def allocate(self):
        if(self.swiat.world[self.pos.y][self.pos.x] is None):
            self.swiat.world[self.pos.y][self.pos.x] = self
        else:
            self.reallocate()

    def reallocate(self):
        rand = Util.losuj(1,4)

        for i in range(0,4):
            kierunek = (rand + i) % 4 + 1

            if kierunek == 1:
                tmp = point(self.pos.x, self.pos.y)
                tmp.y -= 1
                if (self.czyDozwolonyRuch(tmp)
                    and self.swiat.world[tmp.y][tmp.x] is None):
                    self.swiat.world[tmp.y][tmp.x] = self
                    self.pos = tmp
                    return

            elif kierunek == 2:
                tmp = point(self.pos.x, self.pos.y)
                tmp.y += 1
                if (self.czyDozwolonyRuch(tmp)
                    and self.swiat.world[tmp.y][tmp.x] is None):
                    self.swiat.world[tmp.y][tmp.x] = self
                    self.pos = tmp
                    return

            elif kierunek == 3:
                tmp = point(self.pos.x, self.pos.y)
                tmp.x -= 1
                if (self.czyDozwolonyRuch(tmp)
                    and self.swiat.world[tmp.y][tmp.x] is None):
                    self.swiat.world[tmp.y][tmp.x] = self
                    self.pos = tmp
                    return

            elif kierunek == 4:
                tmp = point(self.pos.x, self.pos.y)
                tmp.x += 1
                if (self.czyDozwolonyRuch(tmp)
                    and self.swiat.world[tmp.y][tmp.x] is None):
                    self.swiat.world[tmp.y][tmp.x] = self
                    self.pos = tmp
                    return


    def ruch(self):
        ruch = Util.losuj(0,3)
        tmp = point(0, 0)
        if ruch == 0:
            tmp.y-=1
        elif ruch == 1:
            tmp.y+=1
        elif ruch == 2:
            tmp.x-=1
        elif ruch == 3:
            tmp.x+=1

        return tmp

    def __str__(self):
       return self.rodzaj + " [" + str(self.pos.x) + "," + str(self.pos.y) + "]"

