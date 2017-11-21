import pygame
import time

class About:
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))

		self.fontAbout = pygame.font.Font("./Fonts/Kengo.ttf", 52)
		self.fontDescription = pygame.font.SysFont("monospace", 20)

		self.aboutName = self.fontAbout.render("About", 1, (255,69,0))
		self.descriptionName = self.fontDescription.render("This game was designed on Information Technology undergraduate course", 1, (255,255,255))
		self.description2Name = self.fontDescription.render("of the Federal University of Rio Grande do Norte - Brazil, for the course of", 1, (255,255,255))
		self.description3Name = self.fontDescription.render("Human-Computer Interaction.", 1, (255,255,255))
		self.description4Name = self.fontDescription.render("Student: Raul Silveira Silva", 1, (255,255,255))
		self.description5Name = self.fontDescription.render("Mentor: Dr. Leonardo Cunha de Miranda", 1, (255,255,255))
		self.backName = self.fontDescription.render("Back", 1, (0,100,0))

	def draw(self):
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.aboutName, (275, 50))
		self.screen.blit(self.descriptionName, (30, 200))
		self.screen.blit(self.description2Name, (30, 225))
		self.screen.blit(self.description3Name, (30, 250))
		self.screen.blit(self.description4Name, (30, 300))
		self.screen.blit(self.description5Name, (30, 325))
		self.screen.blit(self.backName, (700, 350))
		pygame.display.flip()

		sound = pygame.mixer.Sound("./Sounds/About_Description.wav")
		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)
		time.sleep(19)
		sound = pygame.mixer.Sound("./Sounds/Back.wav")
		pygame.mixer.Sound.play(sound)