import pygame
import Helpers.drawText

DrawText = Helpers.drawText.DrawText


class Inventory():

    def __init__(self):
        self.BAG_COLOR = (125, 22, 55)
        self.BAG_HEIGHT = 65
        self.BAG_WIDTH = 65
        self.BAG_XPOS = 20
        self.BAG_YPOS = 350
        self.INVENTORY = [{"id": 1, "name": "cock"}, {
            "id": 2, "name": "cock"}, {"id": 3, "name": "cock"}, {"id": 4, "name": "cock"}, {"id": 5, "name": "cock"}, {"id": 6, "name": "cock"}]

    def GetInventory(self):
        print("Loading Inventory...")

        self.containerX = 100
        self.containerY = 200
        # Inventory PARENT container
        self.container = pygame.Rect(
            self.containerX, self.containerY, 200, 200)
        # Inventory CHILD container
        self.innerContainer = pygame.Rect(
            self.containerX + 10, self.containerY + 10, 180, 180)
        # Inventory CLOSE
        self.close = pygame.Rect(self.containerX, self.containerY, 0, 0)

    def DrawInventoryBagToWindow(self, surface):
        BAG_ICON = pygame.image.load("Assets/Images/Icons/bag.png").convert()
        TEXT_SIZE = 20
        image = pygame.transform.scale(
            BAG_ICON, (self.BAG_WIDTH, self.BAG_HEIGHT))
        surface.blit(image, (self.BAG_XPOS, self.BAG_YPOS))
        DrawText(surface, "Tab", TEXT_SIZE, (255, 255, 255),
                 50, 385)

    def DrawInventory(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.container)
        pygame.draw.rect(surface, (210, 20, 150), self.innerContainer)
        origin = pygame.Rect(
            150, self.containerY + 20, 20, 20)
#        [{"id": 0, "name": "cock"}, {
# "id": 1, "name": "cock"}, {"id": 2, "name": "cock"}]

        for i in self.INVENTORY:

            pygame.draw.rect(surface, (140, 20, 50),
                             pygame.Rect(
                origin.x * i["id"] / 4, origin.y, 20, 20))

    def CloseInventory(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.close)

    def AddItem(self, item):
        if item not in self.INVENTORY:
            self.INVENTORY.append(item)
            print("Item Added: ", item)

    def DeleteItem(self, item):
        if item in self.INVENTORY:
            itemFound = self.INVENTORY.index(item)
            self.INVENTORY.pop(itemFound)
            print("Item Removed: ", item)

    def PickUpItem(self, item):
        if item in self.INVENTORY:
            print("Duplicate item found")
