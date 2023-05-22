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

    '''text_return_2 = assets[RETURN].render('Quer tentar', True, WHITE)
    return_rect_2 = text_return_2.get_rect()
    return_rect_2.midtop = (WIDTH // 3 + text_game_height + return_height + return_height_1)
    
    return_height_2 = text_return_2.get_height()

    text_return_3 = assets[RETURN].render('se formar', True, WHITE)
    return_rect_3 = text_return_2.get_rect()
    return_rect_3.midtop = (WIDTH // 3 + text_game_height + return_height + return_height_1 + return_height_2)
    
    return_height_3 = text_return_3.get_height()

    text_return_4 = assets[RETURN].render('novamente?', True, WHITE)
    return_rect_4 = text_return_2.get_rect()
    return_rect_4.midtop = (WIDTH // 3 + text_game_height + return_height + return_height_1 + return_height_2 + return_height_3)
    '''

    '''#========== Cria o yes
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
'''
    running = True
    while running:
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                pygame.quit()

        # verifica em qual botão o jogador clicou
        status_mouse = pygame.mouse.get_pressed()
        posicao_mouse = pygame.mouse.get_pos()

        # cria condicional para caso seja apertado o YES
        '''if status_mouse == (True, False, False):
            if posicao_mouse[0] >= 125 and posicao_mouse[0] <= (125 + text_yes_width) and posicao_mouse[1] >= 550 and posicao_mouse[1] <= (550 + text_yes_height):
                state = GAME
                running = False

            if posicao_mouse[0] >= 375 and posicao_mouse[0] <= (375 + text_no_width) and posicao_mouse[1] >= 550 and posicao_mouse[1] <= (550 + text_no_height):
                pygame.quit()'''
                
        # ----- Gera saídas
        screen.blit(background, background_rect)
        screen.blit(text_game, game_rect)
        #screen.blit(text_over, over_rect)
        screen.blit(text_return, return_rect)
        screen.blit(text_return_1, return_rect_1)
        '''screen.blit(text_return_2, return_rect_2)
        screen.blit(text_return_3, return_rect_3)
        screen.blit(text_return_4, return_rect_4)
        screen.blit(text_yes, yes_rect)
        screen.blit(text_no, no_rect)'''

        pygame.display.flip()