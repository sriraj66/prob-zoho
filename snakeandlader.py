import random

def roll_dice():
    return random.randint(1, 6)

def move_player(position, moves):
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    position += moves
    if position in snakes:
        print(f"Oops! Landed on a snake at {position}. Going down to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! Landed on a ladder at {position}. Climbing up to {ladders[position]}")
        position = ladders[position]
    return position

def play_game():
    player_position = 0
    while player_position < 100:
        input("Press Enter to roll the dice")
        dice_roll = roll_dice()
        print(f"Rolled a {dice_roll}")
        player_position = move_player(player_position, dice_roll)
        print(f"Player position: {player_position}")
        if player_position >= 100:
            print("Congratulations! You won the game.")
            break

# Example usage:
play_game()
