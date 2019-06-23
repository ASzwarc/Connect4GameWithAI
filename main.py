import pygame
import sys
import Board
import constants as const


def draw_board(board):
    pygame.draw.rect(
        screen,
        const.BLUE,
        (0, const.MESSAGE_PROMPT_SIZE,
            const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

    for column in range(const.COLUMN_COUNT):
        for row in range(const.ROW_COUNT):
            position = (int(column*const.CIRCLE_DIAMETER +
                            const.CIRCLE_DIAMETER / 2),
                        int(const.SCREEN_HEIGHT -
                            row*const.CIRCLE_DIAMETER -
                            const.CIRCLE_DIAMETER/2))
            color = const.BLACK
            if board[row, column] == 1:
                color = const.RED
            elif board[row, column] == 2:
                color = const.YELLOW

            pygame.draw.circle(
                screen,
                color,
                position,
                const.RADIUS, 0)

    pygame.display.update()


if __name__ == '__main__':
    board = Board.Board()

    pygame.init()
    screen_size = (const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    myfont = pygame.font.SysFont("monospace", 75)

    board.drop_piece(0, 2, 1)
    board.drop_piece(1, 3, 2)

    draw_board(board.board)

    end_game = False

    while not end_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True

        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()
