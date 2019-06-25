"""
Definiton of Board class
"""
from constants import ROW_COUNT, COLUMN_COUNT
import numpy as np


# TODO Add functions to count each players ones, twos and threes in a row,
# column and diagonal to create score metrics after each move
class Board():
    def __init__(self):
        self.__rows = ROW_COUNT
        self.__columns = COLUMN_COUNT
        self.__board = np.zeros((self.__rows, self.__columns), np.int8)

    @property
    def board(self):
        return self.__board

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    def print_board(self):
        """
        Prints board to standard output
        """
        print(np.flipud(self.__board))

    def drop_piece(self, row, col, piece):
        """
        Drops new piece to game board.
        """
        self.__board[row, col] = piece

    def is_empty_slot_in(self, col) -> bool:
        """
        Checks if there is place in column to add another piece
        """
        return np.count_nonzero(self.__board[:, col] == 0) != 0

    def get_open_row(self, col) -> int:
        """
        Returns index of first, not occupied row in column
        It throws error if there are no empty slots in column!
        """
        return np.nonzero(self.__board[:, col] == 0)[0][0]

    def is_move_winning(self, piece) -> bool:
        """
        Check if there are 3 same elements in row, column or diagonal
        """
        # check rows
        for row in range(self.__rows):
            for column in range(self.__columns - 4):
                if np.count_nonzero(
                        self.__board[row, column:column + 4] == piece) == 4:
                    return True
        # check columns
        for column in range(self.__columns):
            for row in range(self.__rows - 4):
                if np.count_nonzero(
                        self.__board[row:row + 4, column] == piece) == 4:
                    return True

        # check diagonals
        for diagonal in range(-2, 3):
            if np.count_nonzero(self.__board.diagonal(diagonal) == piece) == 4:
                return True
            elif np.count_nonzero(
                    np.fliplr(self.__board).diagonal(diagonal) == piece) == 4:
                return True

        return False
