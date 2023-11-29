import pygame
from scripts.world import World
from scripts.worldGenerator import WorldGenerator
from scripts.controller import Controller
from scripts.player import Player
from scripts.inventory import Inventory
from scripts.shophandler import Shop, Button

# Initialise pygame
pygame.init()

# Draw Screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CANVAS = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPS Params
CLOCK = pygame.time.Clock()
TARGET_FPS = 60
GAME_TICK = 240

# Run Game Bool
running = True


# Add Player
playerInstance = Player(GAME_WINDOW)

# Assign Variables to Imports
generateWorld = WorldGenerator()
worldGeneration = World
playerInventory = Inventory()
playerControls = Controller()
# Get Player Inventory on load
shopHandler = Shop()
shopHandlerButton = Button()


playerInventory.load()
shopHandlerButton.button_rects()


# Player Position on Load
playerInstance.position.x, playerInstance.position.y = 10, 50

# Game loop
while running:
    # Define Delta Time
    dt = CLOCK.tick(GAME_TICK) * .001 * TARGET_FPS

    # Control
    playerControls.GameControls(
        playerInstance, generateWorld.rects, playerInventory, shopHandler, shopHandlerButton)

    # Draw World
    worldGeneration.DrawWorld(CANVAS, generateWorld.rects)
    GAME_WINDOW.blit(CANVAS, (0, 0))

    # Update Player Position
    playerInstance.initialize(dt, generateWorld.rects)

    # Draw Background
    CANVAS.fill((255, 255, 255))

    # Draw Player
    playerInstance.draw(CANVAS)

    # Draw Player inventory bag
    playerInventory.initialize(GAME_WINDOW)
    shopHandler.initialize(GAME_WINDOW)

    pygame.display.update()
