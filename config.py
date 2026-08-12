import json

config_data = {
    "version": "1.0",
    "game_settings": {
        "difficulty": "normal",
        "max_players": 4,
        "graphics_quality": "high"
    },
    "controls": {
        "move_up": "W",
        "move_down": "S",
        "move_left": "A",
        "move_right": "D",
        "action": "SPACE"
    }
}

def load_config(file_path):
    """Load configuration from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading config: {e}')
        return config_data


def save_config(file_path, config):
    """Save configuration to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except IOError as e:
        print(f'Error saving config: {e}')


def get_default_config():
    """Return the default configuration settings."""
    return config_data

