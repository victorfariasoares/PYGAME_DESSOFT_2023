import pygame
import random
from os import path
from assets import load_assets, INICIAL_SCREEN
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, RED, WHITE

pygame.init()
# ----- Gera tela principal

def init_screen(screen):

    # Carrega assets
    assets = load_assets()

    running = True
    while running:
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                pygame.quit()

        # verifica se o jogador começou o jogo
        status_mouse = pygame.mouse.get_pressed()
        posicao_mouse = pygame.mouse.get_pos()

        x_start = 85
        x_end = 414
        y_start = 377
        y_end = 436

        if status_mouse == (True, False, False):
            if posicao_mouse[0] <= x_end and posicao_mouse[0] >= x_start and posicao_mouse[1] >= y_start and posicao_mouse[1] <= y_end:
                state = GAME
                running = False

        # ----- Gera saídas
        screen.blit(assets[INICIAL_SCREEN], (0, 0))

        pygame.display.flip()

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state