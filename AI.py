"""
File containig different oponents AI classes
"""
import random
import numpy as np
from math import inf
import Board
from constants import COLUMN_COUNT, AI, HUMAN, WINDOW_LENGTH, MINIMAX_DEPTH
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

    def evaluate_stop_condition(self, board, depth, is_terminal):
        """
        Evaluates score after stop condition have been reached.
        """
        some_big_score = 1000000
        if is_terminal:
            if board.is_move_winning(AI):
                return (None, some_big_score)
            elif board.is_move_winning(HUMAN):
                return (None, -some_big_score)
            else:  # no more moves
                return (None, 0)
        else:  # depth is zero
            return (None, board.evaluate_window(WINDOW_LENGTH, AI,
                                                MinMaxAI.evalute_window))

    def minimax(self, board: Board, depth: int=MINIMAX_DEPTH,
                maximizingPlayer: bool):
        """
        Minimax algorithm loop

        Args:
            board (Board): Temporary board which will be evaluated
            depth (int): How many moves algorithm should look-ahead,
            default is 4
            maximizingPlayer (bool): If it's player whom score should be maxed

        Returns:
            Tuple(column (int), score(int)): column with best score
        """
        # stop condition
        is_terminal = board.is_terminal()
        if depth = 0 or is_terminal:
            return self.evaluate_stop_condition(board, depth, is_terminal)
        if maximizingPlayer:  # AI
            value = -inf
            best_col = -10
            columns = board.get_valid_locations()
            for col in columns:
                temp_board = copy.deepcopy(board)
                temp_board.drop_piece_in(col, AI)
                score = minimax(temp_board, depth - 1, False)[1]
                if score > value:
                    value = score
                    best_col = col
            return (best_col, value)
        else:  # player
            value = inf
            best_col = -10
            columns = Board.get_valid_locations()
            for col in columns:
                temp_board = copy.deepcopy(board)
                temp_board.drop_piece_in(col, HUMAN)
                score = minimax(temp_board, depth - 1, True)[1]
                if score < value:
                    value = score
                    best_col = col
            return (best_col, value)

    def get_next_move(self) -> int:
        """
        Returns AI's next move. Next move is calculated using MinMax algorithm
        """
        temp_board = copy.deepcopy(self._board)
        result = self.minimax(temp_board, MINIMAX_DEPTH, True)
        print(f"Best result {result[1]} for {result[0]} column")

    @staticmethod
    def evaluate_window(self, window, piece) -> int:
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
