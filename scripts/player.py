import pygame


class Player():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 40)
        self.rect_small = pygame.Rect(0, 0, 20, 20)
        self.LEFT_KEY, self.RIGHT_KEY, self.DOWN_KEY = False, False, False
        self.is_jumping, self.on_ground = False, False
        self.on_right_wall, self.on_left_wall = False, False
        self.gravity, self.friction = .5, -.1
        self.position, self.velocity = pygame.math.Vector2(
            0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)

    def draw(self, display):
        if self.DOWN_KEY:
            pygame.draw.rect(display, (255, 0, 0), self.rect_small)
        else:
            pygame.draw.rect(display, (255, 0, 0), self.rect)

    def update(self, dt, worldRects):
        self.horizontal_movement(dt, worldRects)
        self.vertical_movement(dt, worldRects)

    def horizontal_movement(self, dt, worldRects):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .5
        elif self.RIGHT_KEY:
            self.acceleration.x += .5
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(5)
        self.position.x += self.velocity.x * dt + \
            (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x
        self.rect_small.x = self.position.x

        if self.DOWN_KEY:
            for i in worldRects:
                for i in worldRects:
                    # Right Collision Crouched
                    if i.left - 2 <= self.rect_small.right <= i.left and self.rect_small.bottom > i.top and self.rect_small.top < i.bottom:
                        self.velocity.x = 0
                        self.on_right_wall = True
                        self.RIGHT_KEY = False
                        self.is_jumping = False
                        self.on_ground = False

                    # Left Collision Crouched
                    if i.right <= self.rect_small.left <= i.right + 2 and self.rect_small.bottom > i.top and self.rect_small.top < i.bottom:
                        self.velocity.x = 0
                        self.on_left_wall = True
                        self.LEFT_KEY = False
                        self.is_jumping = False
                        self.on_ground = False
        else:
            for i in worldRects:
                # Right Collision
                if i.left - 2 <= self.rect.right <= i.left and self.rect.bottom > i.top and self.rect.top < i.bottom:
                    self.velocity.x = 0
                    self.on_right_wall = True
                    self.RIGHT_KEY = False
                    self.is_jumping = False
                    self.on_ground = False

                # Left Collision
                if i.right <= self.rect.left <= i.right + 2 and self.rect.bottom > i.top and self.rect.top < i.bottom:
                    self.velocity.x = 0
                    self.on_left_wall = True
                    self.LEFT_KEY = False
                    self.is_jumping = False
                    self.on_ground = False

    def vertical_movement(self, dt, worldRects):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 8:
            self.velocity.y = 8
        self.position.y += self.velocity.y * dt + \
            (self.acceleration.y * .9) * (dt * dt)

        if self.DOWN_KEY:
            for i in worldRects:
                # Bottom Collision Crouched
                if i.top <= self.rect_small.bottom <= i.top + 5 and self.rect_small.right > i.left and self.rect_small.left < i.right:
                    if self.position.y >= i.top:
                        self.on_ground = True
                        self.is_jumping = False
                        self.on_right_wall = False
                        self.on_left_wall = False
                        self.velocity.y = 0
                        self.position.y = i.top

                # Top Collision Crouched
                if i.bottom - 5 <= self.rect_small.top <= i.bottom and self.rect_small.right > i.left and self.rect_small.left < i.right:
                    self.is_jumping = False
                    self.velocity.y += 15
        else:
            for i in worldRects:
                # Bottom Collision
                if i.top <= self.rect.bottom <= i.top + 5 and self.rect.right > i.left and self.rect.left < i.right:
                    if self.position.y >= i.top:
                        self.on_ground = True
                        self.is_jumping = False
                        self.on_right_wall = False
                        self.on_left_wall = False
                        self.velocity.y = 0
                        self.position.y = i.top

                # Top Collision
                if i.bottom - 5 <= self.rect.top <= i.bottom and self.rect.right > i.left and self.rect.left < i.right:
                    self.is_jumping = False
                    self.velocity.y += 15
                else:
                    self.DOWN_KEY = False

        self.rect.bottom = self.position.y
        self.rect_small.bottom = self.position.y

    def limit_velocity(self, max_vel):
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01:
            self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 10
            self.on_ground = False
        if self.on_right_wall:
            self.is_jumping = True
            self.velocity.y -= 14
            self.velocity.x -= 10
            self.on_ground = False
        if self.on_left_wall:
            self.is_jumping = True
            self.velocity.y -= 14
            self.velocity.x += 10
            self.on_ground = False

    def initialize(self, dt, worldRects):
        self.update(dt, worldRects)
