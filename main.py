# -*- coding: utf-8 -*-
import pygame

pygame.init()
pygame.display.set_caption('Kanji - Cardgame')
screen = pygame.display.set_mode((795, 411))
done = False

fontKanji = pygame.font.Font("./Fonts/Kengo.ttf", 62)
fontCardgame = pygame.font.Font("./Fonts/Kengo.ttf", 32)
fontItens = pygame.font.Font("./Fonts/Kengo.ttf", 20)

kanjiName = fontKanji.render("Kanji", 1, (255,69,0))
cardgameName = fontCardgame.render("Cardgame", 1, (255,215,0))
jogarName = fontItens.render("Play", 1, (0,100,0))
instrucoesName = fontItens.render("Tutorial", 1, (255,255,255))
configuracoesName = fontItens.render("Settings", 1, (255,255,255))
sobreName = fontItens.render("About", 1, (255,255,255))
sairName = fontItens.render("Exit", 1, (255,255,255))

screen.blit(kanjiName, (325, 50))
screen.blit(cardgameName, (315, 125))
screen.blit(jogarName, (20, 250))
screen.blit(instrucoesName, (20, 270))
screen.blit(configuracoesName, (20, 290))
screen.blit(sobreName, (20, 310))
screen.blit(sairName, (20, 330))

kanjiKanji = pygame.image.load('./Kanjis/kanji.png')
screen.blit(kanjiKanji, (450, 225))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()