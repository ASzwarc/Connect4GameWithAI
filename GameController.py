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
        self.__board = Board.Board()
        self.__view = View.View()
        self.__turn = 0

        self.__view.draw_board(self.__board)

    def __get_color(self):
        """
        Evaluates, based on turn number, which player's move it is
        and returns proper color of piece
        """
        if self.__get_player_no() == 1:
            return const.RED
        else:
            return const.YELLOW

    def __get_player_no(self) -> int:
        """
        Returns player number
        """
        return (self.__turn % 2) + 1

    def main_game_loop(self):
        """
        Function that runs main game loop
        """
        end_game = False
        while not end_game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_game = True

                elif event.type == pygame.MOUSEMOTION:
                    pos_x = event.pos[0]
                    self.__view.draw_piece_in_prompt(self.__get_color(), pos_x)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__view.clear_prompt_screen()
                    column = int(math.floor(
                        event.pos[0]) / const.CIRCLE_DIAMETER)

                    if self.__board.is_empty_slot_in(column):
                        row = self.__board.get_open_row(column)
                        self.__board.drop_piece(row, column,
                                                self.__get_player_no())

                        if self.__board.is_move_winning(
                                self.__get_player_no()):

                            self.__view.display_winning_message(
                                self.__get_player_no(), self.__get_color())
                            end_game = True

                    self.__view.draw_board(self.__board)
                    self.__turn += 1

            self.__view.display_flip()

        pygame.time.wait(const.MS_BEFORE_EXIT)
        # Be IDLE friendly
        pygame.quit()
