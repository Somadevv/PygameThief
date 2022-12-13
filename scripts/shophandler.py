from typing import List
import pygame
from scripts.loadFile import load_file
from scripts.inventory import Inventory

shopItems = load_file('data/items.json')
playerInventory = Inventory()


class Button:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.buttons: List[Button()] = []
        self.base_pos = pygame.Vector2(750 / 1 - 230, 150)
        self.width = 35
        self.height = 35
        self.x_offset = self.width * 1.75
        self.y_offset = self.height * 1.75

    def button_rects(self):

        for i, item in enumerate(shopItems):
            offset_vector = pygame.Vector2(
                self.x_offset*(i % 3), self.y_offset*(i//3))
            pos = self.base_pos + offset_vector
            self.buttons.append(pygame.Rect(
                pos.x, pos.y, self.width, self.height))

    def render_buttons(self, screen):
        for i in self.buttons:
            pygame.draw.rect(screen, "red", i)


class Shop:
    # Buy, Sell, Standard/Special Items (tabs?)
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.button = Button()
        self.toggleOpen = False
        self.pressed = False
        self.isCollided = False

    def open(self, screen):
        self.containerWidth = screen.get_width() / 3
        self.containerHeight = screen.get_height() / 2.1
        # self.containerX = self.containerWidth - self.containerWidth / 2
        self.containerX = screen.get_width() - self.containerWidth - 30
        self.containerY = self.containerHeight - self.containerHeight / 2
        self.containerColor = (0, 0, 0)

        pygame.draw.rect(screen, self.containerColor, pygame.Rect(self.containerX, self.containerY,
                                                                  self.containerWidth, self.containerHeight))

    def close_inv(self):
        self.toggleOpen = False

    def shop_buy(self, price, itemId):
        print(itemId)
        # self.player.remove_gold(price)
        # self.playerInventory.add_item(itemId)

    def shop_sell(self, itemId):
        pass

    def initialize(self, screen):

        if self.toggleOpen:
            self.open(screen)
            self.button.render_buttons(screen)
        else:
            self.close_inv()
