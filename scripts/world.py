import pygame

# def __init__(self):
#     self.rects = [pygame.rect.Rect(
#         0, 415, 750, 30), pygame.rect.Rect(600, 375, 50, 50)]
#     self.playerStartPosition = 375, 250


class World:

    def draw_world(SURFACE, RECT):
        for i in RECT:
            pygame.draw.rect(SURFACE, (217, 217, 217), i)
