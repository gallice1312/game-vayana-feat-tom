#import module pygame
import pygame
import os 



class Player(object):
    """Spawn player and defined hit box"""
    def __init__(self,x,y,width,height):
        
        #position
        self.x = x
        self.y = y
        #width and height of player
        self.width = width
        self.height = height
        self.vel = 5
        #begening state
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        #define hitbox
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        
        playerImage =  pygame.transform.scale((pygame.image.load('mario.png')),(self.width,self.height))
        screen.blit(playerImage, (100,100)) 
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        pygame.image.load('mario.png').convert()
        
        


#class enemy(object):

#class projectile(object):


#pygame setup 
pygame.init()

screen = pygame.display.set_mode((700,700))
running = True

while running:
    #exit with x on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #set screen color
    bg = (255,255,153)
    screen.fill(bg)

    #add player
    player = Player(100,100,50,50)
    
    pygame.display.update()

  
    pygame.display.flip()


pygame.quit()