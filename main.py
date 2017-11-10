# -*- coding: utf-8 -*-
import pygame
from mainMenu import *
from threading import Thread

class BackgroundSong(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		pygame.mixer.music.load("./Sounds/background.mp3")
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.2)

pygame.init()
pygame.display.set_caption('Kanji - Cardgame')
screen = pygame.display.set_mode((795, 411))

done = False

song = BackgroundSong()
song.start()

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