# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time

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
obstacles_inverts = [411, 438, 488, 588]
obstacles_x = [250, 325, 450]

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
    assets['score_font'] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/snd/game_sound.wav')
    pygame.mixer.music.set_volume(0.4)
    assets['fly_sound'] = pygame.mixer.Sound('assets/snd/fly_sound.wav')
    assets['die_sound'] = pygame.mixer.Sound('assets/snd/die_sound.wav')

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
            self.rect.y = random.choice(obstacles)

        else:
            self.image = pygame.transform.rotate(assets['obstaculo'], 180)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.y = random.choice(obstacles_inverts)
        
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

    # Criando os obstáculos
    obst = Obstacle_1(groups, assets, 'cima', 500)
    all_sprites.add(obst)
    all_obstacles.add(obst)

    obst_inverts = Obstacle_1(groups, assets, 'baixo', 500)
    all_sprites.add(obst_inverts)
    all_obstacles.add(obst_inverts)

    obst_meiuca = Obstacle_1(groups, assets, 'cima', 630)
    all_sprites.add(obst_meiuca)
    all_obstacles.add(obst_meiuca)

    obst_meiuca_inverts = Obstacle_1(groups, assets, 'baixo', 630)
    all_sprites.add(obst_meiuca_inverts)
    all_obstacles.add(obst_meiuca_inverts)

    obst_final = Obstacle_1(groups, assets, 'cima', 750)
    all_sprites.add(obst_final)
    all_obstacles.add(obst_final)

    obst_final_inverts = Obstacle_1(groups, assets, 'baixo', 750)
    all_sprites.add(obst_final_inverts)
    all_obstacles.add(obst_final_inverts)

    # Criando o piso
    floor = Floor(assets, 0)
    all_sprites.add(floor)

    DONE = 0
    PLAYING = 1
    state = PLAYING

    can_flap = True

    score = 0
    max_score = score

    start_time = pygame.time.get_ticks()
    speed_increase_time = 10000

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= speed_increase_time:
            # Aumente a velocidade aqui
            start_time = current_time
            obst.speedx -= 1
            obst_inverts.speedx -= 1
            obst_meiuca.speedx -= 1
            obst_meiuca_inverts.speedx -= 1
            obst_final.speedx -= 1
            obst_final_inverts.speedx -= 1
            floor.speedx -= 1

        # reposiciona os obstaculos
        if obst.rect.right < 0:
            obst.rect.x = WIDTH
            obst_inverts.rect.x = WIDTH
            obst.rect.y = random.choice(obstacles)
            obst_inverts.rect.y = random.choice(obstacles_inverts)

        if obst_meiuca.rect.right < 0:
            obst_meiuca.rect.x = WIDTH
            obst_meiuca_inverts.rect.x = WIDTH
            obst_meiuca.rect.y = random.choice(obstacles)
            obst_meiuca_inverts.rect.y = random.choice(obstacles_inverts)

        if obst_final.rect.right < 0:
            obst_final.rect.x = WIDTH
            obst_final_inverts.rect.x = WIDTH
            obst_final.rect.y = random.choice(obstacles)
            obst_final_inverts.rect.y = random.choice(obstacles_inverts)

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
                        player.rect.y -= 45
                        can_flap = False
                        pygame.mixer.Sound('assets/snd/fly_sound.wav').play()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        can_flap = True

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos sprites
        all_sprites.update()

        if obst.rect.x or obst_meiuca.rect.x or obst_final.rect.x == player.rect.x:
            score += 1

        if score > max_score:
            max_score = score

        if state == PLAYING:
            # Verifica se houve colisão entre flappy e obstáculo
            hits = pygame.sprite.spritecollide(player, all_obstacles, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                assets['die_sound'].play()
                player.speedy = 0
                player.kill()
                time.sleep(0.5)
                state = DONE

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background'], (0, 0))
        # Desenhando jogador
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados