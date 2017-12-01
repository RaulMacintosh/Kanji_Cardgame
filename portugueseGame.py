# -*- coding: utf8 -*-

import pygame
import time
import MFRC522
import RPi.GPIO as GPIO
from threading import Thread
from settingsMenu import *
from random import randint

counter = 5
kanjiFounded = 0
lifes = 3
kanjisNumber = 5
fileName = "./Files/portuguese_easy.txt"

class CardReader(Thread):
	def __init__(self, cardName):
		Thread.__init__(self)
		file = open("./Files/cardIds.txt", "r")
		self.kanjiId = ""
		self.rfidReader = MFRC522.MFRC522()

		for line in file:
			for word in line.split():
				if word == cardName:
					kanjiId = line.split()[1]

	def run(self):
		while counter > 0:
			status, tag_type = self.rfidReader.MFRC522_Request(self.rfidReader.PICC_REQIDL)

			if status == self.rfidReader.MI_OK:
				status, uid = self.rfidReader.MFRC522_Anticoll()

				if status == self.rfidReader.MI_OK:
					uid = ':'.join(['%X' % x for x in uid])
					if uid == self.kanjiId:
						kanjiFounded = 1
						break
					else:
						kanjiFounded = 2
						break

			time.sleep(.25)

class Timer(Thread):
	def __init__(self, num, screen, kanji):
		Thread.__init__(self)
		self.num = num
		self.screen = screen
		self.kanji = kanji
		self.surface = pygame.Surface((795, 411))

		self.fontDescription = pygame.font.SysFont("monospace", 25)

	def run(self):
		global counter
		global kanjiFounded

		kanjiFounded = 0

		GPIO.cleanup()
		cardReader = CardReader(self.kanji)
		cardReader.start()

		# countDown.join()

		while counter >= 0:
			if kanjiFounded != 0:
				break

			if counter == 5:
				sound = pygame.mixer.Sound("./Sounds/5_seconds_remaining.wav")
				sound.set_volume(0.8)
				pygame.mixer.Sound.play(sound)
			self.draw(self.kanji)
			time.sleep(1)
			counter -= 1


	def draw(self, kanji):
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])
		
		self.heart = pygame.image.load('./Images/heart.png')

		self.kanjiName = self.fontDescription.render(kanji, 1, (255,255,255))
		self.screen.blit(self.kanjiName, (360, 150))

		self.secondsName = self.fontDescription.render(str(counter) + "s", 1, (255,255,255))
		self.screen.blit(self.secondsName, (375, 300))

		global lifes
		if lifes == 1:
			self.screen.blit(self.heart, (725, 20))
		elif lifes == 2:
			self.screen.blit(self.heart, (725, 20))
			self.screen.blit(self.heart, (680, 20))
		elif lifes == 3:
			self.screen.blit(self.heart, (725, 20))
			self.screen.blit(self.heart, (680, 20))
			self.screen.blit(self.heart, (635, 20))
		
		pygame.display.flip()
		

class Portuguese:
	def __init__(self, screen, settingsMenu):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))
		self.settingsMenu = settingsMenu

		self.fontPortuguese = pygame.font.Font("./Fonts/Kengo.ttf", 62)
		self.fontDescription = pygame.font.SysFont("monospace", 25)

		global counter
		global kanjisNumber
		global fileName
		
		counter = self.settingsMenu.timeValue
		kanjisNumber = 5 * self.settingsMenu.radioCurrentSelected

		if kanjisNumber == 5:
			fileName = "./Files/portuguese_easy.txt"
		elif kanjisNumber == 10:
			fileName = "./Files/portuguese_normal.txt"
		elif kanjisNumber == 15:
			fileName = "./Files/portuguese_hard.txt"

	def start(self):
		self.portugueseName = self.fontPortuguese.render("Portuguese", 1, (255,69,0))
		self.descriptionName = self.fontDescription.render("The game will ask for the kanjis, in portuguese", 1, (255,255,255))
		sound = pygame.mixer.Sound("./Sounds/Portuguese_instructions.wav")
		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.portugueseName, (215, 100))
		self.screen.blit(self.descriptionName, (40, 200))
		pygame.display.flip()
		time.sleep(4)

		file = open(fileName, "r")
		kanji = ""
		for x in range(1,(randint(1, kanjisNumber)+1)):
			kanji = file.readline()
		file.close()

		self.play(kanji)

	def play(self, kanji):
		sound = pygame.mixer.Sound("./Sounds/" + kanji.rstrip() + ".wav")
		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

		countDown = Timer(1, self.screen, kanji.rstrip())
		countDown.start()

		countDown.join()

		global lifes
		global counter
		global kanjiFounded

		if kanjiFounded == 2:
			kanjiFounded = 0
			lifes -= 1
			if lifes > 0:
				self.play(kanji)

		if kanjiFounded == 1:
			self.gameOver = self.fontPortuguese.render("Excelent", 1, (255,0,0))
			counter = self.settingsMenu.timeValue
			time.sleep(2)

			file = open(fileName, "r")
			kanji = ""
			for x in range(1,(randint(1, kanjisNumber)+1)):
				kanji = file.readline()
			file.close()

			self.play(kanji)

		if counter <= 0:
			lifes -= 1
			if lifes > 0:
				counter = self.settingsMenu.timeValue
				self.play(kanji)

		if lifes <= 0:
			self.gameOver = self.fontPortuguese.render("Game Over", 1, (255,0,0))
			sound = pygame.mixer.Sound("./Sounds/Game_over.wav")
			sound.set_volume(0.8)
			pygame.mixer.Sound.play(sound)

			self.surface.fill((0,0,0))
			self.screen.blit(self.surface, [0,0])

			self.screen.blit(self.gameOver, (250, 175))
			pygame.display.flip()
			time.sleep(2)
			lifes = 3