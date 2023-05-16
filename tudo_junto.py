# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
WIDTH = 500
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy')

# ------- posição do chão
floor_x_pos = 0
floor_y_pos = 638

# ----- Inicia assets
FPS = 120
FLAPPY_WIDTH = 111 / 2
FLAPPY_HEIGHT = 134 / 2

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('assets/img/background.jpeg').convert()
    assets['floor'] = pygame.image.load('assets/img/floor.png').convert()
    assets['floor'] = pygame.transform.scale2x(assets['floor'])
    assets['bird_img'] = pygame.image.load('assets/img/bird.png').convert_alpha()
    assets['bird_img'] = pygame.transform.scale(assets['bird_img'], (FLAPPY_WIDTH, FLAPPY_HEIGHT))

    # Carrega os sons do jogo
    assets['fly_sound'] = pygame.mixer.Sound('assets/snd/fly_sound.wav')

    return assets

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Bird(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bird_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 40
        self.rect.bottom = HEIGHT / 2
        self.speedy = 3
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição do bird
        self.rect.y += 2 * self.speedy

        # Mantem dentro da tela
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= floor_y_pos:
            self.rect.bottom = floor_y_pos

class Floor(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['floor']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = floor_x_pos
        self.rect.y = floor_y_pos
        self.speedx = -1
        self.groups = groups
        self.assets = assets

    def update(self):
        # Faz movimento do chão
        self.rect.x += self.speedx

        # fica em um loop para manter o moviento
        if self.rect.right <= WIDTH:
            self.rect.right = WIDTH + 172

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de sprites
    all_sprites = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites

    # Criando o jogador e o chão
    player = Bird(groups, assets)
    all_sprites.add(player)

    floor = Floor(groups, assets)
    all_sprites.add(floor)

    DONE = 0
    PLAYING = 1
    state = PLAYING

    keys_down = {}

    # ===== Loop principal =====
    #pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, ele voa.
                    #keys_down[event.key] = True
                    if event.key == pygame.K_SPACE:
                        player.rect.y = 0
                        player.rect.y -= 12
                        pygame.mixer.Sound('assets/snd/fly_sound.wav').play()


        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background'], (0, 0))
        # Desenhando jogador
        all_sprites.draw(window)

        pygame.display.update()  # Mostra o novo frame para o jogador

game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados