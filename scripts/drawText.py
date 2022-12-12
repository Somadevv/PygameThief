import pygame


class DrawText():
    def __init__(self, surface, text, size, color, x, y):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.surface = surface
        self.size = size
        font = pygame.font.Font("freesansbold.ttf", self.size)
        text = font.render(self.text, True, self.color)
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        surface.blit(text, textRect)
