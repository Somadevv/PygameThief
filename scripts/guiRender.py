import pygame
import pygame_gui as py_gui


class GUI:

    def __init__(self, width, height):
        self.open = False
        self.manager = py_gui.UIManager((width, height))
        self.panels = []
        self.buttons = []

    def create_panel(self, x, y, width, height):
        py_gui.elements.UIPanel(relative_rect=pygame.Rect(
            (x, y), (width, height)), manager=self.manager)

    def create_multiple_panels(self, x, y, width, height, xOffset, yOffset, amount, perRow):
        for i in range(amount):
            xPos = x + (i % perRow) * xOffset
            yPos = y + yOffset * (i // perRow)
            self.panels.append(py_gui.elements.UIPanel(relative_rect=pygame.Rect(
                (xPos, yPos), (width, height)), manager=self.manager))
        return self.panels

    def create_multiple_buttons(self, amount):
        for i in range(amount):
            xPos = 5 + (i % 3) * 50
            yPos = 5 + 50 * (i // 3)
            self.buttons.append(py_gui.elements.UIButton(relative_rect=pygame.Rect((xPos, yPos), (50, 50)),
                                                         text='Say Hello',
                                                         manager=self.manager))

    def draw(self, screen):
        self.manager.draw_ui(screen)

    def update(self, dt):
        self.manager.update(dt)

    def initialize(self, dt, screen):
        self.update(dt)
        self.draw(screen)
