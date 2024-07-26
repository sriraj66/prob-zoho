import pygame

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Paddle
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width // 2) - (paddle_width // 2)
paddle_y = screen_height - 20
paddle_speed = 10

# Ball
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 3
ball_speed_y = -3

# Bricks
brick_width = 75
brick_height = 20
bricks = []

for i in range(7):
    for j in range(5):
        bricks.append(pygame.Rect(i * (brick_width + 10) + 35, j * (brick_height + 10) + 50, brick_width, brick_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

def draw_bricks(bricks):
    for brick in bricks:
        pygame.draw.rect(screen, blue, brick)

def game_loop():
    global paddle_x, ball_x, ball_y, ball_speed_x, ball_speed_y

    running = True
    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x <= 0 or ball_x >= screen_width - ball_radius:
            ball_speed_x = -ball_speed_x
        if ball_y <= 0:
            ball_speed_y = -ball_speed_y
        if ball_y >= screen_height:
            running = False

        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)

        if paddle_rect.colliderect(ball_rect):
            ball_speed_y = -ball_speed_y

        bricks_to_remove = []
        for brick in bricks:
            if brick.colliderect(ball_rect):
                ball_speed_y = -ball_speed_y
                bricks_to_remove.append(brick)

        for brick in bricks_to_remove:
            bricks.remove(brick)

        pygame.draw.rect(screen, white, paddle_rect)
        pygame.draw.ellipse(screen, white, ball_rect)
        draw_bricks(bricks)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Example usage:
game_loop()
