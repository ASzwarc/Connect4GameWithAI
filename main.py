import GameController
import pygame
import numpy as np


if __name__ == '__main__':
    pygame.init()
    game = GameController.GameController()
    game.main_game_loop()
