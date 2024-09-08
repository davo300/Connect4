# player.py
import random

class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece

    def get_move(self, board):
        valid_move = False
        move = None
        while not valid_move:
            try:
                move = int(input(f"{self.name}, choose a column (0-6): "))
                if move >= 0 and move < 7 and board.is_valid_location(move):
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number.")
        return move

class ComputerPlayer(Player):
    def __init__(self, name, piece):
        super().__init__(name, piece)

    def get_move(self, board):
        # Computer makes a random valid move (can improve this strategy later)
        valid_moves = [col for col in range(7) if board.is_valid_location(col)]
        return random.choice(valid_moves)
