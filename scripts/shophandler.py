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
        # self.base_rect is going to be the one that never gets modified
        # self.base_rect = rect
        # self.rect is going to be the one that is active
        # self.rect = rect
        self.base_pos = pygame.Vector2(750 / 3, 150)
        self.width = 30
        self.height = 30
        self.y_offset = 50
        self.x_offset = 50

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

        # self.button_collision()

    # def button_collision(self) -> bool:
    #     mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    #     for i, item in enumerate(self.buttons):
    #         if item.collidepoint(mouse_pos):
    #             item.width = 40
    #             item.height = 40
    #             exit
    #             # self.player.remove_gold(shopItems[str(i + 1)]["price"])
    #         else:
    #             item.w = 30
    #             item.h = 30

    # def button_scale(self, scale_factor=1.2) -> None:
    #     width = self.base_rect.width * scale_factor
    #     height = self.base_rect.height * scale_factor

    #     c_pos = self.base_rect.center

    #     self.rect = pygame.Rect(0, 0, width, height)
    #     self.rect.center = c_pos

    # def button_controls(self, screen):
    #     mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    #     for i, button in enumerate(self.buttons):
    #         if button.collidepoint(mouse_pos):
    #             button.scale(1.2)
    #             self.player.remove_gold(shopItems[str(i + 1)]["price"])
    #         else:
    #             button.scale(1)

    #         pygame.draw.rect(screen, "white", button.rect)


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
        # self.playerInventory = Player.inventory.Inventory(screen)
        # self.player = Player.player.Player(screen)
        self.pressed = False
        self.isCollided = False

    def open(self, screen):
        self.containerWidth = screen.get_width() / 2
        self.containerHeight = screen.get_height() / 2
        self.containerX = self.containerWidth - self.containerWidth / 2
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
