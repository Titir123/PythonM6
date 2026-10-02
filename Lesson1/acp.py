import pygame

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tiger Wildlife")

background = pygame.image.load("backgrounds.jpg")
tiger = pygame.image.load("tiger.jpeg")

background = pygame.transform.scale(background, (500, 500))
tiger = pygame.transform.scale(tiger, (250, 250))

tiger_rect = tiger.get_rect(center=(250, 260))

heading_font = pygame.font.Font(None, 40)
fact_font = pygame.font.Font(None, 25)

heading = heading_font.render("Tiger", True, (255, 255, 255))
fact = fact_font.render("Tigers are the largest wild cats.", True, (255, 255, 255))

heading_rect = heading.get_rect(center=(250, 40))
fact_rect = fact.get_rect(center=(250, 470))

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(tiger, tiger_rect)
        screen.blit(heading, heading_rect)
        screen.blit(fact, fact_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

game_loop()