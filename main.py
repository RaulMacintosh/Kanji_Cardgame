import pygame

pygame.init()
pygame.display.set_caption('Kanji - Cardgame')
screen = pygame.display.set_mode((795, 411))
done = False

fontKanji = pygame.font.Font("./Fonts/Kengo.ttf", 62)
fontCardgame = pygame.font.Font("./Fonts/Kengo.ttf", 32)

kanjiName = fontKanji.render("Kanji", 1, (255,255,255))
cardgameName = fontCardgame.render("Cardgame", 1, (255,255,255))
screen.blit(kanjiName, (325, 50))
screen.blit(cardgameName, (315, 125))

kanjiKanji = pygame.image.load('/Kanjis/kanji.png')
screen.blit(kanjiKanji, (400, 200))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()