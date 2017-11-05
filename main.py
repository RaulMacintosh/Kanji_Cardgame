import pygame

pygame.init()
pygame.display.set_caption('Kanji - Cardgame')
screen = pygame.display.set_mode((795, 411))
done = False

font = pygame.font.SysFont("monospace", 36)

gameName = font.render("Kanji Cardgame", 1, (255,255,255))
screen.blit(gameName, (300, 100))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()