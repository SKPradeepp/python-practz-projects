import pygame
import random
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("snake_game/sounds/background.mp3")
pygame.mixer.music.set_volume(0.3)
eat_sound = pygame.mixer.Sound("snake_game/sounds/eat.wav")
gameover_sound = pygame.mixer.Sound("snake_game/sounds/gameover.wav")
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 0
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
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
game_started = False
clock = pygame.time.Clock()
while running:
    if not game_started:

        screen.fill(BLACK)

        title = font.render(
        "Snake Game",
        True,
        GREEN
        )

        start = font.render(
        "Press SPACE to Start",
        True,
        WHITE
        )

        high = font.render(
        f"High Score: {high_score}",
        True,
        YELLOW
        )

        screen.blit(title, (220, 180))
        screen.blit(start, (230, 260))
        screen.blit(high, (280, 330))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                   game_started = True
                   pygame.mixer.music.play(-1)

        continue

    screen.fill(BLACK)

    for segment in snake_list:

        pygame.draw.rect(
        screen,
        GREEN,
        (segment[0], segment[1], snake_size, snake_size))
    pygame.draw.rect(
    screen,
    RED,
    (food_x, food_y, 20, 20)
    )

    if game_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.mixer.music.play(-1)
                    score = 0
                    direction = "RIGHT"
                    snake_x = 300
                    snake_y = 200
                    snake_list = []
                    snake_length = 1
                    food_x = random.randrange(0, 800, 20)
                    food_y = random.randrange(0, 600, 20)
                    snake_head = [snake_x, snake_y]
                    game_over = False
                    game_started = False

        screen.fill((0, 0, 0))

        over_text = font.render(
        f"GAME OVER! Score: {score}",
        True,
        RED
        )

        restart_text = font.render(
        "Press R to Restart",
        True,
        WHITE
        )

        screen.blit(over_text, (220, 260))
        screen.blit(restart_text, (230, 310))

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

        if not game_over:
            pygame.mixer.music.stop()
            gameover_sound.play()
        game_over = True

    snake_head = [snake_x, snake_y]

    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]
    for segment in snake_list[:-1]:

        if segment == snake_head:

            if not game_over:
                pygame.mixer.music.stop()
                gameover_sound.play()
            game_over = True

    if snake_x == food_x and snake_y == food_y:

        food_x = random.randrange(0, 800, 20)
        food_y = random.randrange(0, 600, 20)
        score += 1
        snake_length += 1
        eat_sound.play()
        print("Food Eaten!")
        if score > high_score:
            high_score = score
    
    for segment in snake_list[:-1]:

        pygame.draw.rect(
        screen,
        DARK_GREEN,
        (segment[0], segment[1], snake_size, snake_size)
    )

    if len(snake_list) > 0:

        head = snake_list[-1]

        pygame.draw.rect(
        screen,
        GREEN,
        (head[0], head[1], snake_size, snake_size)
    )
    score_text = font.render(
    f"Score: {score}",
    True,
    WHITE
    )
    screen.blit(score_text, (10, 10))
    high_text = font.render(
    f"High Score: {high_score}",
    True,
    YELLOW
    )
    screen.blit(high_text, (10, 40))
    pygame.draw.rect(
    screen,
    WHITE,
    (0, 0, 800, 600),
    2
    )
    pygame.display.update()
    clock.tick(8 + score // 2)
with open("highscore.txt", "w") as f:
    f.write(str(high_score))
pygame.quit()