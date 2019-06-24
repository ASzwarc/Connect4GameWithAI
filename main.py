import pygame
import sys
import Board
import View
import constants as const
import math


if __name__ == '__main__':
    board = Board.Board()

    pygame.init()
    pygame.font.init()
    screen_size = (const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    myfont = pygame.font.SysFont("monospace", const.FONT_SIZE)

    view = View.View(screen)
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
                # clear the prompt from previously drawn piece
                pygame.draw.rect(
                    screen,
                    const.BLACK,
                    (0, 0, const.SCREEN_WIDTH, const.MESSAGE_PROMPT_SIZE))
                # draw new piece
                pygame.draw.circle(
                    screen,
                    color,
                    (event.pos[0], int(const.CIRCLE_DIAMETER / 2)),
                    int(const.CIRCLE_DIAMETER/2))
                pygame.display.update()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(
                    screen,
                    const.BLACK,
                    (0, 0, const.SCREEN_WIDTH, const.MESSAGE_PROMPT_SIZE))
                column = int(math.floor(event.pos[0]) / const.CIRCLE_DIAMETER)
                if board.is_empty_slot_in(column):
                    row = board.get_open_row(column)
                    board.drop_piece(row, column, player)

                    if board.is_move_winning(player):
                        message = myfont.render(
                            "Player {} wins !!!".format(player),
                            True,
                            color)
                        screen.blit(message, (40, 10))
                        pygame.display.update()
                        end_game = True
                view.draw_board(board)
                turn += 1
        pygame.display.flip()

    pygame.time.wait(const.MS_BEFORE_EXIT)
    # Be IDLE friendly
    pygame.quit()
