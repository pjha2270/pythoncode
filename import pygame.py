import pygame
import random

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
size = (600, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake and food
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = 15
food_pos = [random.randrange(1, 600//10) * 10, random.randrange(1, 480//10) * 10]
food_spawn = True

# Set up the game over function
def game_over():
    font_style = pygame.font.SysFont(None, 50)
    game_over_text = font_style.render("Game Over!", True, WHITE)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (size[0]//2, size[1]//2)
    screen.fill(BLACK)
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

# import pygame.py

# Set up the game loop
def game_loop():
    global snake_pos
    global snake_speed
    global food_pos
    global snake_size
    game_exit = False
    snake_speed = [0, 10]  # Initialize snake_speed here
    snake_size = 3  # Initialize snake_size here
    food_pos = [random.randrange(1, 600//10) * 10, random.randrange(1, 480//10) * 10]  # Initialize food_pos here
    snake_pos = [[100, 50]]  # Initialize snake_pos here
    while not game_exit:
        while game_exit:
            screen.fill(BLACK)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = False
                    game_over()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = False
                        game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_speed != [10, 0]:
                    snake_speed = [-10, 0]
                elif event.key == pygame.K_RIGHT and snake_speed != [-10, 0]:
                    snake_speed = [10, 0]
                elif event.key == pygame.K_UP and snake_speed != [0, 10]:
                    snake_speed = [0, -10]
                elif event.key == pygame.K_DOWN and snake_speed != [0, -10]:
                    snake_speed = [0, 10]

        # Update the snake's position
        if snake_pos[0][0] >= size[0] or snake_pos[0][0] < 0 or snake_pos[0][1] >= size[1] or snake_pos[0][1] < 0:
            game_over()
        snake_pos.insert(0, [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]])
        snake_pos = snake_pos[:snake_size]

        # Check if the snake has collided with itself
        for segment in snake_pos[1:]:
            if segment == snake_pos[0]:
                game_over()

        # Check if the snake has eaten the food
        if snake_pos[0] == food_pos:
            food_pos = [random.randrange(1, 600//10) * 10, random.randrange(1, 480//10) * 10]
            snake_size += 1
            snake_pos.extend([(0, 0)] * (snake_size - len(snake_pos)))

        # Draw the snake and food
        screen.fill(BLACK)
        for pos in snake_pos:
            pygame.draw.rect(screen, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        pygame.display.update()

        clock.tick(10)

game_loop()
pygame.quit()
quit()