import pygame

class Tutorial:
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))

		self.fontTutorial = pygame.font.Font("./Fonts/Kengo.ttf", 52)
		self.fontHowToPlay = pygame.font.Font("./Fonts/Kengo.ttf", 22)
		self.fontDescription = pygame.font.SysFont("monospace", 25)

		self.tutorialName = self.fontTutorial.render("Tutorial", 1, (255,69,0))
		self.howToPlayName = self.fontHowToPlay.render("How to play?", 1, (255,215,0))
		self.descriptionName = self.fontDescription.render("Put the card", 1, (255,255,255))
		self.description2Name = self.fontDescription.render("over the Kanji", 1, (255,255,255))
		self.description3Name = self.fontDescription.render("reader.", 1, (255,255,255))
		self.backName = self.fontDescription.render("Back", 1, (0,100,0))

		self.rfidCard = pygame.image.load('./Images/rfidCard.png')

	def draw(self):
		sound = pygame.mixer.Sound("./Sounds/Put_the_card_over_the_Kanji_reader.wav")
		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)
		time.sleep(1)
		sound = pygame.mixer.Sound("./Sounds/Back.wav")
		pygame.mixer.Sound.play(sound)
		
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.tutorialName, (275, 50))
		self.screen.blit(self.howToPlayName, (30, 150))
		self.screen.blit(self.descriptionName, (30, 200))
		self.screen.blit(self.description2Name, (30, 225))
		self.screen.blit(self.description3Name, (30, 250))
		self.screen.blit(self.backName, (700, 350))
		self.screen.blit(self.rfidCard, (425, 125))