import pygame
from game.world import World
from game.player import Player
from game.procedural import generate_level

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Procedurally Generated Game")

# Initialize game variables
clock = pygame.time.Clock()
running = True

# Create game world and player
world = World(10, 10)
player = Player(0, 0)

# Main game loop
while running:
    dt = clock.tick(60)  # milliseconds since last frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump(dt)

    # Update game state
    keys = pygame.key.get_pressed()
    player.input(keys, dt)
    player.update(dt)

    # Fill the screen with a color
    screen.fill((0, 0, 0))

    # Draw the world and player
    world.render_world(screen)
    player.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()