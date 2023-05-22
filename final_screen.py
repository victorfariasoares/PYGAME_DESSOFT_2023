import pygame
import random
import os 
from os import path
from assets import load_assets, GAME_OVER_FONT, YES_FONT
from config import IMG_DIR, BLACK, GAME, QUIT, WIDTH, HEIGHT, RED

pygame.init()

def finish_screen(screen):
    assets = load_assets()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'background.jpeg')).convert()
    background_rect = background.get_rect()

    #========= Cria o GAME OVER
    text_game = assets[GAME_OVER_FONT].render('VOCÊ FOI', True, RED)
    game_rect = text_game.get_rect()
    game_rect.midtop = (WIDTH // 2, 50)

    text_game_height = text_game.get_height()

    #========== Cria segunda linha de escrita
    text_over = assets[GAME_OVER_FONT].render('JUBILADO', True, RED)
    over_rect = text_over.get_rect()
    over_rect.midtop = (WIDTH // 2, 55 + text_game_height)
    
    #========== Cria o yes
    text_yes = assets[YES_FONT].render('YES', True, BLACK)
    yes_rect = text_yes.get_rect()
    yes_rect.midtop = (125, 550)

    # encontra coordenadas
    text_yes_width = text_yes.get_width()
    text_yes_height = text_yes.get_height()

    # ========= Cria o no
    text_no = assets[YES_FONT].render('NO', True, BLACK)
    no_rect = text_no.get_rect()
    no_rect.midtop = (375, 550)

    # encontra coordenadas
    text_no_width = text_no.get_width()
    text_no_height = text_no.get_height()

    running = True
    while running:
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

        # verifica em qual botão o jogador clicou
        status_mouse = pygame.mouse.get_pressed()
        posicao_mouse = pygame.mouse.get_pos()

        # cria condicional para caso seja apertado o YES
        if status_mouse == (True, False, False):
            if posicao_mouse[0] >= 125 and posicao_mouse[0] <= 125 + text_yes_width and posicao_mouse[1] >= 650 and posicao_mouse[1] <= 650 + text_yes_height:
                state = GAME

        # ----- Gera saídas
        screen.blit(background, background_rect)
        screen.blit(text_game, game_rect)
        screen.blit(text_over, over_rect)
        screen.blit(text_yes, yes_rect)
        screen.blit(text_no, no_rect)

        pygame.display.flip()

    return state