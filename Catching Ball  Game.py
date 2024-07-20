import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Basket dimensions
basket_width = 100
basket_height = 20

# Ball dimensions and speed
ball_radius = 15
ball_speed = 5

# Basket speed
basket_speed = 10

# Initialize screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catch the Ball Game')

# Font for displaying text
font = pygame.font.SysFont(None, 36)

# Basket position
basket_x = screen_width // 2 - basket_width // 2
basket_y = screen_height - 50

# Ball position and initial direction (falling)
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = ball_radius
ball_dy = ball_speed

# Score
score = 0
missed = 0
total_chances = 5  # Total chances allowed

# Function to draw basket
def draw_basket():
    pygame.draw.rect(screen, yellow, [basket_x, basket_y, basket_width, basket_height])

# Function to draw ball
def draw_ball():
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

# Function to display text
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to reset game state
def reset_game():
    global score, missed, ball_x, ball_y, ball_dy, game_over
    score = 0
    missed = 0
    ball_x = random.randint(ball_radius, screen_width - ball_radius)
    ball_y = ball_radius
    ball_dy = ball_speed
    game_over = False

# Main game loop
running = True
game_over = False
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Move basket with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    elif keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
        basket_x += basket_speed

    if not game_over:
        # Move the ball
        ball_y += ball_dy

        # Check if the ball is caught by the basket
        if ball_y + ball_radius >= basket_y and basket_x < ball_x < basket_x + basket_width:
            score += 1
            ball_x = random.randint(ball_radius, screen_width - ball_radius)
            ball_y = ball_radius
            ball_dy = ball_speed

        # Check if the ball hits the bottom of the screen
        if ball_y > screen_height:
            missed += 1
            if missed >= total_chances:
                game_over = True
            else:
                ball_x = random.randint(ball_radius, screen_width - ball_radius)
                ball_y = ball_radius
                ball_dy = ball_speed

    # Draw everything
    screen.fill(black)
    draw_basket()
    draw_ball()
    display_text(f"Score: {score}", white, 10, 10)
    display_text(f"Missed: {missed}/{total_chances}", white, screen_width - 150, 10)

    if game_over:
        display_text("Game Over", white, screen_width // 2 - 80, screen_height // 2)
        display_text("Press P to Play Again or Q to Quit", white, screen_width // 2 - 200, screen_height // 2 + 50)

        # Handle play again or quit
        if keys[pygame.K_p]:
            reset_game()
        elif keys[pygame.K_q]:
            running = False

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(60)

pygame.quit()
