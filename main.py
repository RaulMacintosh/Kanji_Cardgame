import pygame

pygame.init()
pygame.display.set_caption('Kanji - Cardgame')
screen = pygame.display.set_mode((795, 411))
done = False

fontKanji = pygame.font.Font("./Fonts/Kengo.ttf", 62)
fontCardgame = pygame.font.Font("./Fonts/Kengo.ttf", 32)

#font = pygame.font.SysFont("monospace", 42)

kanji = fontKanji.render("Kanji", 1, (255,255,255))
cardgame = fontCardgame.render("Cardgame", 1, (255,255,255))
screen.blit(kanji, (325, 50))
screen.blit(cardgame, (315, 125))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()