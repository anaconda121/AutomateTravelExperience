import pygame 
import os
from enemies.enemy import draw

def loadVirus():
	imgs = []
	for x in range(20):
		#pygame.image.load(os.path.join("enemies", "enemies", "virus", "download_000.png"))
		imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("enemies","enemies","virus", "download_" + (f'{x:03}') + ".png")),(64, 64))) # generates padded string