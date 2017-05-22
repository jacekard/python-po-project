from creatures import *
import abc

class World:
    map, kind, organisms, ui = None, None, None, None
    height, width, creatures, directions = None, None, None, None

    def __init__(self, h, w, c):
        self.height, self.width, self.creatures = h, w, c
        self.map = [[None for x in range(self.width)] for y in range(self.height)]
        self.organisms = []

        if self.CreateObject(OrganismKind.Human, Point(y=0, x=0)):
            print("Human created")
        else:
            print("Failed to create human")

        for x in range(self.creatures):
            kind = OrganismKind.RandomKind()
            loc = Point(y=random.randrange(self.height), x=random.randrange(self.width))
            self.CreateObject(kind, loc)

    def CreateObject(self, kind, location):
        if self.map[location.y][location.x] is None:
            org = Organism.SpawnFromKind(kind, self)
            org.location = deepcopy(location)
            self.organisms.append(org)
            self.map[location.y][location.x] = org
            return True
        else:
            return False

    def CheckBounds(self, loc):
        return loc.x >= 0 and loc.y >= 0 and loc.x < self.width and loc.y < self.height

    def CleanUp(self):
        org = [o for o in self.organisms if o.dead == False]
        self.organisms = org

    def Turn(self):
        initiativeQueue = [[] for x in range(8)]
        for org in self.organisms:
            initiativeQueue[org.initiative].append(org)

        for i in range(8):
            for org in initiativeQueue[i]:
                if org is None:
                    continue
                if org.dead:
                    continue
                org.Action()

    def Log(self, text):
        if self.ui is not None:
            self.ui.Log(text)

    def GetHumanAction(self):
        if self.ui is not None:
            action = self.ui.PromptForAction()
            if action == None:
                return -2
        else:
            return random.randrange(self.directions)

    def DumpData(self):
        dump = str(self.height) + " " + str(self.width) + " " + str(len(self.organisms)) + " " + self.kind + "\n"
        for org in self.organisms:
            dump += str(org.kind) + " " + str(org.strength) + " " + str(org.initiative) + " "
            dump += str(org.location.y) + " " + str(org.location.x) + "\n"

        return dump

    @abc.abstractmethod
    def SwitchDirections(self, direction, target):
        pass

    @abc.abstractmethod
    def CoordsToYX(self, point):
        pass



class GridWorld(World):
    def __init__(self, height, width, creatures):
        super(GridWorld, self).__init__(height, width, creatures)
        self.kind = WorldKind.GRID
        self.directions = 4

    def SwitchDirections(self, direction, target):
        if direction == 0:
            target.y -= 1
        elif direction == 2:
            target.y += 1
        elif direction == 3:
            target.x -= 1
        elif direction == 1:
            target.x += 1

        return target

    def CoordsToYX(self, point):
        yx = point.clone()
        yx.y = (point.y - point.y % 15) / 15
        yx.x = (point.x - point.x % 15) / 15
        return yx



class HexWorld(World):
    def __init__(self, height, width, creatures):
        super(HexWorld, self).__init__(height, width, creatures)
        self.kind = WorldKind.HEX
        self.directions = 6

    def SwitchDirections(self, direction, target):
        if direction == 0:
            target.y -= 1
        elif direction == 1:
            target.y -= 1
            target.x += 1
        elif direction == 2:
            target.x += 1
        elif direction == 3:
            target.y += 1
            target.x += 1
        elif direction == 4:
            target.y += 1
        elif direction == 5:
            target.x -= 1

        return target

    def CoordsToYX(self, point):
        yx = point.clone()
        if yx.y % 40 > 20:
            yx.x -= 10
        yx.y = (point.y - point.y % 20) / 20
        yx.x = (point.x - point.x % 20) / 20
        return yx
