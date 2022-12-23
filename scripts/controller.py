import pygame
import sys
from scripts.load_file import load_file
import pygame_gui as py_GUI

shopItems = load_file('data/items.json')


class Controller:

    def game_controls(self, Player, worldRects, player_inventory, ShopHandler, ShopHandlerButton, py_gui):
        # print(py_gui.panels[1])
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        for event in pygame.event.get():

            if event.type == py_GUI.UI_BUTTON_PRESSED:
                for i, item in enumerate(py_gui.buttons):
                    if event.ui_element == py_gui.buttons[i]:
                        # py_GUI.core.UIElement.hide(py_gui.button_rects[i])
                        # py_GUI.core.UIElement.disable(py_gui.buttons[i])

                        print(player_inventory.inventory[i]["name"])
            py_gui.manager.process_events(event)
            if event.type == pygame.KEYDOWN:
                # Movement

                if event.key == pygame.K_a:
                    Player.LEFT_KEY = True
                elif event.key == pygame.K_d:
                    Player.RIGHT_KEY = True
                elif event.key == pygame.K_s:
                    Player.DOWN_KEY = True
                elif event.key == pygame.K_SPACE:
                    Player.jump()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB:
                    player_inventory.initialize()
                    player_inventory.toggle_inventory = not player_inventory.toggle_inventory
                if event.key == pygame.K_1:
                    player_inventory.add_item({"name": "yo"})
                    # print(player_inventory.inventory)
                if event.key == pygame.K_g:
                    ShopHandler.toggleOpen = not ShopHandler.toggleOpen
                if event.key == pygame.K_a:
                    Player.LEFT_KEY = False
                elif event.key == pygame.K_d:
                    Player.RIGHT_KEY = False
                elif event.key == pygame.K_s:
                    for i in worldRects:
                        if i.bottom <= Player.rect_small.top <= i.bottom + 40 and Player.rect_small.right > i.left and Player.rect_small.left < i.right:
                            Player.DOWN_KEY = True
                        else:
                            Player.DOWN_KEY = False
                elif event.key == pygame.K_SPACE:
                    Player.velocity.y *= .25
                    Player.is_jumping = False
                    Player.on_right_wall = False
                    Player.on_left_wall = False
