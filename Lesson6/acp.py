
import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame and sound mixer
pygame.init()
pygame.mixer.init()

# Create the screen
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Background image
background = pygame.image.load(
    "background.png"
).convert()
background = pygame.transform.scale(
    background, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Sound effects
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)  # Repeat continuously

laser_sound = pygame.mixer.Sound("laser.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")

# Player
playerImg = pygame.image.load("player.png")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(
        random.randint(0, SCREEN_WIDTH - 64)
    )
    enemyY.append(
        random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
    )
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)
game_over = False


def show_score(x, y):
    score = font.render(
        "Score : " + str(score_value),
        True, (255, 255, 255)
    )
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render(
        "GAME OVER", True, (255, 255, 255)
    )
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        (enemyX - bulletX) ** 2
        + (enemyY - bulletY) ** 2
    )
    return distance < COLLISION_DISTANCE


# Game loop
running = True

while running:

    # Draw background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if not game_over:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    playerX_change = -5

                if event.key == pygame.K_RIGHT:
                    playerX_change = 5

                if (
                    event.key == pygame.K_SPACE
                    and bullet_state == "ready"
                ):
                    bulletX = playerX
                    bulletY = playerY

                    fire_bullet(bulletX, bulletY)
                    laser_sound.play()

            if (
                event.type == pygame.KEYUP
                and event.key in [
                    pygame.K_LEFT, pygame.K_RIGHT
                ]
            ):
                playerX_change = 0

    if not game_over:

        # Player movement
        playerX += playerX_change
        playerX = max(
            0, min(playerX, SCREEN_WIDTH - 64)
        )

        # Enemy movement
        for i in range(num_of_enemies):

            if enemyY[i] > 340:
                game_over = True
                pygame.mixer.music.stop()
                game_over_sound.play()
                break

            enemyX[i] += enemyX_change[i]

            if (
                enemyX[i] <= 0
                or enemyX[i] >= SCREEN_WIDTH - 64
            ):
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]

            # Collision detection
            if (
                bullet_state == "fire"
                and isCollision(
                    enemyX[i], enemyY[i],
                    bulletX, bulletY
                )
            ):
                explosion_sound.play()

                bulletY = PLAYER_START_Y
                bullet_state = "ready"

                score_value += 1

                enemyX[i] = random.randint(
                    0, SCREEN_WIDTH - 64
                )
                enemyY[i] = random.randint(
                    ENEMY_START_Y_MIN,
                    ENEMY_START_Y_MAX
                )

            enemy(enemyX[i], enemyY[i], i)

        # Bullet movement
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"

        elif bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        # Draw player
        player(playerX, playerY)

    else:
        # Keep the background and score visible
        game_over_text()

    # Display score
    show_score(textX, textY)

    # Update display
    pygame.display.update()

pygame.quit()