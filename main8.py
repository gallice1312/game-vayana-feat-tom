# Debugged Mario vs Bowser game (fixed fireball-enemy collisions and enemy/boss vertical behavior)
import pygame
from pygame.locals import *
import math
import random

def reset_game():
    global x, y, player_life, score_player, bullets, numb_enemy, lvl_state, bowser_life

    # position du joueur
    x = 350
    y = 620

    # stats du joueur
    player_life = 3
    score_player = 0

    # projectiles
    bullets = []

    # réinitialisation du boss
    bowser_life = 5

    # réinitialisation des ennemis selon le niveau
    numb_enemy.clear()

    if lvl_state == "level1":
        for i in range(1, 15):
            numb_enemy.append([random.randint(30, 1000), random.randint(-5, 20), random.choice([1, -1])])
    elif lvl_state == "level2":
        for i in range(1, 20):
            numb_enemy.append([random.randint(30, 1000), random.randint(-5, 20), random.choice([1, -1])])
    elif lvl_state == "boss":
        # un seul boss à chaque reset
        numb_enemy.append([500, 80, 1])


# pygame setup
pygame.init()
pygame.mixer.init()
running = True

# --- IMAGE ---
fireball_image = pygame.transform.scale((pygame.image.load('img/fireball.png')), (20, 20))
player_image = pygame.transform.scale((pygame.image.load('img/mario.png')), (70, 70))
player_image_left = pygame.transform.scale((pygame.image.load('img/mario_left.png')), (70, 70))
enemy_image = pygame.transform.scale((pygame.image.load('img/bowserjr.png')), (70, 80))
bowser_image = pygame.transform.scale((pygame.image.load('img/bigbowser.png')), (180, 140))
explosion = pygame.transform.scale((pygame.image.load('img/explosion.png')), (80, 80))
boss_explosion = pygame.transform.scale((pygame.image.load('img/explosion.png')), (200, 200))
full_heart = pygame.transform.scale((pygame.image.load('img/fullheart.png')), (30, 30))

# backgrounds
bg_image = pygame.image.load('img/backgame.png')
bg_menu = pygame.image.load("img/backmenu.png")
bg_pausemenu = pygame.image.load("img/pausemenu.png")
bg_lose = pygame.image.load("img/youlose.png")
bg_win = pygame.image.load("img/youwin.png")
bg_levels = pygame.image.load("img/levels.png")
bg_winboss = pygame.image.load("img/youwinboss.png")

# screen
screen = pygame.display.set_mode((1248, 832))

# buttons (kept unchanged)
start_rect = pygame.Rect(300, 200, 650, 200)
exit_rect = pygame.Rect(510, 530, 220, 80)
levels_rect = pygame.Rect(440, 430, 360, 90)
continue_rect = pygame.Rect(390, 380, 470, 80)
retrymenu_rect = pygame.Rect(485, 460, 300, 80)
retry_rect = pygame.Rect(470, 300, 305, 100)
quitlosewin_rect = pygame.Rect(500, 500, 250, 90)
menuwinlose_rect = pygame.Rect(490, 405, 270, 90)
levelup_rect = pygame.Rect(420, 300, 430, 100)
menupause_rect = pygame.Rect(510, 541, 250, 80)
level1_rect = pygame.Rect(270, 220, 500, 130)
level2_rect = pygame.Rect(270, 350, 508, 125)
boss_rect = pygame.Rect(270, 475, 410, 125)
startlevel_rect = pygame.Rect(680, 510, 185, 60)
back_rect = pygame.Rect(1130, 20, 105, 50)

# sounds
fireball_sound = pygame.mixer.Sound('sound/fireballsoundeffect.wav')
browser_jr_screem = pygame.mixer.Sound('sound/BowserJrscreaming.wav')
win_sound = pygame.mixer.Sound('sound/winsound.wav')

browser_jr_screem.set_volume(0.2)

# ensure single clock usage
clock = pygame.time.Clock()

# initial flags
islevel1_selected = False
islevel2_selected = False
isboss_selected = False

# player settings
direction = True
player_speed = 10
x = 350
y = 620
player_life = 3
vel_y = 0
gravity = 1
is_jumping = False

# enemy settings
numb_enemy = []
for i in range(1, 15):
    numb_enemy.append([random.randint(30, 350), random.randint(-5, 20), random.choice([1, -1])])

# big bowser
bowser = [[x, 80, 1]]
bowser_life = 5

