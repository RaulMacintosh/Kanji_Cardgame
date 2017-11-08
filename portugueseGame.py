import pygame
import time
from settingsMenu import *

class Portuguese:
	def __init__(self, screen, settingsMenu):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))
		self.settingsMenu = settingsMenu

	def start(self):
		self.fontPortuguese = pygame.font.Font("./Fonts/Kengo.ttf", 62)
		self.fontDescription = pygame.font.SysFont("monospace", 25)

		self.portugueseName = self.fontPortuguese.render("Portuguese", 1, (255,69,0))
		self.descriptionName = self.fontDescription.render("The game will ask for the kanjis, in portuguese", 1, (255,255,255))

		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.portugueseName, (215, 100))
		self.screen.blit(self.descriptionName, (40, 200))
		pygame.display.flip()
		time.sleep(3)

		self.portugueseName = self.fontPortuguese.render("Sorry!", 1, (255,0,0))
		self.descriptionName = self.fontDescription.render("Game mode not implemented", 1, (255,255,255))

		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.portugueseName, (300, 100))
		self.screen.blit(self.descriptionName, (215, 200))
		pygame.display.flip()
		time.sleep(3)