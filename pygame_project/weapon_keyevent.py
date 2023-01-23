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

# character direction
character_to_x = 0

# character speed
character_speed = 5

# creating weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# be able to take multiple shots at once
weapons = []

# weapon speed
weapon_speed = 10

# create bubbles
bubbles_images = [
    pygame.image.load(os.path.join(image_path, "bubble1.png")),
    pygame.image.load(os.path.join(image_path, "bubble2.png")),
    pygame.image.load(os.path.join(image_path, "bubble3.png")),
    pygame.image.load(os.path.join(image_path, "bubble4.png"))]

# speed of bubbles by its size
bubbles_speed_y = [-18, -15, -12, -9] # value of index 0, 1, 2, 3

# bubbles
bubbles = []

# the biggest, first bubble
bubbles.append({
    "pos_x": 50, # x coordinate of bubble
    "pos_y": 50, # y coordinate of bubble
    "img_idx": 0, # image index of bubble
    "to_x": 3, # moving direction of x-axis, -3 to the left or 3 to the right
    "to_y": -6, # moving direction of y-axis
    "init_spd_y": bubbles_speed_y[0]}) # lowest speed of y

running = True # is game running? True -> Yes
while running:
    dt = clock.tick(60) # set FPS to 60

    # 2. event (keyboard, mouse, etc)
    for event in pygame.event.get(): # what kind of event happened?
        if event.type == pygame.QUIT: # quit game when window closed
            running = False # when game is not running

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # character to the left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # character to the right
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # fire the weapon
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. define character coordinate

    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # define weapon's coordinate / location
    weapons = [ [w[0], w[1]- weapon_speed] for w in weapons] # weapon to move above by its speed

    # remove weapon that reached top
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # define bubble's coordinate / location
    for bubbles_idx, bubbles_val in enumerate(bubbles):
        bubbles_pos_x = bubbles_val["pos_x"]
        bubbles_pos_y = bubbles_val["pos_y"]
        bubbles_img_idx = bubbles_val["img_idx"]

        bubbles_size = bubbles_images[bubbles_img_idx].get_rect().size
        bubbles_width = bubbles.size[0]
        bubbles_height = bubbles.size[1]

        # when bubble hits the side wall, switch its direction (bouncing off the wall)
        if bubbles_pos_x < 0 or bubbles_pos_x > screen_width - bubbles_width:
            bubbles_val["to_x"] = bubbles_val["to_x"] * -1

        # y-axis coordinate / location
        # bouncing off the stage and moving upward
        if bubbles_pos_y >= screen_height - stage_height - bubbles_height:
            bubbles_val["to_y"] = bubbles_val["init_spd_y"]
        else: # accelerate in rest of the cases
            bubbles_val["to_y"] += 0.5

        bubbles_val["pos_x"] += bubbles_val["pos_x"]
        bubbles_val["pos_y"] += bubbles_val["pos_y"]

# 4. collision update

    # 5. display on screen
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(bubbles):
        bubbles_pos_x = val["pos_x"]
        bubbles_pos_y = val["pos_y"]
        bubbles_img_idx = val["img_idx"]
        screen.blit(bubbles_images[bubbles_img_idx], (bubbles_pos_x, bubbles_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # draw background again & again

# end pygame
pygame.quit()