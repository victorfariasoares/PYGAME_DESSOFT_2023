import pygame
import random
import time
from config import FPS, WIDTH, HEIGHT, YELLOW, OBSTACLES, OBSTACLES_INVERTS, WHITE, RED, QUIT, DONE, PLAYING
from assets import load_assets, FLY_SOUND, DIE_SOUND, BACKGROUND, SCORE_FONT
from sprites import Bird, Obstacle_1, Floor

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

    can_flap = True

    score = 0
    max_score = score

    state = PLAYING

    start_time = pygame.time.get_ticks()
    speed_increase_time = 10000

    lives = 0

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
            obst.rect.y = random.choice(OBSTACLES)
            obst_inverts.rect.y = random.choice(OBSTACLES_INVERTS)

        if obst_meiuca.rect.right < 0:
            obst_meiuca.rect.x = WIDTH
            obst_meiuca_inverts.rect.x = WIDTH
            obst_meiuca.rect.y = random.choice(OBSTACLES)
            obst_meiuca_inverts.rect.y = random.choice(OBSTACLES_INVERTS)

        if obst_final.rect.right < 0:
            obst_final.rect.x = WIDTH
            obst_final_inverts.rect.x = WIDTH
            obst_final.rect.y = random.choice(OBSTACLES)
            obst_final_inverts.rect.y = random.choice(OBSTACLES_INVERTS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                pygame.quit()
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, ele voa.
                    #keys_down[event.key] = True
                    if event.key == pygame.K_SPACE and can_flap:
                        player.rect.y -= 45
                        can_flap = False
                        assets[FLY_SOUND].play()

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
            hits = pygame.sprite.spritecollide(player, all_obstacles, False, pygame.sprite.collide_mask)
            if len(hits) > 0:
                assets[DIE_SOUND].play()
                player.speedy = 0
                player.kill()
                lives += 1
                time.sleep(0.3)

                if lives == 4:
                    state = DONE
                else:
                    player = Bird(groups, assets)
                    all_sprites.add(player)

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando jogador
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render('{:08d}'.format(score), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(f'você está na DP {lives}', True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state