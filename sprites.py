import random
import pygame
from config import WIDTH, HEIGHT, floor_y_pos, floor_x_pos, OBSTACLES, OBSTACLES_INVERTS


class Bird(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bird_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 40
        self.rect.bottom = HEIGHT / 2
        self.speedy = 2
        self.groups = groups
        self.assets = assets

    def update(self):
         # Atualização da posição do bird
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= floor_y_pos:
            self.rect.bottom = floor_y_pos

class Floor(pygame.sprite.Sprite):
    def __init__(self, assets, x):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['floor']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = floor_x_pos
        self.rect.y = floor_y_pos
        self.rect.x = x
        self.speedx = -1

    def update(self):
        # Faz movimento do chão
        self.rect.x += self.speedx

        if self.rect.right <= WIDTH + 1:
            self.rect.x = 0

class Obstacle_1(pygame.sprite.Sprite):
    def __init__(self, groups, assets, orientacao, x):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        if orientacao == 'cima':
            self.image = assets['obstaculo']
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.y = random.choice(OBSTACLES)

        else:
            self.image = pygame.transform.rotate(assets['obstaculo'], 180)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.y = random.choice(OBSTACLES_INVERTS)
        
        self.rect.x = x

        self.speedx = -1

        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualizando a posição do obstáculo
        self.rect.x += self.speedx

class DESOFT(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)