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
obstacle_space = 184
height_space = 227

# -------- alturas dos obstaculos
obstacles = [0, -27, -77, -177]

# ----- Inicia assets
FPS = 120
FLAPPY_WIDTH = 111 / 2
FLAPPY_HEIGHT = 134 / 2
GREEN = (0, 255, 0)

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('assets/img/background.jpeg').convert()
    assets['floor'] = pygame.image.load('assets/img/floor.png').convert()
    assets['floor'] = pygame.transform.scale2x(assets['floor'])
    assets['bird_img'] = pygame.image.load('assets/img/bird.png').convert_alpha()
    assets['bird_img'] = pygame.transform.scale(assets['bird_img'], (FLAPPY_WIDTH, FLAPPY_HEIGHT))
    assets['obstaculo'] = pygame.image.load('assets/img/obst.png').convert_alpha()
    assets['obstaculo_invert'] = pygame.image.load('assets/img/obst_invert.png').convert_alpha()

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
        self.speedy = 1
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

class Obstacle_1(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['obstaculo']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = -177
        self.rect.x = 450

        z = height_space - self.rect.y

        self.speedx = -1

        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualizando a posição do obstáculo
        self.rect.x += self.speedx

        # Quando o obstáculo passar do começo da tela, cria um novo
        if self.rect.right <= 0:
            self.rect.x = 450
            self.rect.y = random.choice(obstacles)

class Obstacle_1_invert(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.imagem_invertida = assets['obstaculo_invert']
        self.mask = pygame.mask.from_surface(self.imagem_invertida)
        self.rect_invertida = self.imagem_invertida.get_rect()
        self.rect_invertida.y = 0
        self.rect_invertida.x = 450
        z = height_space - self.rect_invertida.y

        self.image = assets['obstaculo']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = floor_y_pos - z + obstacle_space
        self.rect.x = 450

        self.speedx = -1

        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualizando a posição do obstáculo
        self.rect_invertida.x += self.speedx
        self.rect.x += self.speedx

        # Quando o obstáculo passar do começo da tela, cria um novo
        if self.rect.right <= 0:
            self.rect.x = 450

#class Obstacle_2(pygame.sprite.Sprite):


#class Obstacle_3(pygame.sprite.Sprite):



def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_obstacles = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_obstacles'] = all_obstacles

    # Criando o jogador e o chão
    player = Bird(groups, assets)
    all_sprites.add(player)

    # Criando o piso
    floor = Floor(groups, assets)
    all_sprites.add(floor)

    # Criando os obstáculos
    obst = Obstacle_1(groups, assets)
    all_sprites.add(obst)
    all_obstacles.add(obst)

    DONE = 0
    PLAYING = 1
    state = PLAYING

    can_flap = True

    keys_down = {}

    generate_places = True
    y_positions = []

    # ===== Loop principal =====
    #pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        if generate_places:
            for i in range(len(obstacles)):
                y_positions.append(random.randint(0, 500))
            generate_places = False

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
                    if event.key == pygame.K_SPACE and can_flap:
                        player.rect.y -= 35
                        can_flap = False
                        pygame.mixer.Sound('assets/snd/fly_sound.wav').play()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        can_flap = True

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