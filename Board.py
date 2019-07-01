"""
Definiton of Board class
"""
from constants import ROW_COUNT, COLUMN_COUNT
import numpy as np


# TODO Add functions to count each players ones, twos and threes in a row,
# column and diagonal to create score metrics after each move
class Board():
    def __init__(self):
        self._rows = ROW_COUNT
        self._columns = COLUMN_COUNT
        self._board = np.zeros((self._rows, self._columns), np.int8)

    @property
    def board(self):
        return self._board

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def print_board(self):
        """
        Prints board to standard output
        """
        print(np.flipud(self._board))

    # TODO this is only for debugging
    def print_board_not_flipped(self):
        print(self._board)

    def drop_piece(self, row, col, piece):
        """
        Drops new piece to game board.
        """
        self._board[row, col] = piece

    def is_empty_slot_in(self, col) -> bool:
        """
        Checks if there is place in column to add another piece
        """
        if col >= 0 and col < COLUMN_COUNT:
            return np.count_nonzero(self._board[:, col] == 0) != 0
        else:
            return False

    def get_valid_locations(self) -> [int]:
        """
        Returns columns with empty slots
        """
        return [col for col in range(COLUMN_COUNT) if
                self.is_empty_slot_in(col)]

    def get_open_row(self, col) -> int:
        """
        Returns index of first, not occupied row in column
        It throws error if there are no empty slots in column!
        """
        return np.nonzero(self._board[:, col] == 0)[0][0]

    def is_move_winning(self, piece) -> bool:
        """
        Check if there are 3 same elements in row, column or diagonal
        """
        # check rows
        for row in range(self._rows):
            for column in range(self._columns - 4):
                if np.count_nonzero(
                        self._board[row, column:column + 4] == piece) == 4:
                    return True
        # check columns
        for column in range(self._columns):
            for row in range(self._rows - 4):
                if np.count_nonzero(
                        self._board[row:row + 4, column] == piece) == 4:
                    return True

        # check diagonals
        for diagonal in range(-2, 3):
            if np.count_nonzero(self._board.diagonal(diagonal) == piece) == 4:
                return True
            elif np.count_nonzero(
                    np.fliplr(self._board).diagonal(diagonal) == piece) == 4:
                return True

        return False
