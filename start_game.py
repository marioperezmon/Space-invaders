import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 100))
    pygame.display.update()

pygame.quit()