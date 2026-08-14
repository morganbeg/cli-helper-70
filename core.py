from typing import List, Dict, Any

class Game:
    """Represents a game instance."""
    def __init__(self, name: str, genre: str, rating: float) -> None:
        self.name = name
        self.genre = genre
        self.rating = rating

    def __repr__(self) -> str:
        return f"<Game(name={self.name}, genre={self.genre}, rating={self.rating})>"

class GameLibrary:
    """Manages a collection of games."""
    def __init__(self) -> None:
        self.games: List[Game] = []

    def add_game(self, game: Game) -> None:
        """Adds a new game to the library."""
        self.games.append(game)

    def get_games(self) -> List[Dict[str, Any]]:
        """Returns a list of games in the library as dictionaries."""
        return [vars(game) for game in self.games]

    def find_game(self, name: str) -> Game:
        """Finds a game by name in the library."""
        for game in self.games:
            if game.name.lower() == name.lower():
                return game
        return None

# Example usage (to be removed in production):
game1 = Game(name='Cyberpunk 2077', genre='RPG', rating=8.0)
game2 = Game(name='The Witcher 3', genre='RPG', rating=9.5)
library = GameLibrary()
library.add_game(game1)
library.add_game(game2)
print(library.get_games())
print(library.find_game('Cyberpunk 2077'))