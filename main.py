import pygame
from pygame.locals import *
import math
import random

"""--- RESET GAME ---"""
def reset_game():
    """
    Réinitialise toutes les variables du jeu pour le niveau actuel.
    """
    global x, y, player_life, score_player, bullets, numb_enemy, lvl_state, bowser_life


    x = 350
    y = 620
    player_life = 3
    score_player = 0


    bullets = []

    
    bowser_life = 5

    
    numb_enemy.clear()
    if lvl_state == "level1":
        for i in range(7):
            numb_enemy.append([
                random.randint(30, 1000),  
                random.randint(-5, 20),    
                random.choice([1, -1]),    
                random.choice([1, -1])     
            ])
    elif lvl_state == "level2":
        for i in range(10):
            numb_enemy.append([
                random.randint(30, 1000),
                random.randint(-5, 20),
                random.choice([1, -1]),
                random.choice([1, -1])
            ])
    elif lvl_state == "boss":
        
        numb_enemy.append([500, 80, 1, 1])

"""--- INITIALISATION ---"""
pygame.init()
pygame.mixer.init()

"""--- SET SCREEN ---"""
screen = pygame.display.set_mode((1248,832))
pygame.display.set_caption("Mario vs Bowser Jr")


running = True
clock = pygame.time.Clock()


"""--- IMAGE ---"""

fireball_image = pygame.transform.scale(pygame.image.load('img/fireball.png'), (20, 20))
player_image = pygame.transform.scale(pygame.image.load('img/mario.png'), (70, 70))
player_image_left = pygame.transform.scale(pygame.image.load('img/mario_left.png'), (70, 70))
enemy_image = pygame.transform.scale(pygame.image.load('img/bowserjr.png'), (70, 80))
bowser_image = pygame.transform.scale(pygame.image.load('img/bigbowser.png'), (180, 140))
explosion = pygame.transform.scale(pygame.image.load('img/explosion.png'), (80, 80))
boss_explosion = pygame.transform.scale(pygame.image.load('img/explosion.png'), (200, 200))
full_heart = pygame.transform.scale(pygame.image.load('img/fullheart.png'), (30, 30))
#background image
bg_image = pygame.image.load('img/backgame.png')
bg_menu = pygame.image.load("img/backmenu.png")
bg_pausemenu = pygame.image.load("img/pausemenu.png")
bg_lose = pygame.image.load("img/youlose.png")
bg_win = pygame.image.load("img/youwin.png")
bg_levels = pygame.image.load("img/levels.png")
bg_winboss = pygame.image.load("img/youwinboss.png")


"""--- BUTTON ---"""
start_rect = pygame.Rect(300, 200, 650, 200)
exit_rect = pygame.Rect(510,530,220,80)
levels_rect = pygame.Rect(440,430,360,90)
continue_rect= pygame.Rect(390,380,470,80)
retrymenu_rect=pygame.Rect(485,460,300,80)
retry_rect=pygame.Rect(470,300,305,100)
quitlosewin_rect=pygame.Rect(500,500,250,90)
menuwinlose_rect=pygame.Rect(490,405,270,90)
levelup_rect=pygame.Rect(420,300,430,100)
menupause_rect=pygame.Rect(510,541,250,80)
level1_rect=pygame.Rect(270,220,500,130)
level2_rect=pygame.Rect(270,350,508,125)
boss_rect=pygame.Rect(270,475,410,125)
startlevel_rect=pygame.Rect(680,510,185,60)
back_rect=pygame.Rect(1130,20,105,50)

"""--- LEVEL STATE ---"""
islevel1_selected=False
islevel2_selected=False
isboss_selected=False

"""--- GAME STATE"""
game_state = "menu"
lvl_state = "level1"

"""--- SOUND ---"""
fireball_sound = pygame.mixer.Sound('sound/fireballsoundeffect.wav')
browser_jr_screem = pygame.mixer.Sound('sound/BowserJrscreaming.wav')
win_sound = pygame.mixer.Sound('sound/winsound.wav')
browser_jr_screem.set_volume(0.2)

