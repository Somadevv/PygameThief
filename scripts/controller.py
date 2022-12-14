import pygame
import sys
from scripts.load_file import load_file

shopItems = load_file('data/items.json')


class Controller:

    def GameControls(self, Player, worldRects, Inventory, ShopHandler, ShopHandlerButton):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                for i, item in enumerate(ShopHandlerButton.buttons):
                    if event.button == 1 and item.collidepoint(mouse_pos) and ShopHandler.toggleOpen:
                        i = i + 1
                        if Player.gold < shopItems[str(i)]["price"]:
                            print("You can't afford this")
                        else:
                            Inventory.add_item(i)
                            Player.remove_gold(shopItems[str(i)]["price"])

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
                # Inventory
                if event.key == pygame.K_1:
                    print("1 pressed")
                if event.key == pygame.K_TAB:
                    Inventory.toggle_inventory = not Inventory.toggle_inventory
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
