import pygame
import constants
pygame.font.init()

author = constants.muli["70"].render("Created by",True,constants.white)
authorRECT = author.get_rect()
authorRECT.centerx = constants.gameW/2
authorRECT.top = constants.gameH/2 - 160
authors = constants.muli["30"].render("Daniel DeAnda and Desmond Kamas",True,constants.white)
authorsRECT = authors.get_rect()
authorsRECT.centerx = constants.gameW/2
authorsRECT.top = constants.gameH/2 - 70
tool = constants.muli["70"].render("Created with",True,constants.white)
toolRECT = tool.get_rect()
toolRECT.centerx = constants.gameW/2
toolRECT.top = constants.gameH/2 - 10
tools = constants.muli["30"].render("Python | Pygame | Atom | GitHub | Love",True,constants.white)
toolsRECT = tools.get_rect()
toolsRECT.centerx = constants.gameW/2
toolsRECT.top = constants.gameH/2 + 80

begin = constants.muli["30"].render("Press Enter", True, constants.lightPurple)
beginRECT = begin.get_rect()
beginRECT.right = constants.gameW - 20
beginRECT.bottom = constants.gameH - 15

spud = constants.muli["70"].render("Chef Spud",True,constants.black)
spudRECT = spud.get_rect()
spudRECT.left = 350
spudRECT.top = 175

pause = constants.muli["20"].render("Now paused // Press ESC to resume.",True,constants.black)
pauseRECT = pause.get_rect()
pauseRECT.left = 370
pauseRECT.top = 270

gameOver = constants.muli["70"].render("Game Over",True,constants.black)
gameOverRECT = gameOver.get_rect()
gameOverRECT.center = (constants.gameW/2,constants.gameH/2 - 30)
retry = constants.muli["30"].render("Press Enter to Restart",True,constants.black)
retryRECT = retry.get_rect()
retryRECT.center = (constants.gameW/2,constants.gameH/2 + 30)