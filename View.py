"""
Definiton of class View that's responsible for all the drawing
"""

import constants as const
import pygame
import sys


class View:

    def __init__(self):
        self._screen = pygame.display.set_mode((const.SCREEN_WIDTH,
                                               const.SCREEN_HEIGHT))
        self._myfont = pygame.font.SysFont(const.FONT_TYPE, const.FONT_SIZE)

        pygame.font.init()

    def draw_board(self, board):
        """
        Draws empty board on screen
        """
        pygame.draw.rect(self._screen, const.BLUE,
                         (0, const.MESSAGE_PROMPT_SIZE,
                          const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

        for column in range(board.columns):
            for row in range(board.rows):
                position = (int(column*const.CIRCLE_DIAMETER +
                                const.CIRCLE_DIAMETER / 2),
                            int(const.SCREEN_HEIGHT -
                                row*const.CIRCLE_DIAMETER -
                                const.CIRCLE_DIAMETER/2))
                color = const.BLACK
                if board.board[row, column] == 1:
                    color = const.RED
                elif board.board[row, column] == 2:
                    color = const.YELLOW

                pygame.draw.circle(self._screen, color, position,
                                   const.RADIUS, 0)
        pygame.display.update()

    def display_winning_message(self, player_no, color):
        """
        Display message with information which player has won
        """
        message = self._myfont.render(
            f"Player {player_no} wins !!!", True, color)
        self._screen.blit(message, (40, 10))
        pygame.display.update()

    def draw_piece_in_prompt(self, color, pos_x):
        """
        Draws piece (color depends on which players turn is it)
        in prompt screen (above board) in given x position
        """
        # clear the prompt from previously drawn piece
        pygame.draw.rect(self._screen, const.BLACK,
                         (0, 0, const.SCREEN_WIDTH, const.MESSAGE_PROMPT_SIZE))
        # draw new piece
        pygame.draw.circle(self._screen, color,
                           (pos_x, int(const.CIRCLE_DIAMETER / 2)),
                           int(const.CIRCLE_DIAMETER/2))
        pygame.display.update()

    def clear_prompt_screen(self):
        """
        Clears prompt screen from pieces (only black background)
        """
        pygame.draw.rect(self._screen, const.BLACK,
                         (0, 0, const.SCREEN_WIDTH, const.MESSAGE_PROMPT_SIZE))
        pygame.display.update()

    def display_flip(self):
        """
        Calls pygame.display.flip()
        """
        pygame.display.flip()
