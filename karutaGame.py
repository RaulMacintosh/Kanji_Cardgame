import pygame
import time
from settingsMenu import *

class Karuta:
	def __init__(self, screen, settingsMenu):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))
		self.settingsMenu = settingsMenu

	def start(self):
		self.fontKaruta = pygame.font.Font("./Fonts/Kengo.ttf", 62)
		self.fontDescription = pygame.font.SysFont("monospace", 25)

		self.karutaName = self.fontKaruta.render("Karuta", 1, (255,69,0))
		self.descriptionName = self.fontDescription.render("Game with unlimited time", 1, (255,255,255))
		sound = pygame.mixer.Sound("./Sounds/Karuta_instructions.wav")
		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.karutaName, (300, 100))
		self.screen.blit(self.descriptionName, (220, 200))
		pygame.display.flip()
		time.sleep(3)

		self.karutaName = self.fontKaruta.render("Sorry!", 1, (255,0,0))
		self.descriptionName = self.fontDescription.render("Game mode not implemented", 1, (255,255,255))
		sound = pygame.mixer.Sound("./Sounds/Undone.wav")
		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.karutaName, (300, 100))
		self.screen.blit(self.descriptionName, (215, 200))
		pygame.display.flip()
		time.sleep(3)