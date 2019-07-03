"""
File containig different oponents AI classes
"""
import random
import numpy as np
from math import inf
import Board
from constants import COLUMN_COUNT, AI, HUMAN, WINDOW_LENGTH
import copy

# TODO:
#   -> evaluate_window: does it need parameter "piece"?
#   -> evaluate_window: does it need parameter "window_length"?
#   -> evaluate_window: change name because it sucks...
#   -> minimax: check if this function needs to return tuple. Looks like first
#      parameter from it is always ignored


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
        open_columns = self._board.get_valid_locations()
        best_score = -inf
        best_column = random.choice(open_columns)
        print("Next move evaluation")
        for col in open_columns:
            temp_board = copy.deepcopy(self._board)
            temp_board.drop_piece_in(col, AI)
            score = temp_board.evaluate_window(WINDOW_LENGTH, AI,
                                               SimpleLogicAI.evalute_window)
            print(f"Temp. piece at {row}, {col} = {score}")
            temp_board.print_board_not_flipped()
            if score > best_score:
                best_score = score
                best_column = col
        return best_column

    @staticmethod
    def evalute_window(window, piece, isCenter=False) -> int:
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
                np.count_nonzero(window == 0) == 1):
            score += 10
        elif (np.count_nonzero(window == piece) == 2 and
                np.count_nonzero(window == 0) == 2):
            score += 5
        else:
            pass

        if (np.count_nonzero(window == oponent) == 3 and
                np.count_nonzero(window == 0) == 1):
            score -= 80

        if isCenter:
            score += 6 * np.count_nonzero(window == piece)

        return score


class MinMaxAI:
    """
    AI that uses MinMax algorithm to calculate best move
    """
    def __init__(self, board):
        self._board = board

    def get_next_move(self) -> int:
        """
        Returns AI's next move. Next move is calculated using MinMax algorithm
        """
        pass

    @staticmethod
    def evaluate_window(self, window, piece) -> int:
        """
        Evaluates score for given window and piece
        """
        pass
