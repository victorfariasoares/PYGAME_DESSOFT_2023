import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from tela_inicial import init_screen
#from game_screen import game_screen
#from finish_screen import finish_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy')


state = INIT
while state != QUIT:
    state = init_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados