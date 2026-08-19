import json
import os

class GameHandler:
    def __init__(self, game_data_file):
        self.game_data_file = game_data_file
        self.games = self.load_games()

    def load_games(self):
        """Load games from a JSON file."""
        if not os.path.exists(self.game_data_file):
            return []
        with open(self.game_data_file, 'r') as file:
            return json.load(file)

    def save_games(self):
        """Save the games to a JSON file."""
        with open(self.game_data_file, 'w') as file:
            json.dump(self.games, file, indent=4)

    def add_game(self, game):
        """Add a new game to the list."""
        self.games.append(game)
        self.save_games()

    def remove_game(self, game_name):
        """Remove a game by its name."""
        self.games = [g for g in self.games if g['name'] != game_name]
        self.save_games()

    def get_games(self):
        """Retrieve the list of games."""
        return self.games

# Example usage:
# handler = GameHandler('games.json')
# handler.add_game({'name': 'Game1', 'genre': 'Action'})
# print(handler.get_games())
