import random
from core.board import Board  # Add this import if Board is defined in core/board.py

class AIPlayer:
    def __init__(self, name="Computer"):
        self.name = name
        self.board = Board()
        self.possible_moves = [(i, j) for i in range(5) for j in range(5)]

    def place_ships(self, n=3):
        placed = 0
        while placed < n:
            x, y = random.choice(self.possible_moves)
            if self.board.place_ship(x, y):
                placed += 1

    def choose_move(self):
        # Minimax stub can go here
        return random.choice(self.possible_moves)

    def remove_move(self, x, y):
        if (x, y) in self.possible_moves:
            self.possible_moves.remove((x, y))
