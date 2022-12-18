import pygame
from scripts.draw_text import DrawText
from scripts.load_file import load_file
from scripts.guiRender import GUI

import pygame.freetype

pygame.freetype.init()

py_gui = GUI(750, 500)


class Inventory:
    def __init__(self, screen):
        self.inventory = [{"name": "test"}]
        self.toggle_inventory = False
        self.screen = screen

    def load_inventory(self):
        # Invnentory parent container
        container_layer_height = 0
        container_x, container_y = (250, 200)
        container_width, container_height = (250, 200)
        # Invnentory child items
        item_amount, items_per_row = (len(self.inventory), 3)
        item_width, item_height = (
            (container_width / items_per_row / 2), 30)
        item_x, item_y = (container_x + item_width / 1.5, container_y)
        item_x_offset, item_y_offset = (item_width * 1.6, item_height * 1.6)
        py_gui.create_panel(container_x, container_y - 20,
                            container_width, container_height, container_layer_height)
        py_gui.create_multiple_buttons(
            item_x, item_y, item_width * 2 - (item_width / 2), item_height * 2 - (item_height / 2), item_x_offset, item_y_offset,  item_amount, items_per_row, self.inventory)
