import pygame
from mainMenu import *

class Settings:
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))

		self.soundBar = unichr(0x25AE) + unichr(0x25AE) + unichr(0x25AE) + unichr(0x25AE) + unichr(0x25AE) + unichr(0x25AF) + unichr(0x25AF) + unichr(0x25AF) + unichr(0x25AF) + unichr(0x25AF)
		self.easyRadio = unichr(0x25C9)
		self.normalRadio = unichr(0x25CB)
		self.hardRadio = unichr(0x25CB)

		self.currtentItem = 1

		self.fontSettings = pygame.font.Font("./Fonts/Kengo.ttf", 52)
		self.fontItens = pygame.font.SysFont("monospace", 25)

		self.settingsName = self.fontSettings.render("Settings", 1, (255,69,0))
		
		self.soundName = self.fontItens.render("Sound Level: -            +", 1, (255,255,255))
		self.soundBarName = self.fontItens.render(self.soundBar, 1, (0,100,0))
		
		self.levelName = self.fontItens.render("Difficulty Level:   Easy    Normal    Hard", 1, (255,255,255))
		self.easyRadioName = self.fontItens.render(self.easyRadio, 1, (255,255,255))
		self.normalRadioName = self.fontItens.render(self.normalRadio, 1, (255,255,255))
		self.hardRadioName = self.fontItens.render(self.hardRadio, 1, (255,255,255))

		self.timeName = self.fontItens.render("Time to find the Kanji: ", 1, (255,255,255))
		self.backName = self.fontItens.render("Back", 1, (255,255,255))

	def draw(self):
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.settingsName, (275, 50))

		self.screen.blit(self.soundName, (30, 200))
		self.screen.blit(self.soundBarName, (250, 200))

		self.screen.blit(self.levelName, (30, 230))

		
		self.screen.blit(self.timeName, (30, 260))
		self.screen.blit(self.backName, (700, 350))

	def itemUp(self):
		if self.currtentItem == 1:
			pass
		else:
			self.currtentItem -= 1
			self.soundName = self.fontItens.render("Sound Level: -            +", 1, (255,255,255))
			self.soundBarName = self.fontItens.render(self.soundBar, 1, (255,255,255))
			self.levelName = self.fontItens.render("Difficulty Level: ", 1, (255,255,255))
			self.timeName = self.fontItens.render("Time to find the Kanji: ", 1, (255,255,255))
			self.backName = self.fontItens.render("Back", 1, (255,255,255))

			if self.currtentItem == 1:
				self.soundName = self.fontItens.render("Sound Level: -            +", 1, (255,255,255))
				self.soundBarName = self.fontItens.render(self.soundBar, 1, (0,100,0))
			elif self.currtentItem == 2:
				self.levelName = self.fontItens.render("Difficulty Level: ", 1, (0,100,0))
			elif self.currtentItem == 3:
				self.timeName = self.fontItens.render("Time to find the Kanji: ", 1, (0,100,0))
			elif self.currtentItem == 4:
				self.backName = self.fontItens.render("Back", 1, (0,100,0))

			self.draw()

	def itemDown(self):
		if self.currtentItem == 4:
			pass
		else:
			self.currtentItem += 1
			self.soundName = self.fontItens.render("Sound Level: -            +", 1, (255,255,255))
			self.soundBarName = self.fontItens.render(self.soundBar, 1, (255,255,255))
			self.levelName = self.fontItens.render("Difficulty Level: ", 1, (255,255,255))
			self.timeName = self.fontItens.render("Time to find the Kanji: ", 1, (255,255,255))
			self.backName = self.fontItens.render("Back", 1, (255,255,255))

			if self.currtentItem == 1:
				self.soundName = self.fontItens.render("Sound Level: -            +", 1, (255,255,255))
				self.soundBarName = self.fontItens.render(self.soundBar, 1, (0,100,0))
			elif self.currtentItem == 2:
				self.levelName = self.fontItens.render("Difficulty Level: ", 1, (0,100,0))
			elif self.currtentItem == 3:
				self.timeName = self.fontItens.render("Time to find the Kanji: ", 1, (0,100,0))
			elif self.currtentItem == 4:
				self.backName = self.fontItens.render("Back", 1, (0,100,0))

			self.draw()

	def selectItem(self):
		if self.currtentItem == 4:
			return True