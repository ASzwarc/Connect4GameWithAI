"""
Class responsible for controlling whole game.
"""

import Board
import View
import AI
import pygame
import constants as const
import math


class GameController:

    def __init__(self):
        self._board = Board.Board()
        self._view = View.View()
        self._ai = AI.MinMaxAI(self._board)
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

    def evaluate_users_input(self, end_game) -> bool:
        """
        Evaluates user input and draws on screen
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True

            elif event.type == pygame.MOUSEMOTION:
                pos_x = event.pos[0]
                self._view.draw_piece_in_prompt(const.RED, pos_x)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._view.clear_prompt_screen()
                column = int(math.floor(
                            event.pos[0]) / const.CIRCLE_DIAMETER)

                if self._board.is_empty_slot_in(column):
                    row = self._board.get_open_row(column)
                    self._board.drop_piece(row, column, const.HUMAN)

                    if self._board.is_move_winning(const.HUMAN):
                        self._view.display_winning_message(
                            const.HUMAN, const.RED)
                        end_game = True

                    self._turn += 1
                self._view.draw_board(self._board)
            else:
                pass
        return end_game

    def evaluate_ai_action(self, end_game) -> bool:
        """
        Evaluates ai input and draws on screen
        """
        column = self._ai.get_next_move()
        self._view.draw_piece_in_prompt(const.YELLOW,
                                        self._view.get_pos_x_from(
                                            column))
        row = self._board.get_open_row(column)
        pygame.time.wait(500)
        self._board.drop_piece(row, column, const.AI)
        self._view.clear_prompt_screen()
        if self._board.is_move_winning(const.AI):
            self._view.display_winning_message(const.AI, const.YELLOW)
            end_game = True
        self._turn += 1
        self._view.draw_board(self._board)
        return end_game

    def main_game_loop(self):
        """
        Function that runs main game loop
        """
        end_game = False
        while not end_game:

            if self.get_player_no() == const.HUMAN:
                end_game = self.evaluate_users_input(end_game)
            # AI turn
            else:
                end_game = self.evaluate_ai_action(end_game)
                self._board.print_board_not_flipped()
            self._view.display_flip()

        pygame.time.wait(const.MS_BEFORE_EXIT)
        # Be IDLE friendly
        pygame.quit()
