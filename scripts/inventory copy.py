import pygame
from scripts.draw_text import DrawText
from scripts.load_file import load_file


class Inventory:

    def __init__(self):
        self.INVENTORY = {}
        self.toggleInventory = False
        self.gameItems = load_file('data/items.json')

    def load(self):
        print("Loaded player inventory...")

        self.containerX = 15
        self.containerY = 150
        #  PARENT container
        self.container = pygame.Rect(
            self.containerX, self.containerY, 200, 200)
        #  CHILD container
        self.innerContainer = pygame.Rect(
            self.containerX + 10, self.containerY + 10, 180, 180)
        #  CLOSE
        self.closeContainer = pygame.Rect(
            self.containerX, self.containerY, 0, 0)

    def update(self, surface):
        origin = pygame.Rect(
            self.containerX, self.containerY + 20, 20, 20)
        if self.INVENTORY:
            for i, item in enumerate(self.INVENTORY):
                # Grid column spacing
                y_offset = 60
                xPos = self.containerX + 20 + (i % 3) * 57
                yPos = origin.y + y_offset * (i // 3)
                width = 35
                height = 35
                textSize = 13
                textColor = (255, 255, 255)

                pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(
                    xPos, yPos, width, height), 1)
                DrawText(surface, self.INVENTORY[item]["name"], textSize, textColor,
                         xPos + width / 2, yPos + height / 2)

    def open(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.container)
        pygame.draw.rect(surface, (140, 60, 140), self.innerContainer)
        self.update(surface)

    def close(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.closeContainer)

    def add_item(self, itemId):
        itemId = str(itemId)
        if itemId in self.gameItems:
            if itemId not in self.INVENTORY:
                self.INVENTORY[itemId] = {
                    "name": self.gameItems[itemId]["name"], "price": self.gameItems[itemId]["price"]}
                print("Added", self.INVENTORY)
            else:
                print("Item already in inventory")
        else:
            print("No item with that ID exists", itemId)

    def delete_item(self, itemId):
        itemId = str(itemId)

        if itemId not in self.INVENTORY:
            print("No item found with that ID")
        else:
            self.INVENTORY.pop(itemId)

    def draw_bag_to_window(self, surface):
        bagWidth = 65
        bagHeight = 65
        bagXpos = 20
        bagYpos = 350
        bagIcon = pygame.image.load(
            "assets/Images/bag.png").convert_alpha()
        textSize = 20
        image = pygame.transform.scale(
            bagIcon, (bagWidth, bagHeight))
        surface.blit(image, (bagXpos, bagYpos))
        DrawText(surface, "Tab", textSize, (255, 255, 255),
                 50, 385)

    def initialize(self, surface):
        self.draw_bag_to_window(surface)
        # print(self.toggleInventory)

        if self.toggleInventory:
            # print("changed", self.toggleInventory)
            self.open(surface)
        else:
            self.close(surface)
