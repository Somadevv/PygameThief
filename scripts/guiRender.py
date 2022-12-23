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
        self.inventory_panel = []
        self.inventory_clone = []

    def create_multiple_buttons(self, x, y, width, height, xOffset, yOffset, amount, perRow, player_inventory):
        for i in range(amount):
            xPos = x + (i % perRow) * xOffset
            yPos = y + yOffset * (i // perRow)
            self.buttons.append(pygame.Rect((xPos, yPos), (width, height)))
            py_gui.elements.UIButton(relative_rect=self.buttons[i], text=player_inventory[i]["name"],

                                     manager=self.manager,

                                     object_id=ObjectID(class_id='@friendly_buttons',

                                                        object_id='#hello_button'))

    def draw_inventory_item(self, label, player_inventory):
        inventory_clone = player_inventory
        container_x, container_y = (20, 200)
        container_width = 200
        item_width, item_height = (
            (container_width / 3 / 2), 30)
        width, height = (50, 50)
        item_x, item_y = (container_x + item_width / 1.5, container_y)
        item_x_offset, item_y_offset = (item_width * 1.6, item_height * 1.6)
        button_count = len(inventory_clone) - 1
        per_row = 3
        width, height = (50, 50)
        x_pos = item_x + (button_count % per_row) * item_x_offset
        y_pos = item_y + item_y_offset * (button_count // per_row)
        self.buttons.append(py_gui.elements.UIButton(
            relative_rect=pygame.Rect(x_pos, y_pos, width, height), manager=self.manager, text=label))

    def create_inventory_container(self, x, y, width, height, layer_height):
        self.inventory_panel.append(py_gui.elements.UIPanel(relative_rect=pygame.Rect(
            (x, y), (width, height)), manager=self.manager, starting_layer_height=layer_height))

    def disable_panel(self, player_inventory):
        self.inventory_clone = player_inventory
        self.inventory_panel[0].hide()
        self.inventory_panel.clear()
        """
        ! LOOK INTO CLONING INVENTORY OR SOMETHING TO HIDE INV ITEMS ON CLOSE
        """

    def draw(self, screen):
        self.manager.draw_ui(screen)

    def update(self, dt):
        self.manager.update(dt)

    def initialize(self, dt, screen):
        self.update(dt)
        self.draw(screen)
