"""
File containig different oponents AI classes
"""
import random
import numpy as np
from math import inf
import Board
from constants import COLUMN_COUNT, AI, HUMAN
import copy


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


class SimpleLogicAI:
    """
    AI that calculates number of empty slots and tries to block oppononet
    based on current state of board
    """

    def __init__(self, board):
        self._board = board

    def get_next_move(self) -> int:
        """
        Returns AI's next move. AI is inserting piece in temporary board,
        which is copy of current board, and checks which move gives best score.
        """
        best_score = -inf
        best_column = -1
        for column_no in range(COLUMN_COUNT):
            temp_board = copy.deepcopy(self._board)
            row = temp_board.get_open_row(column_no)
            temp_board.drop_piece(row, column_no, AI)
            score = self.get_score(AI)
            if score > best_score:
                best_score = score
                best_column = column_no
        return best_column

    def evalute_window(self, window, piece) -> int:
        """
        Evaluates score for given window and piece
        """
        if piece == HUMAN:
            oponent = AI
        else:
            oponent = HUMAN
        score = 0
        if np.count_nonzero(window == piece) == 4:
            score += 100
        elif (np.count_nonzero(window == piece) == 3 and
                np.count_nonzero(window == 0) >= 1):
            score += 10
        elif (np.count_nonzero(window == piece) == 2 and
                np.count_nonzero(window == 0) >= 2):
            score += 5
        else:
            pass

        if (np.count_nonzero(window == oponent) == 3 and
                np.count_nonzero(window == 0) >= 1):
            score -= 80

        return score

    # TODO Consider refactoring this and moving to Board class.
    # Evaluate function could be passed as a parameter
    def get_score(self, piece) -> int:
        """
        Calculates current score for given piece. It's mainly used by AIs.
        """
        score = 0
        for column in range(self._board.columns):
            score += self.evalute_window(self._board.board[:, column], piece)

        for row in range(self._board.rows):
            score += self.evalute_window(self._board.board[row, :], piece)

        for diagonal_no in range(-2, 3):
            score += self.evalute_window(self._board.board.diagonal(
                diagonal_no), piece)
            score += self.evalute_window(np.fliplr(self._board.board).diagonal(
                diagonal_no), piece)
        return score
