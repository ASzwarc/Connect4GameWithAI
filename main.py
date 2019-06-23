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
            pygame.draw.circle(
                screen,
                const.BLACK,
                (int(column*const.SQUARE_SIZE + const.SQUARE_SIZE / 2),
                    int(const.MESSAGE_PROMPT_SIZE +
                        row*const.SQUARE_SIZE +
                        const.SQUARE_SIZE/2)),
                const.RADIUS, 0)

    pygame.display.update()


if __name__ == '__main__':
    board = Board.Board()

    pygame.init()
    screen_size = (const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    myfont = pygame.font.SysFont("monospace", 75)

    draw_board(board.board)

    end_game = False

    while not end_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True

        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()
