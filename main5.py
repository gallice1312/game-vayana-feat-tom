#import module pygame
import pygame
from pygame.locals import *
import math
import random

def reset_game():
    global x, y, player_life, score_player, bullets, numb_enemy, lvl_state

    # update player positioin
    x = 350
    y = 620

    # update score and life
    player_life = 3
    score_player = 0

    # delet all bullet
    bullets = []

    # draw all enmys
    numb_enemy.clear()
    for i in range(1, 30):
        numb_enemy.append([random.randint(30, 350), random.randint(30, 350), random.choice([1, -1])])




#pygame setup 
pygame.init()
pygame.mixer.init()
running = True




"""--- IMAGE ---"""
#fireball image
fireball_image =  pygame.transform.scale((pygame.image.load('img/fireball.png')),(20,20))
#set player right
player_image =  pygame.transform.scale((pygame.image.load('img/mario.png')),(70,70))
#set player left
player_image_left =  pygame.transform.scale((pygame.image.load('img/mario_left.png')),(70,70))
#enemy image
enemy_image = pygame.transform.scale((pygame.image.load('img/bowserjr.png')),(70,80))
#browser image
bowser_image = pygame.transform.scale((pygame.image.load('img/bigbowser.png')),(140,140))
#explosion image 
explosion = pygame.transform.scale((pygame.image.load('img/explosion.png')),(80,80))
#full heart
full_heart = pygame.transform.scale((pygame.image.load('img/fullheart.png')),(30,30))
#empty heart



#background image
bg_image = pygame.image.load('img/backgame.png')
bg_menu = pygame.image.load("img/backmenu.png")
bg_pausemenu = pygame.image.load("img/pausemenu.png")
bg_lose=pygame.image.load("img/youlose.png")
bg_win=pygame.image.load("img/youwin.png")
bg_levels=pygame.image.load("img/levels.png")
bg_winboss=pygame.image.load("img/youwinboss.png")

"""--- SET BUTTON ---"""
screen = pygame.display.set_mode((1248,832))
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

"""--- SOUND EFFECT ---"""
fireball_sound = pygame.mixer.Sound('sound/fireballsoundeffect.wav')
browser_jr_screem = pygame.mixer.Sound('sound/BowserJrscreaming.wav')
win_sound = pygame.mixer.Sound('sound/winsound.wav')
	
browser_jr_screem.set_volume(0.1)

"""--- SET SCREEN ---"""
#set screen
screen = pygame.display.set_mode((1248,832))
clock = pygame.time.Clock()

islevel1_selected=False
islevel2_selected=False
isboss_selected=False

"""--- PLAYER SETTINGS ---"""
#player direction
direction = True
# velocity of player's movement
player_speed = 10
x =350
y=620
player_life = 3

"""--- ENEMY SETTINGS ---"""
numb_enemy = []
for i in range(1,15):   
    numb_enemy.append([random.randint(30,350),random.randint(30,350),random.choice([1,-1])])


"""--- BIG BOWSER ---"""
bowser = [x,80,1]
bowser_life = 50


"""--- COLISION --"""
def colision(x,enemy_x,y,enemy_y):
    distance = math.sqrt((math.pow(x - enemy_x, 2)) + (math.pow(y - enemy_y, 2)))
    if distance <= 40:
        return True
    else:
        return False
    
"""--- FONT ---"""
font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 40)

"""--- SHOW SCORE ---"""
#Score
score_player = 0
def show_score(x,y):
    score = font.render("SCORE : " + str(score_player), True, (0,0,0))
    screen.blit(score, (x , y ))


def show_life(x,y):
    for i in range (player_life) :
        screen.blit(full_heart, (x , y ))
        x += 30

"""--- DRAW ---"""
def draw_background():
    screen.blit(bg_image,(0,0))
def draw_player(x,y):
    screen.blit(player_image,(x,y))
def draw_player_left(x,y):
    screen.blit(player_image_left,(x,y))


"""--- BULLET SETTINGS ---"""
bullet_speed = -15  # vers le haut
bullets = [] 


# initiate with menu
game_state = "menu" 

