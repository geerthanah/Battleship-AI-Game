import random

class Board:
    def __init__(self, size=5):
        self.size = size
        self.grid = [['~'] * size for _ in range(size)]
        self.ships = []

    def place_ship(self, x, y):
        if self.grid[x][y] == '~':
            self.grid[x][y] = 'S'
            self.ships.append((x, y))
            return True
        return False

    def attack(self, x, y):
        if self.grid[x][y] == 'S':
            self.grid[x][y] = 'X'
            return True
        elif self.grid[x][y] == '~':
            self.grid[x][y] = 'O'
        return False

    def all_ships_sunk(self):
        return all(self.grid[x][y] == 'X' for (x, y) in self.ships)

    def display(self, reveal=False):
        for row in self.grid:
            line = ''
            for cell in row:
                if cell == 'S' and not reveal:
                    line += '~ '
                else:
                    line += f"{cell} "
            print(line.strip())
