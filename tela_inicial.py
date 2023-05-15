import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, RED, WHITE

pygame.init()
# ----- Gera tela principal

def init_screen(screen):
    # Carrega o fundo da tela inicial
    background = pygame.display.set_mode((WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Carrega o flappy
    flappy = pygame.image.load(path.join(IMG_DIR, 'insper_logo.png')).convert_alpha()

    flappy_width = flappy.get_width()

    # ----- Inicia assets
    tamanho_fonte_1 = 50
    font_1 = pygame.font.SysFont(None, tamanho_fonte_1)
    frase_1 = 'FLAPPY INSPER'
    text_intro = font_1.render(frase_1, True, (RED))

    tamanho_fonte_2 = 20
    font_2 = pygame.font.SysFont(None, tamanho_fonte_2)
    frase_2 = 'CHEGUE AO FINAL DO CURSO DE ENGENHARIA'
    text_descrip = font_2.render(frase_2, True, (WHITE))


    #==== obtendo altura e largura dos frames ========
    text_intro_width = text_intro.get_width()
    text_intro_height = text_intro.get_height()

    text_descrip_width = text_descrip.get_width()

    running = True
    while running:
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

        # ----- Gera saídas
        screen.fill((BLACK))  # Preenche com a cor branca
        screen.blit(text_intro, (WIDTH // 2 - text_intro_width // 2, 20))
        screen.blit(text_descrip, (WIDTH // 2 - text_descrip_width // 2, 70))
        screen.blit(flappy, (WIDTH // 2 - flappy_width // 2, 200))

        pygame.display.flip()

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state