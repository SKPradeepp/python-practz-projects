import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pradeepp Snake Game")
score = 0

font = pygame.font.SysFont(None, 35)
snake_x = 300
snake_y = 200
snake_size = 20
food_x = random.randrange(0, 800, 20)
food_y = random.randrange(0, 600, 20)
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (snake_x, snake_y, snake_size, snake_size)
    )
    pygame.draw.rect(
    screen,
    (255, 0, 0),
    (food_x, food_y, 20, 20)
    )

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                snake_x -= 20

            elif event.key == pygame.K_RIGHT:
                snake_x += 20

            elif event.key == pygame.K_UP:
                snake_y -= 20

            elif event.key == pygame.K_DOWN:
                snake_y += 20

    screen.fill((0, 0, 0))

    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (snake_x, snake_y, snake_size, snake_size)
    )

    if snake_x == food_x and snake_y == food_y:

        food_x = random.randrange(0, 800, 20)
        food_y = random.randrange(0, 600, 20)
    
        score += 1
        print("Food Eaten!")

    score_text = font.render(
    f"Score: {score}",
    True,
    (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
pygame.quit()