"""---PLAYER SETTINGS ---"""
x = 350
y = 620
player_life = 3
player_speed = 10
direction = True  # True = Right, False = Left
vel_y = 0
gravity = 1
is_jumping = False

"""--- ENEMY SETTINGS ---"""
numb_enemy = []
bowser_life = 5

"""--- BULLET SETTINGS ---"""
bullets = []
bullet_speed = -15



"""--- COLISION ---"""
def colision(x, enemy_x, y, enemy_y, dist):
    """
    Retourne True si distance entre le joueur / bullet et l'ennemi <= dist
    """
    distance = math.sqrt((math.pow(x - enemy_x,2)) + (math.pow(y - enemy_y,2)))
    return distance <= dist

"""--- DRAW FUNCTION ---"""
def draw_background():
    screen.blit(bg_image,(0,0))

def draw_player(x,y):
    screen.blit(player_image,(x,y))

def draw_player_left(x,y):
    screen.blit(player_image_left,(x,y))

def show_score(x,y):
    score = font.render("SCORE : " + str(score_player), True, (0,0,0))
    screen.blit(score, (x , y ))

def show_lvl(x,y):
    score = font.render(lvl_state.upper(), True, (0,0,0))
    screen.blit(score, (x , y ))

def show_life(x,y):
    for i in range(player_life):
        screen.blit(full_heart, (x , y ))
        x += 30

"""--- FONT ---"""
font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 40)

