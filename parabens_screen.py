import pygame
import random
import os 
from os import path
from assets import load_assets, GAME_OVER_FONT, YES_FONT, RETURN
from config import IMG_DIR, BLACK, GAME, QUIT, WIDTH, HEIGHT, RED, GAME, WHITE

pygame.init()

def parabens_screen(screen):
    assets = load_assets()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'background.jpeg')).convert()
    background_rect = background.get_rect()

    #========= Cria o GAME OVER, PARABÉNS
    text_game = assets[GAME_OVER_FONT].render('PARABÉNS', True, RED)
    game_rect = text_game.get_rect()
    game_rect.midtop = (WIDTH // 2, 50)

    text_game_height = text_game.get_height()

    #========== Cria pergunta
    text_return = assets[RETURN].render('AGORA VOCÊ É', True, WHITE)
    return_rect = text_return.get_rect()
    return_rect.midtop = (WIDTH // 2, 85 + text_game_height)

    return_height = text_return.get_height()

    text_return_1 = assets[RETURN].render('UM ENGENHEIRO', True, WHITE)
    return_rect_1 = text_return_1.get_rect()
    return_rect_1.midtop = (WIDTH // 2, 88 + text_game_height + return_height)

    return_height_1 = text_return_1.get_height()

    running = True
    while running:
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                pygame.quit()
                
        # ----- Gera saídas
        screen.blit(background, background_rect)
        screen.blit(text_game, game_rect)
        screen.blit(text_return, return_rect)
        screen.blit(text_return_1, return_rect_1)

        pygame.display.flip()