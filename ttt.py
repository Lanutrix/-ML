class TicTacToy():
    def __init__(self) -> None:
        self._board = [" "] * 9
        self._current_player = 'X'
    def display_board(self):
        print(f" {self._board[0]} | {self._board[1]} | {self._board[2]} ")
        print("-----------")
        print(f" {self._board[3]} | {self._board[4]} | {self._board[5]} ")
        print("-----------")
        print(f" {self._board[6]} | {self._board[7]} | {self._board[8]} ")

    def make_move(self, position):
        if self._board[position] == " ":
            self._board[position] = self._current_player
            self.switch_player()
        else:
            print("Invalid move. The position is already occupied.")

    def switch_player(self):
        self._current_player = "O" if self._current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self._board[i] == self._board[i + 3] == self._board[i + 6] != " ":
                return True  # Vertical win
            if self._board[i * 3] == self._board[i * 3 + 1] == self._board[i * 3 + 2] != " ":
                return True  # Horizontal win

        if self._board[0] == self._board[4] == self._board[8] != " " or self._board[2] == self._board[4] == self._board[6] != " ":
            return True  # Diagonal win

        return False

    def check_draw(self):
        return " " not in self._board and not self.check_winner()

    def play(self):
        while not self.check_winner() and not self.check_draw():
            self.display_board()
            position = int(input(f"{self._current_player}'s turn. Enter a position (1-9): ")) - 1

            if 0 <= position < 9:
                self.make_move(position)
            else:
                print("Invalid position. Please enter a number between 1 and 9.")
        self.switch_player()
        print(f"{self._current_player} wins!")

TicTacToy().play()