import pygame
import random
####################################################################################
# basic set
pygame.init() # to initialize

# game screen resolution setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Dodge dropping poo") # game title

# FPS
clock = pygame.time.Clock()
#
####################################################################################

# 1. user game set (background, game img, coordinates, font, speed, etc)

score = 0

# load background image
background = pygame.image.load("C:\\Users\\Gang\\IdeaProjects\\python projects\\python_games\\background.png")

# load character image
character = pygame.image.load("C:\\Users\\Gang\\IdeaProjects\\python projects\\python_games\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = ((screen_width / 2) - (character_width / 2))
character_y_pos = (screen_height - character_height)


# font
game_font = pygame.font.Font(None, 40)


# coordinates
to_x = 0

# character speed
character_speed = 0.5


# load poo
poo = pygame.image.load("C:\\Users\\Gang\\IdeaProjects\\python projects\\python_games\\poo.png")
poo_size = poo.get_rect().size
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_x_pos = random.randint(0, screen_width - poo_width)
poo_y_pos = 0
poo_speed = 10

# load game_over
game_over = pygame.image.load(r"C:\Users\Gang\IdeaProjects\python projects\python_games\game_over.png")

start_ticks = pygame.time.get_ticks()

# event loop
running = True # is game running?
while running:
    dt = clock.tick(30) # set FPS to 30
    # print("FPS : " + str(clock.get_fps()))

    # 2. event (keyboard, mouse, etc)
    for event in pygame.event.get(): # what kind of event happened?
        if event.type == pygame.QUIT: # quit game when window closed
            running = False # when game is not running

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. define character coordinate

    character_x_pos += to_x * dt

    # screen border
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    poo_y_pos += poo_speed

    if poo_y_pos > screen_height:
        poo_y_pos = 0
        poo_x_pos = random.randint(0, screen_width - poo_width)
        score += 1

    # 4. collision update
    character_rect = character.get_rect()
    character_rect.right = character_x_pos
    character_rect.top = character_y_pos

    poo_rect = poo.get_rect()
    poo_rect.right = poo_x_pos
    poo_rect.top = poo_y_pos

    # 5. display on screen

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(poo, (poo_x_pos, poo_y_pos))

    # timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    final_score = game_font.render(str(int(score)), True, (255, 255, 255))

    if character_rect.colliderect(poo_rect):
        screen.blit(game_over, (190,200))
        screen.blit(final_score, (screen_width/2, 170))
        pygame.display.update()
        print("Collision")
        running = False

    pygame.display.update() # draw background again & again

pygame.time.delay(2000)

# end pygame
pygame.quit()