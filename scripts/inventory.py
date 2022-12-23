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
        # Draw container
        container_layer_height = 0
        container_x, container_y = (20, 200)
        container_width, container_height = (200, 200)
        py_gui.create_inventory_container(container_x, container_y - 20,
                                          container_width, container_height, container_layer_height)
        # Draw items
        for item in py_gui.inventory_clone:
            py_gui.draw_inventory_item(item["name"], self.inventory)

    def close_inventory(self):
        py_gui.disable_panel(self.inventory)

    def add_item(self, item):
        if len(self.inventory) == 9:
            print("cant")
        else:
            self.inventory.append(item)
            py_gui.draw_inventory_item(item["name"], self.inventory)

    def initialize(self):
        if self.toggle_inventory:
            self.close_inventory()
        else:
            self.load_inventory()