lvl_state = "level1"
"""--- MAIN LOOP ---"""
while running:
    
    clock.tick(60)
    
    
    """--- EVENT ---"""
    
    for event in pygame.event.get():
        #exit with x on the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        """--- MENU ---"""
        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_rect.collidepoint(mouse_pos):
                    game_state = "game"
                if levels_rect.collidepoint(mouse_pos):
                    game_state= "levels"
                if exit_rect.collidepoint(mouse_pos):
                    running = False
        if game_state == "levels":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if level1_rect.collidepoint(mouse_pos):
                    islevel2_selected=False
                    isboss_selected=False
                    islevel1_selected=True
                    lvl_state= "level1"
                if level2_rect.collidepoint(mouse_pos):
                    islevel1_selected=False
                    isboss_selected=False
                    islevel2_selected=True
                    lvl_state= "level2"
                if boss_rect.collidepoint(mouse_pos):
                    islevel1_selected=False
                    islevel2_selected=False
                    isboss_selected=True
                    lvl_state="boss"
                if startlevel_rect.collidepoint(mouse_pos):
                    game_state="game"
                if back_rect.collidepoint(mouse_pos):
                    game_state="menu"
        if game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # revenir au menu
                    game_state = "pause"
        if game_state == "pause":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if continue_rect.collidepoint(mouse_pos):
                    game_state = "game"
                if retrymenu_rect.collidepoint(mouse_pos):
                   reset_game()
                   game_state="game"
                if menupause_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "menu"
        if game_state=="loose":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if retry_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "game"
                if menuwinlose_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_state="menu"
                elif quitlosewin_rect.collidepoint(mouse_pos):
                    running = False
        if game_state=="win":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if levelup_rect.collidepoint(mouse_pos):
                    if lvl_state =="level1":
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
                elif quitlosewin_rect.collidepoint(mouse_pos):
                    running = False
        if game_state=="winboss":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if menuwinlose_rect.collidepoint(mouse_pos):
                    lvl_state="level1"
                    reset_game()
                    game_state="menu"
                elif quitlosewin_rect.collidepoint(mouse_pos):
                    running = False
    
    if game_state == "menu":
        screen.blit(bg_menu, (0, 0))
    if game_state =="win" :
        screen.blit(bg_win,(0,0))
        #win_sound.play()
    if game_state =="loose" :
        screen.blit(bg_lose,(0,0))
    if game_state=="pause":
        screen.blit(bg_pausemenu,(0,0)) 
    if game_state=="levels":
        screen.blit(bg_levels,(0,0))
        if islevel1_selected == True:
           pygame.draw.rect(screen, (255, 0, 0), level1_rect, 4)  # START (bordure rouge)
        if islevel2_selected==True:
            pygame.draw.rect(screen, (255, 0, 0), level2_rect, 4)  # START (bordure rouge)
        if isboss_selected==True:
            pygame.draw.rect(screen, (255, 5, 5), boss_rect, 4)  # START (bordure rouge)
    if game_state=="winboss":
        #win_sound.play()
        screen.blit(bg_winboss,(0,0))
         


    if game_state == "game":
        screen.blit(bg_image, (0, 0)) 
        if lvl_state == 'level1':
            enemy_speed = 7
            numb_enemy = numb_enemy[:7]
        if lvl_state == 'level2':
            enemy_speed = 10
            numb_enemy = numb_enemy[:10]
        if lvl_state == 'boss':
            enemy_speed = 20
            numb_enemy = numb_enemy

            


        """--- MOVEMENT KEYS """
        #get key pressed and move character
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and x > 0:
            x -= player_speed
            direction = False          #left            
        if keys[K_RIGHT] and x < 1200:
            x += player_speed
            direction = True            #right
        if keys[K_SPACE]:
        # create new fireball
            #not more than 1 fireball displayed on the screen
            if len(bullets) < 1:
                fireball_sound.play()
                bullet_x = x + 10  # on the player
                bullet_y = y 
                bullets.append([bullet_x, bullet_y])

        """--- UPDATE BULLET POSITIONS ---"""
        for bullet in bullets[:]:
            bullet[1] += bullet_speed
            # Delet fireball out of the screen 
            if bullet[1] < 0:
                bullets.remove(bullet)

        """--- UPDATE ENEMIES ---"""
        for enemy in numb_enemy:
            enemy[0] += enemy[2] * enemy_speed  # side move
            # Rebondir sur les bords
            if enemy[0] <= 0 or enemy[0] >= 1200 and enemy[1] <810:
                enemy[2] *= -1  # reset enemy direction
                enemy[1] += 40  # go down a lil at every corner
        
            
            
            
        """--- DRAW EVERYTHING---"""
        #draw background
        draw_background()
        if direction == False :
            draw_player_left(x,y)
        if direction == True :
            draw_player(x,y)
        #draw score
        show_score(10,10)
        #draww score
        show_life(10,60)
        
        
        #draw fire ball
        for bullet in bullets:
            screen.blit(fireball_image, (bullet[0], bullet[1]))

            """--- COLISION FIREBALL → ENEMY ---"""
            for enemy in numb_enemy:
                if len(numb_enemy) >0:
                
                    if colision(bullet[0],enemy[0]+20,bullet[1],enemy[1]+20):
                        screen.blit(explosion,(enemy[0],enemy[1]))
                        browser_jr_screem.play()  
                        score_player +=1
                        show_score(10,20)
                        numb_enemy.remove(enemy)
                        bullets.remove(bullet)

                if len(numb_enemy) == 0 :
                    if lvl_state=="level1"or lvl_state=="level2":
                        game_state = 'win'
                    elif lvl_state=="boss":
                        game_state="winboss"

        #draw enemy
        for enemy in numb_enemy:
            screen.blit(enemy_image, (enemy[0], enemy[1]))

            """--- COLISION ENEMY → PLAYER ---"""
            if player_life >0:
                if colision(x,enemy[0]+20,y,enemy[1]+20):
                    numb_enemy.remove(enemy)
                    player_life -= 1
                    show_life(10,60)
                if len(numb_enemy) == 0 :
                    if lvl_state=="level1"or lvl_state=="level2":
                        game_state = 'win'
                    elif lvl_state=="boss":
                        game_state="winboss"
            if player_life == 0 :
                game_state = 'loose'
    
        
    pygame.display.update()
    #pygame.display.flip() 