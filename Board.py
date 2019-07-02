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
        Check if there are 4 same elements in row, column or diagonal
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
        for diagonal in range(-2, 4):
            if np.count_nonzero(self._board.diagonal(diagonal) == piece) == 4:
                return True
            elif np.count_nonzero(
                    np.fliplr(self._board).diagonal(diagonal) == piece) == 4:
                return True

        return False

    def evaluate_window(self, window_length,
                        piece, evaluation_function) -> int:
        """
        Applies evaluation function on every diagonal, row, column
        of window_length. Returns obtained score. Evaluation_function should
        accept two parameters: array to be evaluated and piece number
        """
        score = 0
        # Center column
        center_column = np.array(self.board[:, COLUMN_COUNT // 2]).flatten()
        score += evaluation_function(center_column, piece, True)

        # Vertical
        for column in range(self.columns):
            array = np.array(self.board[:, column]).flatten()
            for row in range(self.rows - window_length + 1):
                result = evaluation_function(array[row:row + window_length],
                                             piece)
                score += result
        # Horizontal
        for row in range(self.rows):
            array = np.array(self.board[row, :]).flatten()
            for column in range(self.columns - window_length + 1):
                score += evaluation_function(
                    array[column:column + window_length], piece)
        # Diagonal
        for row in range(self.rows):
            for column in range(self.columns - window_length + 1):
                array_pos = np.array(
                    self.board[row:row + window_length,
                               column:column + window_length].
                    diagonal(0)).flatten()
                score += evaluation_function(array_pos, piece)

                array_neg = np.array(np.fliplr(self.board)
                                     [row:row + window_length,
                                      column:column + window_length].
                                     diagonal(0)).flatten()
                score += evaluation_function(array_neg, piece)
        return score
