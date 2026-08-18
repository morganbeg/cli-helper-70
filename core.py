import random

class Game:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.players = []

    def add_player(self, player_name):
        self.players.append(player_name)
        print(f"Player {player_name} added to {self.title}.")

    def start_game(self):
        print(f"Starting {self.title}...")
        if not self.players:
            print("No players available to start the game!")
            return
        print(f"Players: {', '.join(self.players)}")
        self.play_round()

    def play_round(self):
        result = random.choice(self.players)
        print(f"{result} wins this round!")

    def show_players(self):
        print(f"Current players in {self.title}: {', '.join(self.players)}")


def main():
    game = Game("Galactic Battle", "Strategy")
    game.add_player("Alice")
    game.add_player("Bob")
    game.start_game()
    game.show_players()

if __name__ == "__main__":
    main()