import os
import pygame
####################################################################################
# basic set
pygame.init() # to initialize

# game screen resolution setting
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Bubble Pang") # game title

# FPS
clock = pygame.time.Clock()
####################################################################################

# 1. user game set (background, game img, coordinates, font, speed, etc)
current_path = os.path.dirname(__file__) # returns current file location
image_path = os.path.join(current_path, "images") # return location of images folder

# background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # to place character on top of stage height

# character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = ((screen_width / 2) - (character_width / 2))
character_y_pos = (screen_height - character_height - stage_height)


running = True # is game running? True -> Yes
while running:
    dt = clock.tick(60) # set FPS to 60
    #print("FPS : " + str(clock.get_fps()))

    # 2. event (keyboard, mouse, etc)
    for event in pygame.event.get(): # what kind of event happened?
        if event.type == pygame.QUIT: # quit game when window closed
            running = False # when game is not running

    # 3. define character coordinate

    # 4. collision update

    # 5. display on screen
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # draw background again & again

# end pygame
pygame.quit()