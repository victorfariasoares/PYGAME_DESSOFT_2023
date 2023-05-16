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

    for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets[EXPLOSION_ANIM] = explosion_anim
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[DESTROY_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[PEW_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets
