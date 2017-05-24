from random import randint

from appJar import gui
from main.Swiat import Swiat

class UI:
    def __init__(self):
        self.app = gui("Wirtualny swiat","400x250")
        self.app.setInPadX(50)
        self.app.setInPadY(50)
        self.app.setBg("white")
        self.init()

    def press(self, btn):
        if btn == "Exit":
            self.app.stop()
        else:
            self.width = self.app.getEntry('width')
            self.height = self.app.getEntry('height')
            self.gameScreen()

    def next_turn(self, btn=None):
        if self.swiat.czyKoniec == True:
            self.game.stop()
        else:
            self.swiat.wykonajTure()
            self.draw()

    def tarcza_alzura(self, btn):
        self.swiat.player.skill()

    def save(self, btn):
        self.swiat.save()

    def load(self, btn):
        self.swiat.load()
        self.draw()


    def draw(self):
        for i in range(int(self.height)):
            for j in range(int(self.width)):

                id = randint(1,9999999999)

                if self.swiat.world[i][j] is not None:
                    rodzaj = self.swiat.world[i][j].getRodzaj()
                    if rodzaj == "CZLOWIEK":
                        self.game.addImage(str(id), "sprites/CZLOWIEK.gif", i, j, 0)
                    elif rodzaj == "WILK":
                        self.game.addImage(str(id), "sprites/WILK.gif", i, j, 0)
                    elif rodzaj == "OWCA":
                        self.game.addImage(str(id), "sprites/OWCA.gif", i, j, 0)
                    elif rodzaj == "CYBEROWCA":
                        self.game.addImage(str(id), "sprites/CYBEROWCA.gif", i, j, 0)
                    elif rodzaj == "LIS":
                        self.game.addImage(str(id), "sprites/LIS.gif", i, j, 0)
                    elif rodzaj == "ZOLW":
                        self.game.addImage(str(id), "sprites/ZOLW.gif", i, j, 0)
                    elif rodzaj == "ANTYLOPA":
                        self.game.addImage(str(id), "sprites/ZOLW.gif", i, j, 0)
                    elif rodzaj == "TRAWA":
                        self.game.addImage(str(id), "sprites/TRAWA.gif", i, j, 0)
                    elif rodzaj == "MLECZ":
                        self.game.addImage(str(id), "sprites/MLECZ.gif", i, j, 0)
                    elif rodzaj == "JAGODY":
                        self.game.addImage(str(id), "sprites/JAGODY.gif", i, j, 0)
                    elif rodzaj == "GUARANA":
                        self.game.addImage(str(id), "sprites/GUARANA.gif", i, j, 0)
                    elif rodzaj == "BARSZCZ":
                        self.game.addImage(str(id), "sprites/BARSZCZ.gif", i, j, 0)
                else:
                    self.game.addImage(str(id), "sprites/empty.gif", i, j, 0)

    def init(self):
        self.app.addLabel("title", "Wirtualny Świat", 0, 0, 2)
        self.app.addLabel("info", "Jacek Ardanowski - 165178", 1, 0 , 2)

        self.app.addLabel("width", "Szerokość: ", 2, 0)
        self.app.addEntry("width", 2, 1)
        self.app.addLabel("height", "Wysokość: ", 3, 0)
        self.app.addEntry("height", 3, 1)
        self.app.setEntryFocus("width")

        self.app.addButtons(["Submit", "Exit"], self.press, 6, 0, 2)
        self.app.enableEnter(self.press)

        #swiat = Swiat(20, 20)

        self.app.go()

    def gameScreen(self):
        self.app.stop()
        self.game = gui("Wirtualny Swiat - Jacek Ardanowski 165178", "450x400")
        self.game.setSticky("nw")
        self.game.setExpand("both")
        self.game.setGeom(str(int(self.width)*21), str(int(self.height)*21))

        self.game.startSubWindow("Panel", modal=False)
        self.game.showSubWindow("Panel")
        self.game.setGeom("100x150")
        self.game.setSubWindowLocation("Panel", 380, 230)
        self.game.addButton("Nowa tura", self.next_turn, 0, 0, 7)
        self.game.addButton("Save", self.save, 1, 0 ,7)
        self.game.addButton("Load", self.load, 2, 0 ,0)
        self.game.addButton("Tarcza", self.tarcza_alzura, 3, 0 ,0)

        self.game.stopSubWindow()

        # self.game.startSubWindow("Komunikaty", modal=False)
        # self.game.showSubWindow("Komunikaty")
        # self.game.setGeom("200x300")
        # self.game.setSubWindowLocation("Komunikaty", 1010, 230)
        # self.game.addLabel("komunikaty","Komunikaty: ")
        # self.game.stopSubWindow()

        self.swiat = Swiat(int(self.width), int(self.height))

        self.game.bindKey("w", self.goUP)
        self.game.bindKey("s", self.goDOWN)
        self.game.bindKey("a", self.goLEFT)
        self.game.bindKey("d", self.goRIGHT)

        self.draw()


        self.game.go()


    def goUP(self, b):
        if self.swiat.player.czyPozycjaY(self.swiat.player.pos.y - 1):
            self.swiat.player.pos.y-=1
        self.next_turn()

    def goDOWN(self, b):
        if self.swiat.player.czyPozycjaY(self.swiat.player.pos.y + 1):
            self.swiat.player.pos.y+=1
        self.next_turn()

    def goRIGHT(self, b):
        if self.swiat.player.czyPozycjaX(self.swiat.player.pos.x + 1):
            self.swiat.player.pos.x+=1
        self.next_turn()

    def goLEFT(self, b):
        if self.swiat.player.czyPozycjaX(self.swiat.player.pos.x - 1):
            self.swiat.player.pos.x-=1
        self.next_turn()
