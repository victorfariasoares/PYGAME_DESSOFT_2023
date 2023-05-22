from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 500 # Largura da tela
HEIGHT = 750 # Altura da tela
FPS = 120 # Frames por segundo

# Define tamanhos
FLAPPY_WIDTH = 111 / 2
FLAPPY_HEIGHT = 134 / 2

# -------- alturas dos obstaculos
OBSTACLES = [0, -27, -77, -177]
OBSTACLES_INVERTS = [411, 438, 488, 588]

# ------- posição do chão
floor_x_pos = 0
floor_y_pos = 638
obstacle_space = 184
height_space = 227

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
DONE = 3
PLAYING = 4
CONCLUDE = 5