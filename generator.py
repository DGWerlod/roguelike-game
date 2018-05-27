import math, random, constants
from img import images
from copy import deepcopy
from objects.enemy import Enemy
from objects.door import Door
from logic import matrices
from rooms import standard, shop, dish, risk, boss

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
            e.x += random.randint(0,300)-150
            e.y += random.randint(0,300)-150
    return room

def startFloor():
    nextRooms = []
    nextFloor = [[None,None,None,None,None],
                [None,None,None,None,None],
                [None,None,None,None,None],
                [None,None,None,None,None],
                [None,None,None,None,None]]
    numRooms = 8 + random.randint(0,4)
    for i in range(numRooms):
        nextRooms.append(randomizeSpawn(deepcopy(standard[random.randint(0,len(standard)-1)])))
    nextRooms.append(randomizeSpawn(deepcopy(shop[random.randint(0,len(shop)-1)])))
    nextRooms.append(randomizeSpawn(deepcopy(dish[random.randint(0,len(dish)-1)])))
    nextRooms.append(randomizeSpawn(deepcopy(risk[random.randint(0,len(risk)-1)])))
    nextRooms.append(randomizeSpawn(deepcopy(boss[random.randint(0,len(boss)-1)])))

    for i in range(len(nextRooms)):
        while True:
            pos = math.floor(random.randint(0,(constants.gridLength**2)-1))
            if nextFloor[math.floor(pos/constants.gridLength)][pos%constants.gridLength] == None:
                nextFloor[math.floor(pos/constants.gridLength)][pos%constants.gridLength] = nextRooms[i]
                break

    # for y in range(5):
    #     out = ""
    #     for x in range(5):
    #         if not nextFloor[y][x] == None:
    #             out = out + "y "
    #         else:
    #             out = out + "n "
    #     print(out)

    for i in range(constants.gridLength**2):
        yPos = math.floor(i/constants.gridLength)
        xPos = i%constants.gridLength
        if not nextFloor[yPos][xPos] == None: # Only do if there is a room here
                while True:
                    # print("LOOP VALIDATE")
                    if not validatePos(nextFloor,yPos,xPos):
                     # Move the room so it will have an adjacent room
                        temp = nextFloor[yPos][xPos]
                        nextFloor[yPos][xPos] = None
                        nextPos = yPos*constants.gridLength + xPos + 1
                        while True:
                            # print("LOOP REASSIGN")
                            nextPos = nextPos % (constants.gridLength**2)
                            yPos, xPos = math.floor(nextPos/constants.gridLength), nextPos%constants.gridLength
                            if nextFloor[yPos][xPos] == None:
                                nextFloor[yPos][xPos] = temp
                                break
                            else:
                                nextPos += 1
                                # print("NextPos: ", nextPos)
                    else: # Pos is valid finally
                        break

    testFloor = [[None,None,None,None,None],
                [None,None,None,None,None],
                [None,None,None,None,None],
                [None,None,None,None,None],
                [None,None,None,None,None]]
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

    for y in range(constants.gridLength):
        out = ""
        for x in range(constants.gridLength):
            if testFloor[y][x] == 'f':
                out = out + "1 "
            else:
                out = out + "0 "
        print(out)

    return nextFloor

# Resets all data specific to this instance of these rooms
def prepareFloor(nextFloor):
    for i in nextFloor:
        for j in i:
            if not j == None:
                j["doors"] = []
                for key in j:
                    for k in j[key]:
                        if key == "enemies": pass
                        elif key == "items":
                            k.consumedFlag = False

# links adjacent rooms with doors
def linkFloor(nextFloor):
    for i in range(len(nextFloor)):
        for j in range(len(nextFloor[i])):
            if not nextFloor[i][j] == None:
                if j > 0 and not nextFloor[i][j-1] == None:
                    nextFloor[i][j]["doors"].append(Door(0,(constants.gameH-constants.doorWide)/2,constants.doorSlim,constants.doorWide,nextFloor[i][j-1]["type"],"a"))
                if j < constants.gridLength-1 and not nextFloor[i][j+1] == None:
                    nextFloor[i][j]["doors"].append(Door(constants.gameW-constants.doorSlim,(constants.gameH-constants.doorWide)/2,constants.doorSlim,constants.doorWide,nextFloor[i][j+1]["type"],"d"))
                if i > 0 and not nextFloor[i-1][j] == None:
                    nextFloor[i][j]["doors"].append(Door((constants.gameW-constants.doorWide)/2,0,constants.doorWide,constants.doorSlim,nextFloor[i-1][j]["type"],"w"))
                if i < constants.gridLength-1 and not nextFloor[i+1][j] == None:
                    nextFloor[i][j]["doors"].append(Door((constants.gameW-constants.doorWide)/2,constants.gameH-constants.doorSlim,constants.doorWide,constants.doorSlim,nextFloor[i+1][j]["type"],"s"))

# Literally does everything
def newFloor():
    floor = startFloor()
    prepareFloor(floor)
    linkFloor(floor)
    return floor
