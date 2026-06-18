import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pradeepp Snake Game")
score = 0
direction = "RIGHT"
font = pygame.font.SysFont(None, 35)
snake_x = 300
snake_y = 200
snake_list = []
snake_length = 1
snake_size = 20
food_x = random.randrange(0, 800, 20)
food_y = random.randrange(0, 600, 20)
running = True
game_over = False
clock = pygame.time.Clock()
while running:

    screen.fill((0, 0, 0))

    for segment in snake_list:

        pygame.draw.rect(
        screen,
        (0, 255, 0),
        (segment[0], segment[1], snake_size, snake_size))
    pygame.draw.rect(
    screen,
    (255, 0, 0),
    (food_x, food_y, 20, 20)
    )
    if game_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        over_text = font.render(
        f"GAME OVER! Score: {score}",
        True,
        (255, 0, 0)
        )

        screen.blit(over_text, (220, 280))

        pygame.display.update()

        continue

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            elif event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
    if direction == "LEFT":
        snake_x -= 20

    elif direction == "RIGHT":
        snake_x += 20

    elif direction == "UP":
        snake_y -= 20

    elif direction == "DOWN":
        snake_y += 20
        
    if snake_x < 0 or snake_x > 780 or snake_y < 0 or snake_y > 580:
        game_over = True

    if snake_x == food_x and snake_y == food_y:

        food_x = random.randrange(0, 800, 20)
        food_y = random.randrange(0, 600, 20)
        score += 1
        snake_length += 1
        print("Food Eaten!")
    
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)

    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]
    for segment in snake_list[:-1]:

        if segment == snake_head:

            game_over = True
    score_text = font.render(
    f"Score: {score}",
    True,
    (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(8)
pygame.quit()