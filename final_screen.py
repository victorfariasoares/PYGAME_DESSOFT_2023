import pygame
import random
import os 
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, RED, WHITE

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy')

# Carrega o fundo da tela inicial
background = pygame.image.load(path.join(IMG_DIR, 'img_final_jubilado_again.jpeg')).convert()
background_rect = background.get_rect()

# Carrega o yes
yes_button = pygame.image.load(path.join(IMG_DIR, 'final_screen_yes_button.jpg')).convert_alpha()

# Carrega o botão de start
no_button = pygame.image.load(path.join(IMG_DIR, 'final_screen_no_button.jpg')).convert()

background = pygame.transform.scale(background, (480, 600))
no_button = pygame.transform.scale(no_button, (326//3, 175//3))
yes_button = pygame.transform.scale(yes_button, (326//3, 175//3))

# ----- Inicia assets-------
tamanho_fonte_1 = 70
font_1 = pygame.font.SysFont(None, tamanho_fonte_1)
frase_1 = 'FLAPPY INSPER'
text_intro = font_1.render(frase_1, True, (RED))

#==== obtendo altura e largura dos frames ========
text_intro_width = text_intro.get_width()
text_intro_height = text_intro.get_height()
centro_text_intro = WIDTH // 2 - text_intro_width // 2

flappy_width = yes_button.get_width()
centro_flappy = WIDTH // 2 - flappy_width // 2

start_bottom_width = no_button.get_width()
start_bottom_height = no_button.get_height()
centro_start = WIDTH // 2 - start_bottom_width // 2

running = True
while running:
    # Processa os eventos (mouse, teclado, botão, etc).
    for event in pygame.event.get():
        # Verifica se foi fechado.
        if event.type == pygame.QUIT:
            state = QUIT
            running = False

    # verifica se o jogador começou o jogo
    status_mouse = pygame.mouse.get_pressed()
    posicao_mouse = pygame.mouse.get_pos()
    print(posicao_mouse)

    if status_mouse != (False, False, False):
        if posicao_mouse[0] <= (centro_start + start_bottom_width) and posicao_mouse[0] >= centro_start and posicao_mouse[1] >= 450 and posicao_mouse[1] <= (start_bottom_height + 450):
            state = GAME
            running = False

    # ----- Gera saídas
    window.fill((BLACK))  # Preenche com a cor preta
    window.blit(background, background_rect)
    window.blit(text_intro, (centro_text_intro, 20))
    window.blit(yes_button, (90, 504))
    window.blit(no_button, (293, 504))

    pygame.display.flip()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador