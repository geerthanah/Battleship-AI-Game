import unittest
from core.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=5)

    def test_place_ship_valid(self):
        result = self.board.place_ship(2, 3)
        self.assertTrue(result)
        self.assertEqual(self.board.grid[2][3], 'S')

    def test_place_ship_invalid(self):
        self.board.place_ship(2, 3)
        result = self.board.place_ship(2, 3)  # Replacing same spot
        self.assertFalse(result)

    def test_attack_hit(self):
        self.board.place_ship(1, 1)
        result = self.board.attack(1, 1)
        self.assertTrue(result)
        self.assertEqual(self.board.grid[1][1], 'X')

    def test_attack_miss(self):
        result = self.board.attack(0, 0)
        self.assertFalse(result)
        self.assertEqual(self.board.grid[0][0], 'O')

    def test_all_ships_sunk(self):
        self.board.place_ship(0, 0)
        self.board.attack(0, 0)
        self.assertTrue(self.board.all_ships_sunk())

        self.board.place_ship(1, 1)
        self.assertFalse(self.board.all_ships_sunk())

if __name__ == '__main__':
    unittest.main()
