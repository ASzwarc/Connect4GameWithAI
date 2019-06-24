"""
Definiton of class View that's responsible for all the drawing
"""

import constants as const
import pygame


class View:

    def __init__(self, screen):
        self.__screen = screen
        self.__myfont = pygame.font.SysFont("monospace", const.FONT_SIZE)

        pygame.font.init()

    def draw_board(self, board):
        """
        Draws empty board on screen
        """
        pygame.draw.rect(
            self.__screen,
            const.BLUE,
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

                pygame.draw.circle(
                    self.__screen,
                    color,
                    position,
                    const.RADIUS, 0)

        pygame.display.update()

    def display_winning_message(self, player_no, color):
        """
        Display message with information which player has won
        """
        message = self.__myfont.render(
            "Player {} wins !!!".format(player_no),
            True,
            color)
        self.__screen.blit(message, (40, 10))
        pygame.display.update()
