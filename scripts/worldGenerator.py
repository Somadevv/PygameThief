import pygame
import json
# Opening JSON file
test = open('Data/Levels/test_level.json')
data = json.load(test)


class worldGenerator():
    def __init__(self):
        self.rects = []
        self.playerStartPosition = 0, 0

        for i in data:
            self.rects.append(pygame.rect.Rect(
                i["xPos"], i["yPos"], i["width"], i["height"]))
