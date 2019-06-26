"""
Class responsible for controlling whole game.
"""

import Board
import View
import pygame
import constants as const
import math


class GameController:

    def __init__(self):
        self._board = Board.Board()
        self._view = View.View()
        self._turn = 0

        self._view.draw_board(self._board)

    def get_color(self):
        """
        Evaluates, based on turn number, which player's move it is
        and returns proper color of piece
        """
        if self.get_player_no() == 1:
            return const.RED
        else:
            return const.YELLOW

    def get_player_no(self) -> int:
        """
        Returns player number
        """
        return (self._turn % 2) + 1

    def main_game_loop(self):
        """
        Function that runs main game loop
        """
        # TODO Refactor main loop so it's using AI code as second player
        end_game = False
        while not end_game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_game = True

                elif event.type == pygame.MOUSEMOTION:
                    pos_x = event.pos[0]
                    self._view.draw_piece_in_prompt(self.get_color(), pos_x)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._view.clear_prompt_screen()
                    column = int(math.floor(
                        event.pos[0]) / const.CIRCLE_DIAMETER)

                    if self._board.is_empty_slot_in(column):
                        row = self._board.get_open_row(column)
                        self._board.drop_piece(row, column,
                                               self.get_player_no())

                        if self._board.is_move_winning(self.get_player_no()):

                            self._view.display_winning_message(
                                self.get_player_no(), self.get_color())
                            end_game = True

                        self._turn += 1
                    self._view.draw_board(self._board)

            self._view.display_flip()

        pygame.time.wait(const.MS_BEFORE_EXIT)
        # Be IDLE friendly
        pygame.quit()
