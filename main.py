import numpy as np
import pygame
import sys

import constants


def create_board():
    """
    Creates empty board initialized with zeros
    """
    return np.zeros((constants.ROW_COUNT, constants.COLUMN_COUNT), np.int8)

def print_board(board):
    """
    Prints board to standard output
    """
    print(board)

if __name__ == '__main__':
    print_board(create_board())
