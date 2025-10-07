#import module pygame
import pygame
from pygame.locals import *
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
screen = pygame.display.set_mode((700,700))
screen_update = pygame.transform.scale_by(bg_image,(700,700))

#set clock
clock = pygame.time.Clock()
#Score
score_player = 0
player_life = 3

"""--- PLAYER SETTINGS ---"""
#player direction
direction = True
# velocity of player's movement
player_speed = 10
x =360
y=580

<<<<<<< Updated upstream
bullets = [] # This goes right above the while loop

def projectile(x,y):
    pygame.draw.circle(screen,(255,0,0),(x,y), 10)

=======
"""--- ENEMY SETTINGS ---"""
numb_enemy = [[50,50,-1],[250,50,-1],[200,100,1]]
enemy_speed = 5
>>>>>>> Stashed changes



"""--- FUNCTION --"""

def colision(x,enemy_x,y,enemy_y):
    if abs(x-enemy_x) <= 2 or abs(y - enemy_y) <=2:
        return True
    else :
        return False

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
    if keys[K_RIGHT] and x < 650:
        x += player_speed
        direction = True           #right

    if keys[K_SPACE]:
    # create new fireball
        #not more than 10 fireball displayed on the screen
        if len(bullets) < 10:
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
        if enemy[0] <= 0 or enemy[0] >= 660:
            enemy[2] *= -1  # reset enemy direction
            enemy[1] += 10  # go down a lil at every corner
        
        
        

    """--- DRAW EVERYTHING---"""
    #draw background
    draw_background()
    #draww player
    draw_player(x,y)
    
<<<<<<< Updated upstream

    key_pressed_is = pygame.key.get_pressed()
    # Changing the coordinates
    # of the player
    if event.type==KEYDOWN:

        if key_pressed_is[K_LEFT]:
            x -= 10
        if key_pressed_is[K_RIGHT]:
            x += 10

        if key_pressed_is[K_SPACE]:
            projectile(x,100)


    screen.blit(bg_image,(0,0))

    #set player
    image =  pygame.transform.scale((pygame.image.load('mario.png')),(50,50))
    #reset background
    screen.blit(image, (x,580))
 
=======
    
    #draw fire ball
    for bullet in bullets:
        screen.blit(fireball_image, (bullet[0], bullet[1]))

        """--- COLISION PLAYER → ENEMY ---"""
    
        


    #draw enemy
    for enemy in numb_enemy:
        screen.blit(enemy_image, (enemy[0], enemy[1]))

        """--- COLISION ENEMY → PLAYER ---"""
         
        
>>>>>>> Stashed changes
        
    pygame.display.update()
    #pygame.display.flip() 