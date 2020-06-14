#current spot in tutorial: 12:42

import pygame
import os
import time
import random

#links image with assets folder and name of pic in order to load ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")) 
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")) 
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")) 

#load in player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")) 

#load in lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#load in background image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("assets", "background-black.png"))
