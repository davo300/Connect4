# game.py
import numpy as np
from player import Player, ComputerPlayer

class Board:
    def __init__(self):
        self.board = np.zeros((6, 7))  # 6 rows, 7 columns

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[5][col] == 0  # Check if the top row is empty

    def get_next_open_row(self, col):
        for r in range(6):
            if self.board[r][col] == 0:
                return r

    def print_board(self):
        print(np.flip(self.board, 0))  # Flip the board to display correctly

    def winning_move(self, piece):
        # Check horizontal locations for a win
        for c in range(4):
            for r in range(6):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return True

        # Check vertical locations for a win
        for c in range(7):
            for r in range(3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return True

        # Check positively sloped diagonals
        for c in range(4):
            for r in range(3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return True

        # Check negatively sloped diagonals
        for c in range(4):
            for r in range(3, 6):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return True

        return False

def play_game():
    board = Board()
    player1 = Player("Player 1", 1)
    player2 = ComputerPlayer("Computer", 2)

    game_over = False
    turn = 0

    while not game_over:
        board.print_board()
        if turn == 0:
            col = player1.get_move(board)
        else:
            col = player2.get_move(board)

        if board.is_valid_location(col):
            row = board.get_next_open_row(col)
            board.drop_piece(row, col, player1.piece if turn == 0 else player2.piece)

            if board.winning_move(player1.piece if turn == 0 else player2.piece):
                board.print_board()
                print(f"{'Player 1' if turn == 0 else 'Computer'} wins!")
                game_over = True

        turn = (turn + 1) % 2  # Switch turns

if __name__ == '__main__':
    play_game()
