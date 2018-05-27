import pygame
pygame.init()

presets = {'keyW':pygame.K_w,'keyA':pygame.K_a,'keyS':pygame.K_s,'keyD':pygame.K_d,'keySpace':pygame.K_SPACE}
controls = {'keyW':False,'keyA':False,'keyS':False,'keyD':False,'keySpace':False}

def listen(event):
        if event.type == pygame.QUIT:
            close()
        elif event.type == pygame.KEYDOWN:
            for p in presets:
                if event.key == presets[p]:
                    controls[p] = True
        elif event.type == pygame.KEYUP:
            for p in presets:
                if event.key == presets[p]:
                    controls[p] = False
