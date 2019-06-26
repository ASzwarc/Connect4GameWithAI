"""
File containig different oponents AI classes
"""

import random
from constants import COLUMN_COUNT


class AI:

    def __init__(self, board):
        self._board = board

    def get_next_move(self) -> int:
        """
        Returns column in which next piece will be inserted
        """
        raise NotImplementedError("This is AI interface method")


class RandomAI(AI):

    def get_next_move(self) -> int:
        return random.randint(0, COLUMN_COUNT - 1)
