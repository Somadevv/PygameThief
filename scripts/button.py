from typing import List

import pygame


class Button:
    def __init__(self, rect: pygame.Rect) -> None:
        # self.base_rect is going to be the one that never gets modified
        self.base_rect = rect
        # self.rect is going to be the one that is active
        self.rect = rect

    def collidepoint(self, pos: pygame.Vector2) -> bool:
        return self.rect.collidepoint(pos)

    def scale(self, scale_factor=1.2) -> None:
        width = self.base_rect.width * scale_factor
        height = self.base_rect.height * scale_factor

        c_pos = self.base_rect.center

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = c_pos
