import random
import time

def generate_random_number(min_value, max_value):
    """Generate a random integer within the given range."""
    return random.randint(min_value, max_value)


def wait_with_progress(seconds):
    """Wait for a specified number of seconds while displaying a progress indicator."""
    for i in range(seconds):
        print("Waiting... {}/{} seconds".format(i + 1, seconds))
        time.sleep(1)


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def format_player_score(player_name, score):
    """Format the player's score for display."""
    return f"Player: {player_name}, Score: {score}"