import pygame
pygame.init()

# --- SETUP ---
screen = pygame.display.set_mode((1536, 1024))
pygame.display.set_caption("Mario Game")
clock = pygame.time.Clock()

bg_menu = pygame.image.load("backmenu2.png")
bg_game = pygame.image.load("background.png")
bg_pause = pygame.image.load()

game_state = "menu" 

# --- RECTANGLES DU MENU ---
start_rect = pygame.Rect(360, 250, 810, 260)
exit_rect = pygame.Rect(610,550,320,120)

# --- VARIABLES DU JEU ---
x, y = 100, 500
velocity = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_rect.collidepoint(mouse_pos):
                    print("game starting...")
                    game_state = "game"
                elif exit_rect.collidepoint(mouse_pos):
                    running = False

        elif game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # revenir au menu
                    game_state = "menu"
    if game_state == "menu":
        screen.blit(bg_menu, (0, 0))
      

    elif game_state == "game":
        screen.blit(bg_game, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  x -= velocity
        if keys[pygame.K_RIGHT]: x += velocity
        mario = pygame.transform.scale(pygame.image.load("mario.png"), (50,50))
        screen.blit(mario, (x,y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