"""--- MAINLOOP ---"""
while running:
    clock.tick(60)
    screen.fill((0,0,0))
    
    """--- EVENT QUIT ---"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            quit()
        
       
        if game_state=="game" and event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and not is_jumping:
                is_jumping=True
                vel_y=-20
            if event.key==pygame.K_ESCAPE:
                game_state="pause"

        """--- MENU BUTTONS ---"""
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if game_state=="menu":
                if start_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state="game"
                if levels_rect.collidepoint(mouse_pos):
                    game_state="levels"
                if exit_rect.collidepoint(mouse_pos):
                    running=False
            #level
            if game_state=="levels":
                if level1_rect.collidepoint(mouse_pos):
                    islevel2_selected=False
                    isboss_selected=False
                    islevel1_selected=True
                    lvl_state="level1"
                if level2_rect.collidepoint(mouse_pos):
                    islevel1_selected=False
                    isboss_selected=False
                    islevel2_selected=True
                    lvl_state="level2"
                if boss_rect.collidepoint(mouse_pos):
                    islevel1_selected=False
                    islevel2_selected=False
                    isboss_selected=True
                    lvl_state="boss"
                if startlevel_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state="game"
                if back_rect.collidepoint(mouse_pos):
                    game_state="menu"
            #pause
            if game_state=="pause":
                if continue_rect.collidepoint(mouse_pos):
                    game_state="game"
                if retrymenu_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state="game"
                if menupause_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state="menu"
            #loose
            if game_state=="loose":
                if retry_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state="game"
                if menuwinlose_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state="menu"
                if quitlosewin_rect.collidepoint(mouse_pos):
                    running=False
            #win
            if game_state=="win":
                if levelup_rect.collidepoint(mouse_pos):
                    if lvl_state=="level1":
                        lvl_state="level2"
                        reset_game()
                        game_state="game"
                    elif lvl_state=="level2":
                        lvl_state="boss"
                        reset_game()
                        game_state="game"
                if menuwinlose_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state="menu"
                if quitlosewin_rect.collidepoint(mouse_pos):
                    running=False
            #win boss
            if game_state=="winboss":
                if menuwinlose_rect.collidepoint(mouse_pos):
                    lvl_state="level1"
                    reset_game()
                    game_state="menu"
                if quitlosewin_rect.collidepoint(mouse_pos):
                    running=False

    """--- DRAW SCREENS ---"""
    if game_state=="menu": screen.blit(bg_menu,(0,0))
    if game_state=="levels": 
        screen.blit(bg_levels,(0,0))
        if islevel1_selected == True:
            pygame.draw.rect(screen, (255, 0, 0), level1_rect, 4)  
        if islevel2_selected==True:
            pygame.draw.rect(screen, (255, 0, 0), level2_rect, 4) 
        if isboss_selected==True:
            pygame.draw.rect(screen, (255, 5, 5), boss_rect, 4)
    if game_state=="pause": screen.blit(bg_pausemenu,(0,0))
    if game_state=="loose": screen.blit(bg_lose,(0,0))
    if game_state=="win": screen.blit(bg_win,(0,0))
    if game_state=="winboss": screen.blit(bg_winboss,(0,0))

    """--- PLAYER MOVE ---"""
    if game_state=="game":
        draw_background()
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and x>0:     #left
            x-=player_speed
            direction=False
        if keys[K_RIGHT] and x<1200: #right
            x+=player_speed
            direction=True
        if keys[K_SPACE]:            #fireball
            if len(bullets) == 0: 
                fireball_sound.play()
                bullets.append([x+10, y])

        #jump
        if is_jumping:
            y+=vel_y
            vel_y+=gravity
        if y>=620:
            y=620
            vel_y=0
            is_jumping=False

        """--- UPDATE BULLET POSITIONS ---"""
        for bullet in bullets[:]:
            bullet[1]+=bullet_speed
            if bullet[1]<0:
                bullets.remove(bullet)
            else:
                screen.blit(fireball_image,(bullet[0],bullet[1]))

        """--- UPDATE ENEMIES ---"""
        for enemy in numb_enemy[:]:
            enemy[0]+=enemy[2]*7  
            enemy[1]+=enemy[3]*3  
        
            if lvl_state=="boss":
                if enemy[0]<=0 or enemy[0]>=1248-180:
                    enemy[2]*=-1
                if enemy[1]<=0 or enemy[1]>=620:
                    enemy[3]*=-1
                screen.blit(bowser_image,(enemy[0],enemy[1]))
                
                pygame.draw.rect(screen,(255,0,0),(enemy[0]+30,enemy[1]-20,180*(bowser_life/5),10))
            else:
                if enemy[0]<=0 or enemy[0]>=1178:
                    enemy[2]*=-1
                    enemy[3]=random.choice([-1,1])
                if enemy[1]<=0 or enemy[1]>=620:
                    enemy[3]*=-1
                screen.blit(enemy_image,(enemy[0],enemy[1]))

            """--- ENEMY → PLAYER---"""
            if lvl_state!="boss" and colision(x,enemy[0]+35,y,enemy[1]+40,40):
                player_life-=1
                if player_life<=0: game_state="loose"
                if enemy in numb_enemy: numb_enemy.remove(enemy)
            elif lvl_state=="boss" and colision(x,enemy[0]+90,y,enemy[1]+70,80):
                player_life=0
                game_state="loose"

        """--- COLISION FIREBALL → ENEMY ---"""
        for bullet in bullets[:]:
            for enemy in numb_enemy[:]:
                if lvl_state!="boss":
                    if colision(bullet[0],enemy[0]+35,bullet[1],enemy[1]+40,40):
                        score_player+=1
                        if bullet in bullets: bullets.remove(bullet)
                        if enemy in numb_enemy: numb_enemy.remove(enemy)
                        browser_jr_screem.play()
                else:
                    if bowser_life>0 and colision(bullet[0],enemy[0]+90,bullet[1],enemy[1]+70,80):
                        bowser_life-=1
                        if bullet in bullets: bullets.remove(bullet)
                        browser_jr_screem.play()
                    if bowser_life<=0:
                        if enemy in numb_enemy: numb_enemy.remove(enemy)


        """--- DRAW EVERYTHING---"""
        if direction: draw_player(x,y)
        else: draw_player_left(x,y)
        show_score(10,20)
        show_life(10,80)
        show_lvl(1100,10)

        #win ?
        if lvl_state!="boss" and len(numb_enemy)==0: game_state="win"
        if lvl_state=="boss" and bowser_life<=0: game_state="winboss"

    pygame.display.update()
