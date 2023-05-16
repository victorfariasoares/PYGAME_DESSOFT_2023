import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
BIRD_IMG = 'insper_img'
DIE_SOUND = 'die_sound'
FLY_SOUND = 'fly_sound'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpeg')).convert()
    assets[BIRD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'insper_logo.png')).convert_alpha()

    # Carrega os sons do jogo
    assets['fly_sound'] = pygame.mixer.Sound('assets/snd/fly_sound.wav')
    return assets
