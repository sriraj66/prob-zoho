import curses
import random

# Game settings
screen_width = 40
screen_height = 20
paddle_width = 6
ball_speed = 1

# Initialize curses
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.keypad(1)
stdscr.timeout(100)

# Paddle initial position
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 2

# Ball initial position and direction
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = ball_speed
ball_dy = -ball_speed

# Initialize bricks
bricks = []
brick_width = 5
brick_height = 1
for y in range(2, 6, brick_height + 1):
    for x in range(0, screen_width, brick_width + 1):
        bricks.append((x, y))

def draw_game():
    stdscr.clear()
    for brick in bricks:
        for i in range(brick_width):
            stdscr.addch(brick[1], brick[0] + i, '#')
    for i in range(paddle_width):
        stdscr.addch(paddle_y, paddle_x + i, '-')
    stdscr.addch(ball_y, ball_x, 'O')
    stdscr.refresh()

def main(stdscr):
    global paddle_x, ball_x, ball_y, ball_dx, ball_dy

    while True:
        draw_game()

        key = stdscr.getch()

        if key == curses.KEY_LEFT and paddle_x > 0:
            paddle_x -= 1
        elif key == curses.KEY_RIGHT and paddle_x < screen_width - paddle_width:
            paddle_x += 1

        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with walls
        if ball_x <= 0 or ball_x >= screen_width - 1:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy

        # Ball collision with paddle
        if ball_y == paddle_y - 1 and paddle_x <= ball_x <= paddle_x + paddle_width:
            ball_dy = -ball_dy

        # Ball collision with bricks
        hit_brick = None
        for brick in bricks:
            if brick[0] <= ball_x < brick[0] + brick_width and brick[1] == ball_y:
                hit_brick = brick
                ball_dy = -ball_dy
                break
        if hit_brick:
            bricks.remove(hit_brick)

        # Ball falls out of the screen
        if ball_y >= screen_height:
            break

    stdscr.clear()
    stdscr.addstr(screen_height // 2, screen_width // 2 - 5, "GAME OVER")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
