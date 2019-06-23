"""
Definiton of Board class
"""
from constants import ROW_COUNT, COLUMN_COUNT
import numpy as np


class Board():
    def __init__(self):
        self.rows = ROW_COUNT
        self.columns = COLUMN_COUNT
        self.board = np.zeros((self.rows, self.columns), np.int8)

    def print_board(self):
        """
        Prints board to standard output
        """
        print(np.flipud(self.board))

    def drop_piece(self, row, col, piece):
        """
        Drops new piece to game board.
        """
        self.board[row][col] = piece

    def is_move_winning(self, piece) -> bool:
        """
        Check if there are 3 same elements in row, column or diagonal
        """
        # check rows
        for row in range(self.rows):
            for column in range(self.columns - 3):
                if np.count_nonzero(
                        self.board[row, column:column + 3] == piece) == 3:
                    print("Winning row {}, columns[{} : {}]".format(
                        row, column, column + 3))
                    return True
        # check columns
        for column in range(self.columns):
            for row in range(self.rows - 3):
                if np.count_nonzero(
                        self.board[row:row + 3, column] == piece) == 3:
                    print("Winning column {}, rows[{} : {}]".format(
                        column, row, row + 3))
                    return True

        # check diagonals
        for diagonal in range(-3, 4):
            if np.count_nonzero(self.board.diagonal(diagonal) == piece) == 3:
                print("Winning diagonal {}".format(diagonal))
                return True
            elif np.count_nonzero(
                    np.fliplr(self.board).diagonal(diagonal) == piece) == 3:
                print("Winning diagonal, flipped {}".format(diagonal))
                return True

        return False
