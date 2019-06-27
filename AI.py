"""
File containig different oponents AI classes
"""
import random
import Board
from constants import COLUMN_COUNT


class RandomAI:
    """
    AI that picks next move randomly.
    """

    def __init__(self, board):
        self._board = board

    def get_next_move(self) -> int:
        """
        Returns AI's next move
        """
        column = -1
        while not self._board.is_empty_slot_in(column):
            column = random.randint(0, COLUMN_COUNT - 1)
        return column
