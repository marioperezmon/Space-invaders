import pygame

black = (0, 0, 0)

class nave():
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height), 2)


