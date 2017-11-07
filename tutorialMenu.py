import pygame

class Tutorial:
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))

		self.fontTutorial = pygame.font.Font("./Fonts/Kengo.ttf", 52)
		self.fontHowToPlay = pygame.font.Font("./Fonts/Kengo.ttf", 32)

		self.tutorialName = self.fontTutorial.render("Tutorial", 1, (255,69,0))
		self.howToPlayName = self.fontHowToPlay.render("Como jogar?", 1, (255,215,0))

	def draw(self):
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.tutorialName, (275, 50))
		self.screen.blit(self.howToPlayName, (30, 200))