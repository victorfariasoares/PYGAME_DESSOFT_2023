import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, CONCLUDE
from init_screen import init_screen
from game_screen import game_screen
from final_screen import finish_screen
from parabens_screen import parabens_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy')


state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == CONCLUDE:
        state = parabens_screen(window)
    else:
        state = finish_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados