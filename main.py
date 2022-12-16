import pygame
from scripts.world import World
from scripts.world_generator import WorldGenerator
from scripts.controller import Controller
from scripts.player import Player
from scripts.inventory import Inventory
from scripts.shop_handler import Shop, Button
from scripts.guiRender import GUI

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 750, 500
CANVAS = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# FPS Params
CLOCK = pygame.time.Clock()
TARGET_FPS = 60
GAME_TICK = 120

# Run Game Bool
running = True


# Add Player
playerInstance = Player(GAME_WINDOW)

# Assign Variables to Imports
generateWorld = WorldGenerator()
worldGeneration = World
py_gui = GUI(SCREEN_WIDTH, SCREEN_HEIGHT)
player_inventory = Inventory(GAME_WINDOW)
playerControls = Controller()
# Get Player Inventory on load
shopHandler = Shop(GAME_WINDOW)
shopHandlerButton = Button(GAME_WINDOW)


# playerInventory.load()
shopHandlerButton.button_rects()

# Player Position on Load
playerInstance.position.x, playerInstance.position.y = 0, 0


# Game loop
while running:
    # Draw World

    worldGeneration.draw_world(CANVAS, generateWorld.rects)
    GAME_WINDOW.blit(CANVAS, (0, 0))

    # Define Delta Time
    dt = CLOCK.tick(GAME_TICK) * .001 * TARGET_FPS

    # Control
    playerControls.game_controls(
        playerInstance, generateWorld.rects, player_inventory, shopHandler, shopHandlerButton, py_gui)

    # Update Player Position
    playerInstance.initialize(dt, generateWorld.rects)

    # Draw Background
    CANVAS.fill((255, 255, 255))
    # Draw Player
    playerInstance.draw(CANVAS)

    # Display fps in cli
    # print("FPS", int(CLOCK.get_fps()))

    # Draw Player inventory bag

    shopHandler.initialize()

    py_gui.initialize(dt, GAME_WINDOW)

    pygame.display.update()
