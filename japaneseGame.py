import pygame
import time
from settingsMenu import *

class Japanese:
	def __init__(self, screen, settingsMenu):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))
		self.settingsMenu = settingsMenu

	def start(self):
		self.fontJapanese = pygame.font.Font("./Fonts/Kengo.ttf", 62)
		self.fontDescription = pygame.font.SysFont("monospace", 25)

		self.japaneseName = self.fontJapanese.render("Japanese", 1, (255,69,0))
		self.descriptionName = self.fontDescription.render("The game will ask for the kanjis, in romaji", 1, (255,255,255))
		sound = pygame.mixer.Sound("./Sounds/Japanese_instructions.wav")
		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.japaneseName, (240, 100))
		self.screen.blit(self.descriptionName, (70, 200))
		pygame.display.flip()
		time.sleep(3)

		self.japaneseName = self.fontJapanese.render("Sorry!", 1, (255,0,0))
		self.descriptionName = self.fontDescription.render("Game mode not implemented", 1, (255,255,255))
		sound = pygame.mixer.Sound("./Sounds/Undone.wav")
		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.japaneseName, (300, 100))
		self.screen.blit(self.descriptionName, (215, 200))
		pygame.display.flip()
		time.sleep(3)