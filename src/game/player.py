import random
import pygame

class Player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.velocity_y = 0
        self.is_jumping = False
        self.move_speed = 0.01
        self.jump_speed = 0.005

        # Procedurally generate color and shape
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
        self.shape = random.choice(['rect', 'circle'])
        self.size = random.randint(20, 40)

    def move(self, dx, dy, dt):
        self.x += dx * self.move_speed * dt
        self.y += dy * self.move_speed * dt

    def jump(self, dt):
        if not self.is_jumping:
            self.velocity_y = -self.jump_speed * dt
            self.is_jumping = True

    def input(self, keys, dt):
        dx, dy = 0, 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1
        self.move(dx, dy, dt)

    def update(self, dt):
        # Gravity always applies
        gravity = 0.0005  # Tiles per ms^2
        self.y += self.velocity_y * dt
        self.velocity_y += gravity * dt

        # Ground level (bottom of the world)
        ground_level = 9  # For a 10x10 world, last tile is y=9
        if self.y >= ground_level:
            self.y = ground_level
            self.velocity_y = 0
            self.is_jumping = False

    def draw(self, surface, tile_size=50):
        px = self.x * tile_size + tile_size // 2
        py = self.y * tile_size + tile_size // 2
        if self.shape == 'rect':
            rect = pygame.Rect(
                px - self.size // 2,
                py - self.size // 2,
                self.size,
                self.size
            )
            pygame.draw.rect(surface, self.color, rect)
        else:
            pygame.draw.circle(surface, self.color, (px, py), self.size // 2)