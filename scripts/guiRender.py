import pygame
import pygame_gui as py_gui
from pygame_gui.core import ObjectID


class GUI:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, width, height):
        self.open = False
        self.manager = py_gui.UIManager(
            (width, height), 'assets/Theme/theme.json')
        self.panels = []
        self.buttons = []

    def create_panel(self, x, y, width, height, layer_height):
        self.test = py_gui.elements.UIPanel(relative_rect=pygame.Rect(
            (x, y), (width, height)), manager=self.manager, starting_layer_height=layer_height)

    def create_multiple_buttons(self, x, y, width, height, xOffset, yOffset, amount, perRow, player_inventory):
        for i in range(amount):
            xPos = x + (i % perRow) * xOffset
            yPos = y + yOffset * (i // perRow)
            self.buttons.append(py_gui.elements.UIButton(relative_rect=pygame.Rect((xPos, yPos), (width, height)),
                                                         text=player_inventory[i]["name"],

                                                         manager=self.manager,

                                                         object_id=ObjectID(class_id='@friendly_buttons',

                                                                            object_id='#hello_button')))

    def create_multiple_panels(self, x, y, width, height, xOffset, yOffset, amount, perRow):
        for i in range(amount):
            xPos = x + (i % perRow) * xOffset
            yPos = y + yOffset * (i // perRow)
            self.panels.append(py_gui.elements.UIPanel(relative_rect=pygame.Rect(
                (xPos, yPos), (width, height)), manager=self.manager))

    def disable_button(self, button_id):
        self.buttons.pop(button_id)

    def draw(self, screen):
        self.manager.draw_ui(screen)

    def update(self, dt):
        self.manager.update(dt)

    def initialize(self, dt, screen):
        self.update(dt)
        self.draw(screen)
