#import module pygame
import pygame
import os 



class player(object):
    """Spawn player and defined hit box"""
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        #hitbox
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) 

        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('images', 'mario.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

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
    screen.fill((255,255,153))
    

    pygame.display.flip()


pygame.quit()