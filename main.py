import pygame

pygame.init()
pygame.display.set_caption('Kanji - Cardgame')
screen = pygame.display.set_mode((795, 411))
done = False

fontKanji = pygame.font.Font("./Fonts/Kengo.ttf", 52)
fontCardgame = pygame.font.Font("./Fonts/Kengo.ttf", 42)

#font = pygame.font.SysFont("monospace", 42)

kanji = fontKanji.render("Kanji", 1, (255,255,255))
cardgame = fontCardgame.render("Cardgame", 1, (255,255,255))
screen.blit(kanji, (300, 100))
screen.blit(cardgame, (250, 200))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()