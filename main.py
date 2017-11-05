# -*- coding: utf-8 -*-
import pygame

pygame.init()
pygame.display.set_caption('Kanji - Cardgame')
screen = pygame.display.set_mode((795, 411))
done = False

fontKanji = pygame.font.Font("./Fonts/Kengo.ttf", 62)
fontCardgame = pygame.font.Font("./Fonts/Kengo.ttf", 32)
fontItens = pygame.font.SysFont("monospace", 20)

kanjiName = fontKanji.render("Kanji", 1, (255,69,0))
cardgameName = fontCardgame.render("Cardgame", 1, (255,215,0))
jogarName = fontItens.render("Jogar", 1, (0,100,0))
instrucoesName = fontItens.render("Instruções", 1, (255,255,255))
configuracoesName = fontItens.render("Configurações", 1, (255,255,255))
sobreName = fontItens.render("Sobre", 1, (255,255,255))
sairName = fontItens.render("Sair", 1, (255,255,255))

screen.blit(kanjiName, (325, 50))
screen.blit(cardgameName, (315, 125))
screen.blit(jogarName, (10, 300))
screen.blit(instrucoesName, (10, 310))
screen.blit(configuracoesName, (10, 320))
screen.blit(sobreName, (10, 330))
screen.blit(sairName, (10, 340))

kanjiKanji = pygame.image.load('./Kanjis/kanji.png')
screen.blit(kanjiKanji, (450, 225))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()