import unittest
from cuatro_en_linea import fullColumn, Game

class testCuatroEnLinea(unittest.TestCase):
    def test_board(self):
        game = Game()
        self.assertEqual(len(game.board), 8)
        self.assertEqual(len(game.board[0]), 8)
    
    # def test_cambiar_jugador(self):
    #     game = Game()
    #     game.cambiar_jugador()
    #     self.assertEqual(game.cambiar_jugador(),game.jugador == False)

    def test_insert_token(self):
        game = Game()
        game.insert_token(3)
        game.insert_token(5)
        game.insert_token(6)
        game.insert_token(6)
        self.assertEqual(game.board[7][3],"x")
        self.assertEqual(game.board[7][5],"o")
        self.assertEqual(game.board[7][6],"x")
        self.assertEqual(game.board[6][6],"o")
    
    def test_column_winner(self):
        game = Game()
        game.insert_token(3)
        game.insert_token(5)
        game.insert_token(3)
        game.insert_token(6)
        game.insert_token(3)
        game.insert_token(7)
        game.insert_token(3)
        print(game.board)
        self.assertEqual(game.column_winner(), True)
    
    def test_row_winner(self):
        game = Game()
        game.insert_token(3)
        game.insert_token(1)
        game.insert_token(4)
        game.insert_token(1)
        game.insert_token(5)
        game.insert_token(3)
        game.insert_token(6)
        game.insert_token(6)
        self.assertEqual(game.row_winner(),True)
    
    def test_decreasing_diagonal_winner(self):
        game = Game()
        game.insert_token(3)#x
        game.insert_token(3)#o
        game.insert_token(3)#x
        game.insert_token(3)#o
        game.insert_token(4)#x
        game.insert_token(4)#o
        game.insert_token(5)#x
        game.insert_token(4)#o
        game.insert_token(7)#x
        game.insert_token(5)#o
        game.insert_token(7)#x
        game.insert_token(6)#o
        self.assertEqual(game.decreasing_diagonal_winner(),True)

    def test_growing_diagonal_winner(self):
        game = Game()
        game.insert_token(0)#x
        game.insert_token(1)#o
        game.insert_token(1)#x
        game.insert_token(2)#o
        game.insert_token(2)#x
        game.insert_token(3)#o
        game.insert_token(2)#x
        game.insert_token(3)#o
        game.insert_token(3)#x
        game.insert_token(5)#o
        game.insert_token(3)#x
        # print(game.board)
        self.assertEqual(game.growing_diagonal_winner(),True)

    def test_growing_diagonal_winner2(self):
        game = Game()
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(2)
        game.insert_token(3)
        game.insert_token(4)
        game.insert_token(5)
        game.insert_token(6)
        game.insert_token(7)
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(2)
        game.insert_token(3)
        game.insert_token(5)
        game.insert_token(6)
        game.insert_token(7)
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(2)
        game.insert_token(3)
        game.insert_token(4)
        game.insert_token(5)
        game.insert_token(6)
        game.insert_token(7)
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(0)
        game.insert_token(2)
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(0)
        game.insert_token(3)
        # print(game.board)
        self.assertEqual(game.column_winner(), True)
        self.assertEqual(game.row_winner(), False)
        self.assertEqual(game.growing_diagonal_winner(), False)
        self.assertEqual(game.decreasing_diagonal_winner(), False)


if __name__ == '__main__':
    unittest.main()