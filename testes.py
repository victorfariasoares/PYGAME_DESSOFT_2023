import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, IMG_DIR
from os import path
from init_screen import init_screen
#from game_screen import game_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)



flappy = pygame.image.load(path.join(IMG_DIR, 'bird.png')).convert_alpha()

flappy_width = flappy.get_width()
flappy_height = flappy.get_height()

print(flappy_width)
print(flappy_height)

pygame.quit()