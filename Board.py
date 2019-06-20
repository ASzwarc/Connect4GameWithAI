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
        print(self.board)
