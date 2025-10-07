#import module pygame
import pygame
from pygame.locals import *
import math

#pygame setup 
pygame.init()
running = True


"""--- IMAGE ---"""
#fireball image
fireball_image =  pygame.transform.scale((pygame.image.load('fireball.png')),(10,10))
#set player
player_image =  pygame.transform.scale((pygame.image.load('mario.png')),(50,50))
#background image
bg_image = pygame.image.load('background.png')
#enemy image
enemy_image = pygame.transform.scale((pygame.image.load('spaceship.png')),(60,60))

"""--- SET SCREEN ---"""
#set screen
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

#set clock
clock = pygame.time.Clock()

"""--- WIN SCREEN ---"""

"""--- LOOSE SCREEN ---"""


"""--- PLAYER SETTINGS ---"""
#player direction
direction = True
# velocity of player's movement
player_speed = 10
x =350
y=580
player_life = 3

"""--- ENEMY SETTINGS ---"""
numb_enemy = [[50,50,-1],[250,50,-1],[200,100,1]]
enemy_speed = 5



"""--- COLISION --"""

def colision(x,enemy_x,y,enemy_y):
    distance = math.sqrt((math.pow(x - enemy_x, 2)) + (math.pow(y - enemy_y, 2)))
    if distance <= 40:
        return True
    else:
        return False

"""--- FONT ---"""
font = pygame.font.Font('freesansbold.ttf', 20)


"""--- SHOW SCORE ---"""
#Score
score_player = 0
def show_score(x,y):
    score = font.render("Points: " + str(score_player), True, (255,255,255))
    screen.blit(score, (x , y ))


"""--- DRAW ---"""
def draw_background():
    screen.blit(bg_image,(0,0))

def draw_player(x,y):
    screen.blit(player_image, (x,y))


"""--- BULLET SETTINGS ---"""
bullet_speed = -15  # vers le haut
bullets = [] 

    
"""--- MAIN LOOP ---"""
while running:
    
    # Set the frame rates to 60 fps
    clock.tick(60)
    
    """--- EVENT ---"""
    
    for event in pygame.event.get():
        #exit with x on the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        
    """--- MOVEMENT KEYS """
    #get key pressed and move character
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and x > 0:
        x -= player_speed
        direction = False          #left
    if keys[K_RIGHT] and x < 1536:
        x += player_speed
        direction = True           #right

    if keys[K_SPACE]:
    # create new fireball
        #not more than 10 fireball displayed on the screen
        if len(bullets) < 5:
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
        if enemy[0] <= 0 or enemy[0] >= 1536:
            enemy[2] *= -1  # reset enemy direction
            enemy[1] += 10  # go down a lil at every corner
        
        
        

    """--- DRAW EVERYTHING---"""
    #draw background
    draw_background()
    #draww player
    draw_player(x,y)
    #draw score
    show_score(10,10)
    
    #draw fire ball
    for bullet in bullets:
        screen.blit(fireball_image, (bullet[0], bullet[1]))

        """--- COLISION FIREBALL → ENEMY ---"""
        for enemy in numb_enemy:
            if len(numb_enemy) >0:
                if colision(bullet[0],enemy[0],bullet[1],enemy[1]):
                    score_player +=1
                    show_score(10,10)
                    numb_enemy.remove(enemy)

            if len(numb_enemy) == 0 :
                print('YOU WIN')
    
        


    #draw enemy
    for enemy in numb_enemy:
        screen.blit(enemy_image, (enemy[0], enemy[1]))

        """--- COLISION ENEMY → PLAYER ---"""
        if player_life >0:
            if colision(x,enemy[0],y,enemy[1]):
                player_life -= 1
        if player_life == 0 :
            break

    
        
    pygame.display.update()
    #pygame.display.flip() 