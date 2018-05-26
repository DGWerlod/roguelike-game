import pygame, math, random
pygame.init()

gameW, gameH = 900, 600

ctx = pygame.display.set_mode((gameW,gameH))
pygame.display.set_caption("CircleGame")
clock = pygame.time.Clock()

def close():
    pygame.quit()
    quit()

def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()

        pygame.display.update()
        clock.tick(60)

main()
