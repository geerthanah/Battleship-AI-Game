from core.board import Board

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()

    def place_ships(self, n=3):
        placed = 0
        while placed < n:
            x, y = map(int, input(f"{self.name}, enter ship position (x y): ").split())
            if self.board.place_ship(x, y):
                placed += 1
            else:
                print("Invalid position. Try again.")
