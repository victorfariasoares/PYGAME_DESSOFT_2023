import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, RED, WHITE

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy')

# Carrega o fundo da tela inicial
background = pygame.image.load(path.join(IMG_DIR, 'background.jpeg')).convert()
background_rect = background.get_rect()

# Carrega o flappy
flappy = pygame.image.load(path.join(IMG_DIR, 'insper_logo.png')).convert_alpha()

# Carrega o botão de start
start_bottom = pygame.image.load(path.join(IMG_DIR, 'start.png')).convert()

# ----- Inicia assets-------
tamanho_fonte_1 = 70
font_1 = pygame.font.SysFont(None, tamanho_fonte_1)
frase_1 = 'FLAPPY INSPER'
text_intro = font_1.render(frase_1, True, (RED))

tamanho_fonte_2 = 25
font_2 = pygame.font.SysFont(None, tamanho_fonte_2)
frase_2 = 'CHEGUE AO FINAL DO CURSO DE ENGENHARIA'
text_descrip = font_2.render(frase_2, True, (WHITE))

#==== obtendo altura e largura dos frames ========
text_intro_width = text_intro.get_width()
text_intro_height = text_intro.get_height()
centro_text_intro = WIDTH // 2 - text_intro_width // 2

flappy_width = flappy.get_width()
centro_flappy = WIDTH // 2 - flappy_width // 2

start_bottom_width = start_bottom.get_width()
start_bottom_height = start_bottom.get_height()
centro_start = WIDTH // 2 - start_bottom_width // 2

text_descrip_width = text_descrip.get_width()
centro_text_descrip = WIDTH // 2 - text_descrip_width // 2

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
    window.blit(text_descrip, (centro_text_descrip, 85))
    window.blit(flappy, (centro_flappy, 200))
    window.blit(start_bottom, (centro_start, 450))

    pygame.display.flip()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador