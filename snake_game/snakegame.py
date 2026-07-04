import pygame
import random
import os
import sys
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pygame.init()
pygame.mouse.set_visible(False)
pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load(os.path.join(BASE_DIR, "sounds", "background.mp3"))
eat_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "eat.wav"))
gameover_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "gameover.wav"))
apple = pygame.image.load(os.path.join(BASE_DIR, "images", "apple.png"))
icon = pygame.image.load(os.path.join(BASE_DIR, "images", "icon.png"))
apple = pygame.transform.scale(apple, (20, 20))
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
eat_flash = 0
try:
    with open(os.path.join(BASE_DIR, "highscore.txt"), "r") as f:
        high_score = int(f.read())
except:
    high_score = 0
screen = pygame.display.set_mode((800, 600))
pygame.display.set_icon(icon)
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
paused = False
clock = pygame.time.Clock()
def reset_game():
    global score, direction
    global snake_x, snake_y
    global snake_list, snake_length
    global food_x, food_y
    global game_over, game_started
    global paused

    score = 0
    direction = "RIGHT"

    snake_x = 300
    snake_y = 200

    snake_list = []
    snake_length = 1

    while True:
        food_x = random.randrange(0, 800, 20)
        food_y = random.randrange(0, 600, 20)

        if [food_x, food_y] not in snake_list:
            break

    game_over = False
    game_started = False
    paused = False

def draw_grid():
    for x in range(0, 800, 20):
        pygame.draw.line(screen, (0, 35, 0), (x, 0), (x, 600))

    for y in range(0, 600, 20):
        pygame.draw.line(screen, (0, 35, 0), (0, y), (800, y))

while running:
    if not game_started:

        screen.fill(BLACK)

        title = font.render("Snake Game", True, GREEN)

        start = font.render("SPACE - Start", True, WHITE)

        pause_info = font.render("P - Pause", True, WHITE)

        quit_info = font.render("ESC - Quit", True, WHITE)

        high = font.render(f"High Score : {high_score}", True, YELLOW)

        screen.blit(title, (190,150))
        screen.blit(start, (280,220))
        screen.blit(pause_info, (295,260))
        screen.blit(quit_info, (285,300))
        screen.blit(high, (255,360))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                   game_started = True
                   pygame.mixer.music.play(-1)
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_ESCAPE:
                    running = False

        continue

    screen.fill(BLACK)
    draw_grid()

    for segment in snake_list:

        pygame.draw.rect(
        screen,
        GREEN,
        (segment[0], segment[1], snake_size, snake_size))
    if eat_flash > 0:
        pygame.draw.circle(
        screen,
        YELLOW,
        (food_x + 10, food_y + 10),
        15
        )
        eat_flash -= 1
    screen.blit(apple, (food_x, food_y))

    if game_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.mixer.music.play(-1)
                    reset_game()
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BLACK)
        pygame.draw.rect(
    screen,
    RED,
    (150,150,500,300),
    4
)
        over_text = font.render(
    "GAME OVER",
    True,
    RED
)

        score_text = font.render(
    f"Score : {score}",
    True,
    WHITE
)

        high_score_text = font.render(
    f"High Score : {high_score}",
    True,
    YELLOW
)

        restart_text = font.render(
    "R - Restart",
    True,
    WHITE
)

        quit_text = font.render(
    "ESC - Quit",
    True,
    WHITE
)

        screen.blit(over_text, (250,180))
        screen.blit(score_text, (270,240))
        screen.blit(high_score_text, (240,280))
        screen.blit(restart_text, (270,340))
        screen.blit(quit_text, (270,380))

        pygame.display.update()

        continue

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

            elif event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    if paused:
        screen.fill(BLACK)
        
        pygame.draw.rect(
        screen,
        YELLOW,
        (170,180,460,180),
        3
    )

        pause_text = font.render(
        "GAME PAUSED",
        True,
        YELLOW
    )

        resume_text = font.render(
        "Press P to Resume",
        True,
        WHITE
    )

        screen.blit(pause_text, (250, 250))
        screen.blit(resume_text, (220, 300))

        pygame.display.update()
        clock.tick(10)
        continue

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

        while True:

            food_x = random.randrange(0, 800, 20)
            food_y = random.randrange(0, 600, 20)

            if [food_x, food_y] not in snake_list:
                break
        score += 1
        snake_length += 1
        eat_sound.play()
        eat_flash = 5
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
    eye_radius = 2

    if direction == "RIGHT":
        pygame.draw.circle(screen, BLACK, (head[0] + 15, head[1] + 5), eye_radius)
        pygame.draw.circle(screen, BLACK, (head[0] + 15, head[1] + 15), eye_radius)

    elif direction == "LEFT":
        pygame.draw.circle(screen, BLACK, (head[0] + 5, head[1] + 5), eye_radius)
        pygame.draw.circle(screen, BLACK, (head[0] + 5, head[1] + 15), eye_radius)

    elif direction == "UP":
        pygame.draw.circle(screen, BLACK, (head[0] + 5, head[1] + 5), eye_radius)
        pygame.draw.circle(screen, BLACK, (head[0] + 15, head[1] + 5), eye_radius)

    elif direction == "DOWN":
        pygame.draw.circle(screen, BLACK, (head[0] + 5, head[1] + 15), eye_radius)
        pygame.draw.circle(screen, BLACK, (head[0] + 15, head[1] + 15), eye_radius)
    score_text = font.render(
    f"Score : {score}",
    True,
    WHITE
    )
    screen.blit(score_text, (10, 10))
    high_text = font.render(
    f"High Score : {high_score}",
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
with open(os.path.join(BASE_DIR, "highscore.txt"), "w") as f:
    f.write(str(high_score))
pygame.mouse.set_visible(True)
pygame.quit()