# collision
def colision(x, enemy_x, y, enemy_y):
    distance = math.sqrt((math.pow(x - enemy_x, 2)) + (math.pow(y - enemy_y, 2)))
    return distance <= 40

# font
font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 40)

# score
score_player = 0

def show_score(xp, yp):
    score = font.render("SCORE : " + str(score_player), True, (0, 0, 0))
    screen.blit(score, (xp, yp))

def show_lvl(xp, yp):
    score = font.render(lvl_state.upper(), True, (0, 0, 0))
    screen.blit(score, (xp, yp))

def show_life(xp, yp):
    xx = xp
    for i in range(player_life):
        screen.blit(full_heart, (xx, yp))
        xx += 30

# draw
def draw_background():
    screen.blit(bg_image, (0, 0))

def draw_player(px, py):
    screen.blit(player_image, (px, py))

def draw_player_left(px, py):
    screen.blit(player_image_left, (px, py))

# bullets
bullet_speed = -15
bullets = []

# initial states
game_state = "menu"
lvl_state = "level1"

# Main loop
while running:
    current_time = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        # Menu and state handling (kept same)
        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_rect.collidepoint(mouse_pos):
                    game_state = "game"
                if levels_rect.collidepoint(mouse_pos):
                    game_state = "levels"
                if exit_rect.collidepoint(mouse_pos):
                    running = False
        if game_state == "levels":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if level1_rect.collidepoint(mouse_pos):
                    islevel2_selected = False
                    isboss_selected = False
                    islevel1_selected = True
                    lvl_state = "level1"
                if level2_rect.collidepoint(mouse_pos):
                    islevel1_selected = False
                    isboss_selected = False
                    islevel2_selected = True
                    lvl_state = "level2"
                if boss_rect.collidepoint(mouse_pos):
                    islevel1_selected = False
                    islevel2_selected = False
                    isboss_selected = True
                    lvl_state = "boss"
                if startlevel_rect.collidepoint(mouse_pos):
                    game_state = "game"
                if back_rect.collidepoint(mouse_pos):
                    game_state = "menu"
        if game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not is_jumping:
                        is_jumping = True
                        vel_y = -20
                if event.key == pygame.K_ESCAPE:
                    game_state = "pause"
        if game_state == "pause":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if continue_rect.collidepoint(mouse_pos):
                    game_state = "game"
                if retrymenu_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "game"
                if menupause_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "menu"
        if game_state == "loose":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if retry_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "game"
                if menuwinlose_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "menu"
                elif quitlosewin_rect.collidepoint(mouse_pos):
                    running = False
        if game_state == "win":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if levelup_rect.collidepoint(mouse_pos):
                    if lvl_state == "level1":
                        lvl_state = "level2"
                        reset_game()
                        game_state = "game"
                    elif lvl_state == "level2":
                        lvl_state = "boss"
                        reset_game()
                        game_state = "game"
                if menuwinlose_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "menu"
                elif quitlosewin_rect.collidepoint(mouse_pos):
                    running = False
        if game_state == "winboss":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if menuwinlose_rect.collidepoint(mouse_pos):
                    lvl_state = "level1"
                    reset_game()
                    game_state = "menu"
                elif quitlosewin_rect.collidepoint(mouse_pos):
                    running = False

    # --- RENDER STATES ---
    if game_state == "menu":
        screen.blit(bg_menu, (0, 0))
    if game_state == "win":
        screen.blit(bg_win, (0, 0))
    if game_state == "loose":
        screen.blit(bg_lose, (0, 0))
    if game_state == "pause":
        screen.blit(bg_pausemenu, (0, 0))
    if game_state == "levels":
        screen.blit(bg_levels, (0, 0))
        if islevel1_selected:
            pygame.draw.rect(screen, (255, 0, 0), level1_rect, 4)
        if islevel2_selected:
            pygame.draw.rect(screen, (255, 0, 0), level2_rect, 4)
        if isboss_selected:
            pygame.draw.rect(screen, (255, 5, 5), boss_rect, 4)
    if game_state == "winboss":
        screen.blit(bg_winboss, (0, 0))

    if game_state == "game":
        screen.blit(bg_image, (0, 0))

        # level parameters
        if lvl_state == 'level1':
            enemy_speed = 7
            numb_enemy = numb_enemy[:7]
            move = 50
            coll = 50
        if lvl_state == 'level2':
            enemy_speed = 10
            numb_enemy = numb_enemy[:10]
            move = 50
            coll = 50
        if lvl_state == 'boss':
            enemy_speed = 15
            numb_enemy = bowser
            move = 80
            player_life = 1
            coll = 110

        # player movement
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and x > 0:
            x -= player_speed
            direction = False
        if keys[K_RIGHT] and x < 1200:
            x += player_speed
            direction = True
        if keys[K_SPACE]:
            if len(bullets) < 1:
                fireball_sound.play()
                bullet_x = x + 10
                bullet_y = y
                bullets.append([bullet_x, bullet_y])
        if is_jumping:
            y += vel_y
            vel_y += gravity
        if y >= 620:
            y = 620
            vel_y = 0
            is_jumping = False

        # update bullets
        for bullet in bullets[:]:
            bullet[1] += bullet_speed
            if bullet[1] < 0:
                try:
                    bullets.remove(bullet)
                except ValueError:
                    pass

        # update enemies (movement)
        max_x = 1200 - 70
        for enemy in numb_enemy:
            enemy[0] += enemy[2] * enemy_speed

            # reverse at horizontal borders
            if enemy[0] <= 0:
                enemy[0] = 0
                enemy[2] *= -1
                enemy[1] += move
            elif enemy[0] >= max_x:
                enemy[0] = max_x
                enemy[2] *= -1
                enemy[1] += move

            # clamp vertical position and if exceeded, pull back up so enemies/boss don't get stuck at the very bottom
            enemy_height = 140 if lvl_state == 'boss' else 80
            max_y = 832 - enemy_height
            if enemy[1] < 0:
                enemy[1] = 0
            if enemy[1] > max_y:
                # instead of leaving them below the visible play area, set them to just below the max
                enemy[1] = max(0, max_y - move)

        # DRAW
        draw_background()
        if direction is False:
            draw_player_left(x, y)
        else:
            draw_player(x, y)
        show_score(10, 20)
        show_life(10, 80)
        show_lvl(1100, 10)

        # FIREBALL → ENEMY collision (safer removal)
        enemies_to_remove = set()
        bullets_to_remove = set()

        for bi, bullet in enumerate(bullets[:]):
            # update bullet already done above, now check collisions
            for ei, enemy in enumerate(numb_enemy[:]):
                # protective check in case lists changed
                if bullet not in bullets or enemy not in numb_enemy:
                    continue

                if colision(bullet[0], enemy[0] + coll, bullet[1], enemy[1] + coll):
                    # collision!
                    if lvl_state != 'boss':
                        enemies_to_remove.add(ei)
                        bullets_to_remove.add(bi)
                        score_player += 1
                        browser_jr_screem.play()
                    else:
                        # boss hit
                        bullets_to_remove.add(bi)
                        browser_jr_screem.play()
                        bowser_life -= 1
                        score_player += 1
                        # if boss dead, mark for removal
                        if bowser_life <= 0:
                            enemies_to_remove.add(ei)
                    # stop checking other enemies for this bullet
                    break

        # perform removals (use reversed indices to remove safely)
        for bi in sorted(bullets_to_remove, reverse=True):
            if bi < len(bullets):
                try:
                    del bullets[bi]
                except Exception:
                    pass
        for ei in sorted(enemies_to_remove, reverse=True):
            if ei < len(numb_enemy):
                try:
                    del numb_enemy[ei]
                except Exception:
                    pass

        # If all enemies cleared -> win
        if len(numb_enemy) == 0:
            if lvl_state in ("level1", "level2"):
                game_state = 'win'
            elif lvl_state == 'boss':
                game_state = 'winboss'

        # draw bullets (after collision handling so removed bullets don't get blitted)
        for bullet in bullets:
            screen.blit(fireball_image, (bullet[0], bullet[1]))

        # draw enemies and handle enemy→player collisions
        for enemy in numb_enemy[:]:
            if lvl_state != 'boss':
                screen.blit(enemy_image, (enemy[0], enemy[1]))
            else:
                screen.blit(bowser_image, (enemy[0], enemy[1]))

            if player_life > 0:
                if colision(x, enemy[0] + 70, y, enemy[1] + 70):
                    if lvl_state != 'boss':
                        try:
                            numb_enemy.remove(enemy)
                        except ValueError:
                            pass
                        player_life -= 1
                    else:
                        player_life -= 1

            if player_life <= 0:
                game_state = 'loose'

    pygame.display.update()

pygame.quit()
