from appJar import gui

from main.Swiat import Swiat

def pressed(self, name):
    print(name, "pressed")

class UI:
    def __init__(self):
        app = gui()
        app.addLabel("title", "Hello World")
        app.setGeom("600x400")

        app.addLabelEntry("Szerokość")
        app.setLabelFg("Szerokość", "white")
        app.addLabelEntry("Wysokość")
        app.setLabelFg("Wysokość", "white")

        app.addButton("OK", pressed)

        #swiat = Swiat(20, 20)

        app.go()

