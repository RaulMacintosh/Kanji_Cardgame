import pygame
import time

class Settings:
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))

		self.soundBar = unichr(0x25AE) + unichr(0x25AE) + unichr(0x25AE) + unichr(0x25AE) + unichr(0x25AE) + unichr(0x25AF) + unichr(0x25AF) + unichr(0x25AF) + unichr(0x25AF) + unichr(0x25AF)
		self.easyRadio = unichr(0x25C9)
		self.normalRadio = unichr(0x25CB)
		self.hardRadio = unichr(0x25CB)
		self.timeValue = 5
		self.radioCurrentSelected = 1

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

		self.timeName = self.fontItens.render("Time to find the Kanji: -    +", 1, (255,255,255))
		self.secondsName = self.fontItens.render(str(self.timeValue) + "s", 1, (255,255,255))

		self.backName = self.fontItens.render("Back", 1, (255,255,255))

	def playSound(self, idSound):
		sound = pygame.mixer.Sound("./Sounds/Sound_level.wav")
		if idSound == 1:
			sound = pygame.mixer.Sound("./Sounds/Sound_level.wav")
		elif idSound == 2:
			sound = pygame.mixer.Sound("./Sounds/Difficulty_level.wav")
		elif idSound == 3:
			sound = pygame.mixer.Sound("./Sounds/Time_to_find_the_Kanji.wav")
		elif idSound == 4:
			sound = pygame.mixer.Sound("./Sounds/Back.wav")

		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

	def playRadioSound(self, idSound):
		sound = pygame.mixer.Sound("./Sounds/Easy.wav")
		if idSound == 1:
			sound = pygame.mixer.Sound("./Sounds/Easy.wav")
		elif idSound == 2:
			sound = pygame.mixer.Sound("./Sounds/Normal.wav")
		elif idSound == 3:
			sound = pygame.mixer.Sound("./Sounds/Hard.wav")

		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

	def draw(self):		
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.settingsName, (275, 50))

		self.screen.blit(self.soundName, (30, 200))
		self.screen.blit(self.soundBarName, (250, 200))

		self.screen.blit(self.levelName, (30, 230))
		self.screen.blit(self.easyRadioName, (300, 230))
		self.screen.blit(self.normalRadioName, (420, 230))
		self.screen.blit(self.hardRadioName, (570, 230))

		self.screen.blit(self.timeName, (30, 260))
		self.screen.blit(self.secondsName, (420, 260))

		self.screen.blit(self.backName, (700, 350))

	def soundLeft(self):
		for x in range(0,10):
			char = self.soundBar[x]

			if x > 0 and char == unichr(0x25AF):
				self.soundBar = self.soundBar[:x-1] + unichr(0x25AF) + self.soundBar[x:]
				break
			if x == 9:
				self.soundBar = self.soundBar[:x] + unichr(0x25AF)

		self.draw()

	def soundRight(self):
		for x in range(0,10):
			char = self.soundBar[x]

			if x < 10 and char == unichr(0x25AF):
				self.soundBar = self.soundBar[:x] + unichr(0x25AE) + self.soundBar[x+1:]
				break
			if x == 0 and char == unichr(0x25AF):
				self.soundBar[x] = unichr(0x25AE)

		self.draw()

	def radioLeft(self, sound):
		self.easyRadio = unichr(0x25CB)
		self.normalRadio = unichr(0x25CB)
		self.hardRadio = unichr(0x25CB)
		self.easyRadioName = self.fontItens.render(self.easyRadio, 1, (255,255,255))
		self.normalRadioName = self.fontItens.render(self.normalRadio, 1, (255,255,255))
		self.hardRadioName = self.fontItens.render(self.hardRadio, 1, (255,255,255))

		if self.radioCurrentSelected == 1:
			self.easyRadio = unichr(0x25C9)
			self.easyRadioName = self.fontItens.render(self.easyRadio, 1, (0,100,0))
		elif self.radioCurrentSelected == 2:
			self.easyRadio = unichr(0x25C9)
			self.normalRadio = unichr(0x25CB)
			self.radioCurrentSelected -= 1
			self.easyRadioName = self.fontItens.render(self.easyRadio, 1, (0,100,0))
		elif self.radioCurrentSelected == 3:
			self.normalRadio = unichr(0x25C9)
			self.hardRadio = unichr(0x25CB)
			self.radioCurrentSelected -= 1
			self.normalRadioName = self.fontItens.render(self.normalRadio, 1, (0,100,0))

		self.draw()
		if sound:
			self.playRadioSound(self.radioCurrentSelected)

	def radioRight(self, sound):
		self.easyRadio = unichr(0x25CB)
		self.normalRadio = unichr(0x25CB)
		self.hardRadio = unichr(0x25CB)
		self.easyRadioName = self.fontItens.render(self.easyRadio, 1, (255,255,255))
		self.normalRadioName = self.fontItens.render(self.normalRadio, 1, (255,255,255))
		self.hardRadioName = self.fontItens.render(self.hardRadio, 1, (255,255,255))

		if self.radioCurrentSelected == 1:
			self.easyRadio = unichr(0x25CB)
			self.normalRadio = unichr(0x25C9)
			self.radioCurrentSelected += 1
			self.normalRadioName = self.fontItens.render(self.normalRadio, 1, (0,100,0))
		elif self.radioCurrentSelected == 2:
			self.normalRadio = unichr(0x25CB)
			self.hardRadio = unichr(0x25C9)
			self.radioCurrentSelected += 1
			self.hardRadioName = self.fontItens.render(self.hardRadio, 1, (0,100,0))
		elif self.radioCurrentSelected == 3:
			self.hardRadio = unichr(0x25C9)
			self.hardRadioName = self.fontItens.render(self.hardRadio, 1, (0,100,0))
		
		self.draw()
		if sound:
			self.playRadioSound(self.radioCurrentSelected)

	def timeLeft(self):
		if self.timeValue == 5:
			pass
		else:
			self.timeValue -= 1

	def timeRight(self):
		if self.timeValue == 30:
			pass
		else:
			self.timeValue += 1

	def itemLeft(self):
		if self.currtentItem == 1:
			self.soundLeft()
			self.soundBarName = self.fontItens.render(self.soundBar, 1, (0,100,0))
		elif self.currtentItem == 2:
			self.radioLeft(True)
		elif self.currtentItem == 3:
			self.timeLeft()
			self.secondsName = self.fontItens.render(str(self.timeValue) + "s", 1, (0,100,0))

		self.draw()

	def itemRight(self):
		if self.currtentItem == 1:
			self.soundRight()
			self.soundBarName = self.fontItens.render(self.soundBar, 1, (0,100,0))
		elif self.currtentItem == 2:
			self.radioRight(True)
		elif self.currtentItem == 3:
			self.timeRight()
			self.secondsName = self.fontItens.render(str(self.timeValue) + "s", 1, (0,100,0))
		
		self.draw()

	def itemUp(self):
		if self.currtentItem == 1:
			pass
		else:
			self.currtentItem -= 1
			self.soundName = self.fontItens.render("Sound Level: -            +", 1, (255,255,255))
			self.soundBarName = self.fontItens.render(self.soundBar, 1, (255,255,255))
			
			self.levelName = self.fontItens.render("Difficulty Level:   Easy    Normal    Hard", 1, (255,255,255))
			self.easyRadioName = self.fontItens.render(self.easyRadio, 1, (255,255,255))
			self.normalRadioName = self.fontItens.render(self.normalRadio, 1, (255,255,255))
			self.hardRadioName = self.fontItens.render(self.hardRadio, 1, (255,255,255))

			self.timeName = self.fontItens.render("Time to find the Kanji: -    +", 1, (255,255,255))
			self.secondsName = self.fontItens.render(str(self.timeValue) + "s", 1, (255,255,255))

			self.backName = self.fontItens.render("Back", 1, (255,255,255))

			if self.currtentItem == 1:
				self.soundBarName = self.fontItens.render(self.soundBar, 1, (0,100,0))
			elif self.currtentItem == 2:
				if self.radioCurrentSelected == 1 or self.radioCurrentSelected == 2:
					self.radioCurrentSelected += 1
					self.radioLeft(False)
				else:
					self.radioCurrentSelected -= 1
					self.radioRight(False)
			elif self.currtentItem == 3:
				self.secondsName = self.fontItens.render(str(self.timeValue) + "s", 1, (0,100,0))
			elif self.currtentItem == 4:
				self.backName = self.fontItens.render("Back", 1, (0,100,0))

			self.draw()
			self.playSound(self.currtentItem)

	def itemDown(self):
		if self.currtentItem == 4:
			pass
		else:
			self.currtentItem += 1
			self.soundName = self.fontItens.render("Sound Level: -            +", 1, (255,255,255))
			self.soundBarName = self.fontItens.render(self.soundBar, 1, (255,255,255))
			
			self.levelName = self.fontItens.render("Difficulty Level:   Easy    Normal    Hard", 1, (255,255,255))
			self.easyRadioName = self.fontItens.render(self.easyRadio, 1, (255,255,255))
			self.normalRadioName = self.fontItens.render(self.normalRadio, 1, (255,255,255))
			self.hardRadioName = self.fontItens.render(self.hardRadio, 1, (255,255,255))

			self.timeName = self.fontItens.render("Time to find the Kanji: -    +", 1, (255,255,255))
			self.secondsName = self.fontItens.render(str(self.timeValue) + "s", 1, (255,255,255))

			self.backName = self.fontItens.render("Back", 1, (255,255,255))

			if self.currtentItem == 1:
				self.soundName = self.fontItens.render("Sound Level: -            +", 1, (255,255,255))
				self.soundBarName = self.fontItens.render(self.soundBar, 1, (0,100,0))
			elif self.currtentItem == 2:
				if self.radioCurrentSelected == 1 or self.radioCurrentSelected == 2:
					self.radioCurrentSelected += 1
					self.radioLeft(False)
				else:
					self.radioCurrentSelected -= 1
					self.radioRight(False)
			elif self.currtentItem == 3:
				self.secondsName = self.fontItens.render(str(self.timeValue) + "s", 1, (0,100,0))
			elif self.currtentItem == 4:
				self.backName = self.fontItens.render("Back", 1, (0,100,0))

			self.draw()
			self.playSound(self.currtentItem)

	def selectItem(self):
		if self.currtentItem == 4:
			return True