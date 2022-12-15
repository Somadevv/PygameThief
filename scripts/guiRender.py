import pygame
import pygame_gui as py_gui


class GUI:

    def __init__(self, width, height):
        self.open = False
        self.manager = py_gui.UIManager((width, height))

    def create_panel(self, x, y, width, height):
        py_gui.elements.UIPanel(relative_rect=pygame.Rect(
            (x, y), (width, height)), manager=self.manager)

    def draw(self, screen):
        self.manager.draw_ui(screen)

    def update(self, dt):
        self.manager.update(dt)

    def initialize(self, dt, screen):
        self.update(dt)
        self.draw(screen)
