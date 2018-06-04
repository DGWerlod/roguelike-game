import math, random, constants
from img import images
from copy import deepcopy
from logic import matrices
from rooms import start, standard, shop, dish, risk, boss
from objects.door import Door
from objects.minimap import Minimap
from objects.enemy import Enemy
from objects.spawner import Spawner
from objects.boss import Boss

floorPlan = []
for x in range(constants.gridLength):
    floorPlan.append([])
    for y in range(constants.gridLength):
        floorPlan[x].append(None)

specialLists = [shop,dish,risk,boss]

def randomPos(x,y):
    return x+random.randint(0,300)-150, y+random.randint(0,300)-150

def trySpawn(enemy, room, map):
    if not (isinstance(enemy,Boss) or isinstance(enemy,Spawner)):
        return None
    else:
        spawn = None
        if enemy.name == "peep":
            if random.randint(0,math.ceil(1000/map.level)) == 0:
                spawn = Enemy("bunny")
                if random.randint(0,math.ceil(100/map.level)) == 0: # i.e. 1 in 100,000 chance per frame
                    spawn = Boss("peep")
        elif isinstance(enemy, Spawner):
            if enemy.spawnCD == 0:
                spawn = Spawner(enemy.name,math.ceil(enemy.spawnSpd*(map.level+1)/map.level))
        if spawn != None:
            spawn.setup()
            spawn.x, spawn.y = (constants.gameW-spawn.w)/2, (constants.gameH-spawn.h)/2
            spawn.x, spawn.y = randomPos(spawn.x, spawn.y)
            room["enemies"].append(spawn)

def validatePos(nextFloor,yPos,xPos):
    validPos = False
    if not yPos == 0:
        if not nextFloor[yPos-1][xPos] == None:
            validPos = True
    if not xPos == 0:
        if not nextFloor[yPos][xPos-1] == None:
            validPos = True
    if not yPos == constants.gridLength-1:
        if not nextFloor[yPos+1][xPos] == None:
            validPos = True
    if not xPos == constants.gridLength-1:
        if not nextFloor[yPos][xPos+1] == None:
            validPos = True
    return validPos

def randomizeSpawn(room):
    for e in room["enemies"]:
        e.x, e.y = (constants.gameW-e.w)/2, (constants.gameH-e.h)/2
        if not e.name == "peep":
            e.x, e.y = randomPos(e.x, e.y)
    return room

def startFloor():
    nextRooms = [start]
    nextFloor = deepcopy(floorPlan)
    numRooms = 8 + random.randint(0,4)
    for i in range(numRooms):
        nextRooms.append(randomizeSpawn(deepcopy(standard[random.randint(0,len(standard)-1)])))
    for s in specialLists:
        nextRooms.append(randomizeSpawn(deepcopy(s[random.randint(0,len(s)-1)])))

    for i in range(len(nextRooms)):
        while True:
            pos = math.floor(random.randint(0,(constants.gridLength**2)-1))
            if nextFloor[math.floor(pos/constants.gridLength)][pos%constants.gridLength] == None:
                nextFloor[math.floor(pos/constants.gridLength)][pos%constants.gridLength] = nextRooms[i]
                break

    for i in range(constants.gridLength**2):
        yPos = math.floor(i/constants.gridLength)
        xPos = i%constants.gridLength
        if not nextFloor[yPos][xPos] == None: # Only do if there is a room here
                while True:
                    if not validatePos(nextFloor,yPos,xPos):
                     # Move the room so it will have an adjacent room
                        temp = nextFloor[yPos][xPos]
                        nextFloor[yPos][xPos] = None
                        nextPos = yPos*constants.gridLength + xPos + 1
                        while True:
                            nextPos = nextPos % (constants.gridLength**2)
                            yPos, xPos = math.floor(nextPos/constants.gridLength), nextPos%constants.gridLength
                            if nextFloor[yPos][xPos] == None:
                                nextFloor[yPos][xPos] = temp
                                break
                            else:
                                nextPos += 1
                    else: # Pos is valid finally
                        break

    testFloor = deepcopy(floorPlan)
    validX, validY = 0, 0
    for y in range(constants.gridLength):
        for x in range(constants.gridLength):
            if not nextFloor[y][x] == None:
                testFloor[y][x] = 'y'
                validX, validY = x, y
            else:
                testFloor[y][x] = 'n'

    matrices.bucketFill(testFloor,validX,validY) #bucketFill is x,y
    for y in range(constants.gridLength):
        for x in range(constants.gridLength):
            if testFloor[y][x] == 'y':
                return startFloor()

    # Print this floor to the console (deprecated: see minimap.py)
    # for y in range(constants.gridLength):
    #     out = ""
    #     for x in range(constants.gridLength):
    #         if testFloor[y][x] == 'f':
    #             out = out + "1 "
    #         else:
    #             out = out + "0 "
    #     print(out)

    return nextFloor

# Resets all data specific to this instance of these rooms
def prepareFloor(nextFloor):
    for i in nextFloor:
        for j in i:
            if not j == None:
                j["doors"] = []
                for key in j:
                    for k in j[key]:
                        if key == "enemies" or key == "items":
                            k.setup()
                        elif key == "items":
                            k.consumedFlag = False

# links adjacent rooms with doors
def linkFloor(nextFloor):
    for i in range(len(nextFloor)):
        for j in range(len(nextFloor[i])):
            if not nextFloor[i][j] == None:
                if j > 0 and not nextFloor[i][j-1] == None:
                    nextFloor[i][j]["doors"].append(Door(nextFloor[i][j-1]["type"],"a"))
                if j < constants.gridLength-1 and not nextFloor[i][j+1] == None:
                    nextFloor[i][j]["doors"].append(Door(nextFloor[i][j+1]["type"],"d"))
                if i > 0 and not nextFloor[i-1][j] == None:
                    nextFloor[i][j]["doors"].append(Door(nextFloor[i-1][j]["type"],"w"))
                if i < constants.gridLength-1 and not nextFloor[i+1][j] == None:
                    nextFloor[i][j]["doors"].append(Door(nextFloor[i+1][j]["type"],"s"))

# Literally does everything
def newFloor(level):
    floor = startFloor()
    prepareFloor(floor)
    linkFloor(floor)
    return floor

def nextFloor(map):
    if map == None: level = 1
    else: level = map.level+1
    floor = newFloor(level)
    map = Minimap(floor, level)

    # Find the start room
    for y in range(constants.gridLength):
        for x in range(constants.gridLength):
            if floor[y][x] != None and floor[y][x]["enemies"] == [] and floor[y][x]["items"] == []:
                startRoom = floor[y][x]
                startPos = [y,x]
                return floor, startRoom, startPos, map
