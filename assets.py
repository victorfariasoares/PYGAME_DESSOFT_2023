import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR, FLAPPY_WIDTH, FLAPPY_HEIGHT


BACKGROUND = 'background'
INICIAL_SCREEN = 'inicial screen'
BIRD_IMG = 'bird_img'
DIE_SOUND = 'die_sound'
FLOOR = 'floor'
FLY_SOUND = 'fly_sound'
OBSTACLE = 'obstaculo'
OBSTACLE_INVERT = 'obstaculo_invert'
SCORE_FONT = 'score_font'
GAME_OVER_FONT = 'game_over_font'
YES_FONT = 'yes_font'
RETURN = 'return'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpeg')).convert()
    assets[INICIAL_SCREEN] = pygame.image.load(os.path.join(IMG_DIR, 'foto_inicial.png')).convert()
    assets[FLOOR] = pygame.image.load(os.path.join(IMG_DIR, 'floor.png')).convert()
    assets[FLOOR] = pygame.transform.scale2x(assets['floor'])
    assets[BIRD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bird.png')).convert_alpha()
    assets[BIRD_IMG] = pygame.transform.scale(assets['bird_img'], (FLAPPY_WIDTH, FLAPPY_HEIGHT))
    assets[OBSTACLE] = pygame.image.load(os.path.join(IMG_DIR, 'obst.png')).convert_alpha()
    assets[OBSTACLE_INVERT] = pygame.image.load(os.path.join(IMG_DIR, 'obst_invert.png')).convert_alpha()
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'prstartk.ttf'), 28)
    assets[GAME_OVER_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'prstartk.ttf'), 56)
    assets[YES_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'prstartk.ttf'), 35)
    assets[RETURN] = pygame.font.Font(os.path.join(FNT_DIR, 'prstartk.ttf'), 25)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'game_sound.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[FLY_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'fly_sound.wav'))
    assets[DIE_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'die_sound.wav'))

    return assets
