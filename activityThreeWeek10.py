class Board:
    """Represents the Tic Tac Toe board."""

    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        """Display the board."""
        print("\n")
        for i, row in enumerate(self.grid):
            print(" | ".join(row))
            if i < 2:
                print("-" * 5)

    def empty_squares(self):
        """Return list of empty squares."""
        return [(r, c) for r in range(3) for c in range(3) if self.grid[r][c] == " "]

    def make_move(self, row, col, symbol):
        """Place a symbol if valid."""
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def won_game(self, symbol):
        """Check if symbol has won."""
        lines = self.grid + [list(col) for col in zip(*self.grid)]
        lines.append([self.grid[i][i] for i in range(3)])
        lines.append([self.grid[i][2 - i] for i in range(3)])
        return any(all(cell == symbol for cell in line) for line in lines)

    def game_over(self):
        """Return True if someone wins or draw."""
        return self.won_game("X") or self.won_game("O") or len(self.empty_squares()) == 0


class Player:
    """Represents a player."""

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    """Main Tic Tac Toe game."""

    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1

    def other_player(self):
        """Switch turns."""
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def make_human_move(self):
        """Handle a player's move."""
        while True:
            try:
                row = int(input(f"{self.current_player.name}, enter row (0–2): "))
                col = int(input(f"{self.current_player.name}, enter col (0–2): "))
                if (row, col) in self.board.empty_squares():
                    self.board.make_move(row, col, self.current_player.symbol)
                    break
                print(" Invalid move — square already taken or out of range.")
            except ValueError:
                print(" Please enter valid numbers between 0 and 2.")

    def play_one_turn(self):
        """Play a single turn."""
        self.make_human_move()

    def play_game(self):
        """Main game loop."""
        print("=== Tic Tac Toe (Human1 vs Human2) ===")
        self.board.display()
        while not self.board.game_over():
            print(f"\n{self.current_player.name}'s turn ({self.current_player.symbol})")
            self.play_one_turn()
            self.board.display()
            if self.board.won_game(self.current_player.symbol):
                print(f" {self.current_player.name} wins!")
                return
            self.other_player()
        print(" It's a draw!")

    def print_result(self):
        """Print final result."""
        print("Game finished. Thanks for playing!")


if __name__ == "__main__":
    game = Game()
    game.play_game()
    game.print_result()
