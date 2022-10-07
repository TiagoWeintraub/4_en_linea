import random

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


# column = 0
# first_row = 7
# winner = False
# a = board[first_row][column]
# print(a)

def column_winner(board,ficha):
        first_row = 0
        column = 0
        board = board
        
        while column <= 7:
            for row in board:
                if (board[first_row][column] == ficha) and (board[first_row + 1][column] == ficha) and (board[first_row + 2][column] == ficha) and (board[first_row + 3][column] == ficha):
                    winner = True # NO ENTRA EN ESTE IF
                    return winner
                if first_row == 4:
                    first_row = 0
                    break
                first_row += 1
            column += 1

a = column_winner(board,'x')
print(a)