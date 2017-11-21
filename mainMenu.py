import pygame
from settingsMenu import *
from tutorialMenu import *
from playMenu import *
from aboutMenu import *

class Menu:
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))

		self.currtentItem = 1

		self.fontKanji = pygame.font.Font("./Fonts/Kengo.ttf", 62)
		self.fontCardgame = pygame.font.Font("./Fonts/Kengo.ttf", 32)
		self.fontItens = pygame.font.SysFont("monospace", 25)

		self.kanjiName = self.fontKanji.render("Kanji", 1, (255,69,0))
		self.cardgameName = self.fontCardgame.render("Cardgame", 1, (255,215,0))
		self.jogarName = self.fontItens.render("Play", 1, (0,100,0))
		self.instrucoesName = self.fontItens.render("Tutorial", 1, (255,255,255))
		self.configuracoesName = self.fontItens.render("Settings", 1, (255,255,255))
		self.sobreName = self.fontItens.render("About", 1, (255,255,255))
		self.sairName = self.fontItens.render("Exit", 1, (255,255,255))
		self.kanjiKanji = pygame.image.load('./Images/kanji.png')

		self.settingsMenu = Settings(self.screen)
		self.tutorialMenu = Tutorial(self.screen)
		self.playMenu = Play(self.screen, self.settingsMenu)
		self.aboutMenu = About(self.screen)

		self.playSound(1)

	def playSound(self, idSound):
		sound = pygame.mixer.Sound("./Sounds/Play.wav")
		if idSound == 1:
			sound = pygame.mixer.Sound("./Sounds/Play.wav")
		elif idSound == 2:
			sound = pygame.mixer.Sound("./Sounds/Tutorial.wav")
		elif idSound == 3:
			sound = pygame.mixer.Sound("./Sounds/Settings.wav")
		elif idSound == 4:
			sound = pygame.mixer.Sound("./Sounds/About.wav")
		elif idSound == 5:
			sound = pygame.mixer.Sound("./Sounds/Exit.wav")

		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

	def draw(self):
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.kanjiName, (325, 50))
		self.screen.blit(self.cardgameName, (315, 125))
		self.screen.blit(self.jogarName, (30, 200))
		self.screen.blit(self.instrucoesName, (30, 230))
		self.screen.blit(self.configuracoesName, (30, 260))
		self.screen.blit(self.sobreName, (30, 290))
		self.screen.blit(self.sairName, (30, 320))
		self.screen.blit(self.kanjiKanji, (450, 225))

	def itemUp(self):
		if self.currtentItem == 1:
			pass
		else:
			self.currtentItem -= 1
			self.jogarName = self.fontItens.render("Play", 1, (255,255,255))
			self.instrucoesName = self.fontItens.render("Tutorial", 1, (255,255,255))
			self.configuracoesName = self.fontItens.render("Settings", 1, (255,255,255))
			self.sobreName = self.fontItens.render("About", 1, (255,255,255))
			self.sairName = self.fontItens.render("Exit", 1, (255,255,255))

			if self.currtentItem == 1:
				self.jogarName = self.fontItens.render("Play", 1, (0,100,0))
			elif self.currtentItem == 2:
				self.instrucoesName = self.fontItens.render("Tutorial", 1, (0,100,0))
			elif self.currtentItem == 3:
				self.configuracoesName = self.fontItens.render("Settings", 1, (0,100,0))
			elif self.currtentItem == 4:
				self.sobreName = self.fontItens.render("About", 1, (0,100,0))
			elif self.currtentItem == 5:
				self.sairName = self.fontItens.render("Exit", 1, (0,100,0))

			self.playSound(self.currtentItem)
			self.draw()

	def itemDown(self):
		if self.currtentItem == 5:
			pass
		else:
			self.currtentItem += 1
			self.jogarName = self.fontItens.render("Play", 1, (255,255,255))
			self.instrucoesName = self.fontItens.render("Tutorial", 1, (255,255,255))
			self.configuracoesName = self.fontItens.render("Settings", 1, (255,255,255))
			self.sobreName = self.fontItens.render("About", 1, (255,255,255))
			self.sairName = self.fontItens.render("Exit", 1, (255,255,255))

			if self.currtentItem == 1:
				self.jogarName = self.fontItens.render("Play", 1, (0,100,0))
			elif self.currtentItem == 2:
				self.instrucoesName = self.fontItens.render("Tutorial", 1, (0,100,0))
			elif self.currtentItem == 3:
				self.configuracoesName = self.fontItens.render("Settings", 1, (0,100,0))
			elif self.currtentItem == 4:
				self.sobreName = self.fontItens.render("About", 1, (0,100,0))
			elif self.currtentItem == 5:
				self.sairName = self.fontItens.render("Exit", 1, (0,100,0))

			self.playSound(self.currtentItem)
			self.draw()

	def selectItem(self):
		if self.currtentItem == 1:
		 	self.playMenu.draw()
		 	done = False
		 	while not done:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP:
							self.playMenu.itemUp()
						if event.key == pygame.K_DOWN:
							self.playMenu.itemDown()
						if event.key == pygame.K_RETURN:
							done = self.playMenu.selectItem()

				pygame.display.flip()
			self.draw()
		elif self.currtentItem == 2:
			self.tutorialMenu.draw()
			done = False
			while not done:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							done = True

				pygame.display.flip()
			self.draw()
		elif self.currtentItem == 3:
			self.settingsMenu.draw()
			done = False
			while not done:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP:
							self.settingsMenu.itemUp()
						if event.key == pygame.K_DOWN:
							self.settingsMenu.itemDown()
						if event.key == pygame.K_LEFT:
							done = self.settingsMenu.itemLeft()
						if event.key == pygame.K_RIGHT:
							done = self.settingsMenu.itemRight()
						if event.key == pygame.K_RETURN:
							done = self.settingsMenu.selectItem()

				pygame.display.flip()
			self.draw()
		elif self.currtentItem == 4:
			self.aboutMenu.draw()
			done = False
			while not done:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							done = True

				pygame.display.flip()
			self.draw()
		elif self.currtentItem == 5:
			return True