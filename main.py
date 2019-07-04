import GameController
import pygame
import numpy as np


if __name__ == '__main__':
    matrix = np.matrix([[2,  2,  3,  4,  5,  6,  7],
                        [2,  9,  10, 11, 12, 13, 14],
                        [0, 16, 17, 18, 19, 20, 21],
                        [0,  2,  3,  4,  5,  6,  7],
                        [0,  9,  10, 11, 12, 13, 14],
                        [0, 16, 17, 18, 19, 20, 21]])
    # print(matrix)
    # print(np.array(matrix[:, 0]).flatten())
    # print("Line break")
    # for row in range(6 - 3):
    #     for column in range(7 - 3):
    #         array = np.array(matrix[row:row+4, column:column+4].diagonal(0)).flatten()
    #         print(f"{row}, {column} : {array}")

    # print("another line break")
    # for row in range(6):
    #     array = np.array(matrix[row, :]).flatten()
    #     for column in range(7 - 4):
    #         print(f"{row}, {column} : {array[column:column + 4]}")

    pygame.init()
    game = GameController.GameController()
    game.main_game_loop()
