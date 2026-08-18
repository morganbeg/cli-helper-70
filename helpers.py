import random
import math

def roll_dice(sides=6):
    """Roll a dice with a given number of sides."""
    return random.randint(1, sides)

def calculate_distance(point_a, point_b):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)

def choose_random_item(items):
    """Select a random item from a list."""
    return random.choice(items)

def format_player_stats(player_name, health, score):
    """Format player's stats for display."""
    return f'{player_name}: Health = {health}, Score = {score}'

def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum."""
    return max(min_value, min(value, max_value))
