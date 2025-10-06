#import module pygame
import pygame
from pygame.locals import *

#pygame setup 
pygame.init()

running = True

#set screen
screen = pygame.display.set_mode((700,700))
#set screen color
bg_image = pygame.image.load('background.png')

#set clock
clock = pygame.time.Clock()

#player direction
direction = True

# velocity of player's movement
velocity = 12
x =360

bullets = [] # This goes right above the while loop

def projectile(x):
    fireball_image =  pygame.transform.scale((pygame.image.load('fireball.png')),(10,10))
    screen.blit(fireball_image, (x,400))


while running:

    
    # Set the frame rates to 60 fps
    clock.tick(60)
    
    #exit with x on the window
    for event in pygame.event.get():

        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = True
            elif event.key == pygame.K_LEFT:
                direction = False

    

    key_pressed_is = pygame.key.get_pressed()
    # Changing the coordinates
    # of the player
    if event.type==KEYDOWN:

        if key_pressed_is[K_LEFT]:
            x -= 10
        if key_pressed_is[K_RIGHT]:
            x += 10

        if key_pressed_is[K_SPACE]:
            projectile(x)



    screen.blit(bg_image,(0,0))

    #set player
    image =  pygame.transform.scale((pygame.image.load('mario.png')),(50,50))
    #reset background
    screen.blit(image, (x,580))
    
 
        
    pygame.display.update()

    #pygame.display.flip() 

