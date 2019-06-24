import pygame
import sys
import Board
import View
import constants as const
import math


if __name__ == '__main__':
    board = Board.Board()

    pygame.init()

    view = View.View()
    view.draw_board(board)

    end_game = False
    turn = 0

    while not end_game:
        player = (turn % 2) + 1
        if player == 1:
            color = const.RED
        else:
            color = const.YELLOW

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True

            elif event.type == pygame.MOUSEMOTION:
                pos_x = event.pos[0]
                view.draw_piece_in_prompt(color, pos_x)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                view.clear_prompt_screen()
                column = int(math.floor(event.pos[0]) / const.CIRCLE_DIAMETER)
                if board.is_empty_slot_in(column):
                    row = board.get_open_row(column)
                    board.drop_piece(row, column, player)

                    if board.is_move_winning(player):
                        view.display_winning_message(player, color)
                        end_game = True
                view.draw_board(board)
                turn += 1
        pygame.display.flip()

    pygame.time.wait(const.MS_BEFORE_EXIT)
    # Be IDLE friendly
    pygame.quit()
