import random
import pygame
from pygame.sprite import AbstractGroup
from config import WIDTH, HEIGHT
from assets import BIRD_IMG

class Bird(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BIRD_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedy = 0.25
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição do bird
        self.rect.y += 0.25

        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT