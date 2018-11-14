import pygame
pygame.mixer.init()

soundData = [
    ["chomp", 0.9],
    ["chop", 0.1],
    ["loud_thump", 0.4],
    ["squish", 0.3],
    ["paper", 0.5],
    ["slam1", 1.0],
    ["slam2", 1.0],
    ["unlock", 1.0]
]

sounds = {}
for d in soundData:
    sounds[d[0]] = pygame.mixer.Sound("sound/" + d[0] + ".ogg")
    sounds[d[0]].set_volume(d[1])

def play(name):
    sounds[name].play()

overtureGoTime = 12.730 # seconds
overtureLoopTime = 25.424 # seconds
END_FLAG = pygame.USEREVENT + 1 # ensures that this flag != any preset one

pygame.mixer.music.load("sound/overture.ogg")
# noinspection PyArgumentList
pygame.mixer.music.set_endevent(END_FLAG)

def changeMusic(time, song=None):
    if song is None:
        pygame.mixer.music.pause()
        pygame.mixer.music.rewind()
        pygame.mixer.music.play()
        pygame.mixer.music.set_pos(time)
