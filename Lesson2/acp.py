import pygame

# Initialize Pygame
pygame.init()

# Create the screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Sprite Adventure")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 200, 0)

# Rectangle sprite
x = 275
y = 175
width = 50
height = 50

# Movement speed
speed = 5

# Starting color
sprite_color = RED

# Game loop
running = True

while running:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keys are pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed

    # Keep the rectangle inside the screen
    if x < 0:
        x = 0

    if x + width > WIDTH:
        x = WIDTH - width

    if y < 0:
        y = 0

    if y + height > HEIGHT:
        y = HEIGHT - height

    # Change color when touching an edge
    if x == 0:
        sprite_color = GREEN

    elif x + width == WIDTH:
        sprite_color = BLUE

    elif y == 0:
        sprite_color = YELLOW

    elif y + height == HEIGHT:
        sprite_color = RED

    # Clear the screen
    screen.fill(WHITE)

    # Draw the solid rectangle
    pygame.draw.rect(screen, sprite_color, (x, y, width, height))

    # Draw an outline around the rectangle
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 3)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()