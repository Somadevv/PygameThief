import pygame
from scripts.draw_text import DrawText
from scripts.load_file import load_file


class Inventory:
    def __init__(self, screen):
        self.inventory = [{"name": "First", "price": 10, "active": False}, {"name": "Second", "price": 10, "active": True}, {
            "name": "Third", "price": 10, "active": True}, {"name": "Fourth", "price": 10, "active": False}, {"name": "Five", "price": 10, "active": True}]
        self.hotbar_inventory = []
        self.toggle_inventory = False
        self.screen = screen

        # Find all active items in inventory & append to hotbar inventory
        for i in self.inventory:
            if i["active"] == True:
                self.hotbar_inventory.append(i)

    def set_active_item():
        pass

    def draw_hotbar(self, gui):
        containerWidth = 150
        containerHeight = 50
        containerXpos = (self.screen.get_width() / 2) - (containerWidth / 2)
        containerYpos = self.screen.get_height() - 60

        for i, item in enumerate(self.hotbar_inventory):
            xPos = containerXpos + 5 + (i % 3) * 50
            yPos = containerYpos + 5
            width = containerWidth / 3 - 10
            height = containerHeight - 10
            hotbar_item = gui.create_panel(xPos, yPos, width, height)

    def draw_bag_icon(self):
        bagWidth = 65
        bagHeight = 65
        bagXpos = 20
        bagYpos = 350
        bagIcon = pygame.image.load(
            "assets/Images/bag.png").convert_alpha()
        textSize = 20
        image = pygame.transform.scale(
            bagIcon, (bagWidth, bagHeight))
        self.screen.blit(image, (bagXpos, bagYpos))
        DrawText(self.screen, "Tab", textSize, (255, 255, 255),
                 50, 385)

    def draw_inventory(self):
        self.containerX = 15
        self.containerY = 150
        #  PARENT container
        container = pygame.Rect(
            self.containerX, self.containerY, 200, 200)
        #  CHILD container
        innerContainer = pygame.Rect(
            self.containerX + 10, self.containerY + 10, 180, 180)
        #  CLOSE
        # self.closeContainer = pygame.Rect(
        #     containerX, containerY, 0, 0)
        pygame.draw.rect(self.screen, (0, 0, 0), container)
        pygame.draw.rect(self.screen, (140, 60, 140), innerContainer)

        if self.inventory:
            origin = pygame.Rect(
                self.containerX, self.containerY + 20, 20, 20)
            for i, item in enumerate(self.inventory):
                # Grid column spacing
                y_offset = 60
                xPos = self.containerX + 20 + (i % 3) * 57
                yPos = origin.y + y_offset * (i // 3)
                width = 35
                height = 35
                textSize = 13
                textColor = (255, 255, 255)

                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                    xPos, yPos, width, height), 1)
                DrawText(self.screen, self.inventory[i]["name"], textSize, textColor,
                         xPos + width / 2, yPos + height / 2)

    def add_to_inventory(self):
        pass

    def remove_from_inventory(self):
        pass

    def draw(self, gui):
        self.draw_hotbar(gui)
        self.draw_bag_icon()

        if self.toggle_inventory:
            self.draw_inventory()
