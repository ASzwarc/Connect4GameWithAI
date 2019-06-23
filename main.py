import pygame
import sys
import Board

if __name__ == '__main__':
    board = Board.Board()
    board.print_board()
    for i in range(3):
        board.drop_piece(0, i, 2)
    board.print_board()
    board.is_move_winning(2)
    # for i in range(3):
    #     board.drop_piece(i, 3, 1)
    board.drop_piece(2, 3, 1)
    board.drop_piece(1, 2, 1)
    board.drop_piece(3, 4, 1)
    board.print_board()
    board.is_move_winning(1)
