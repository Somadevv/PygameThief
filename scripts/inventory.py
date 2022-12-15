import pygame
from scripts.draw_text import DrawText
from scripts.load_file import load_file


class Inventory:
    def __init__(self, screen):
        self.hotbar_inventory = []
        self.toggle_inventory = False
        self.screen = screen

    def set_active_item():
        pass

    def draw_hotbar(self, gui):
        pass

    def draw_bag_icon(self):
        pass

    def draw_inventory(self, gui):
        # Pixel perfect grid layout
        width, height = (30, 30)
        x, y = (50, 50)
        amount, perRow = (9, 3)
        gui.create_multiple_panels(
            x, y, width, height,  width * 2 - (width / 2), height * 2 - (height / 2), amount, perRow)

    def close_inventory(self, gui):
        pass

    def remove_from_inventory(self):
        pass

    def draw(self, gui):
        self.draw_hotbar(gui)
        # self.draw_inventory(gui)
        self.draw_bag_icon()

        if self.toggle_inventory:
            self.draw_inventory(gui)
        else:
            self.close_inventory(gui)
