import pygame
import constants
pygame.font.init()

author = constants.muli["70"].render("Created by",True,constants.white)
authorRECT = author.get_rect(centerx = constants.gameW/2, top = constants.gameH/2 - 160)

authors = constants.muli["30"].render("Daniel DeAnda and Desmond Kamas",True,constants.white)
authorsRECT = authors.get_rect(centerx = constants.gameW/2, top = constants.gameH/2 - 70)

tool = constants.muli["70"].render("Created with",True,constants.white)
toolRECT = tool.get_rect(centerx = constants.gameW/2, top = constants.gameH/2 - 10)

tools = constants.muli["30"].render("Python | Pygame | Atom | GitHub | Love",True,constants.white)
toolsRECT = tools.get_rect(centerx = constants.gameW/2, top = constants.gameH/2 + 80)

begin = constants.muli["30"].render("Press Enter", True, constants.lightPurple)
beginRECT = begin.get_rect(right = constants.gameW - 20, bottom = constants.gameH - 15)

authorsList = [[author, authorRECT], [authors, authorsRECT], [tool, toolRECT], [tools, toolsRECT], [begin, beginRECT]]

spud = constants.muli["70"].render("Chef Spud",True,constants.black)
spudRECT = spud.get_rect(left = 350, top = 175)

pause = constants.muli["20"].render("Now paused | Press ESC to resume.",True,constants.black)
pauseRECT = pause.get_rect(left = 385, top = 275)

gameOver = constants.muli["70"].render("Game Over",True,constants.black)
gameOverRECT = gameOver.get_rect(center = (constants.gameW/2,constants.gameH/2 - 30))

retry = constants.muli["30"].render("Press Enter to Restart",True,constants.black)
retryRECT = retry.get_rect(center = (constants.gameW/2,constants.gameH/2 + 30))