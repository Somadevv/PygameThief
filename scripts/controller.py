import pygame
import sys


class Controller:

    def GameControls(self, Player, worldRects, Inventory, ShopHandler, ShopHandlerButton):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                for i, item in enumerate(ShopHandlerButton.buttons):
                    if event.button == 1 and item.collidepoint(mouse_pos) and ShopHandler.toggleOpen:
                        print(item, "Hello")
            if event.type == pygame.KEYDOWN:
                # Movement
                if event.key == pygame.K_a:
                    Player.LEFT_KEY = True
                elif event.key == pygame.K_d:
                    Player.RIGHT_KEY = True
                elif event.key == pygame.K_SPACE:
                    Player.jump()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                # Inventory
                if event.key == pygame.K_1:
                    Inventory.add_item(1)
                    Inventory.delete_item(2)
                if event.key == pygame.K_TAB:
                    print("opened")
                    Inventory.toggleInventory = not Inventory.toggleInventory
                if event.key == pygame.K_g:
                    ShopHandler.toggleOpen = not ShopHandler.toggleOpen
                if event.key == pygame.K_a:
                    Player.LEFT_KEY = False
                elif event.key == pygame.K_d:
                    Player.RIGHT_KEY = False
                elif event.key == pygame.K_SPACE:
                    Player.velocity.y *= .25
                    Player.is_jumping = False
                    Player.on_right_wall = False
                    Player.on_left_wall = False
