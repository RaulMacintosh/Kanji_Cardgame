# -*- coding: utf-8 -*-
import pygame
from mainMenu import *

pygame.init()
pygame.display.set_caption('Kanji - Cardgame')
screen = pygame.display.set_mode((795, 411))

done = False

menu = Menu(screen)
menu.draw()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				menu.itemUp()
			if event.key == pygame.K_DOWN:
				menu.itemDown()
			if event.key == pygame.K_RETURN:
				done = menu.selectItem()
    
	pygame.display.flip()