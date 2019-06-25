import GameController
import pygame

if __name__ == '__main__':
    pygame.init()
    game = GameController.GameController()
    game.main_game_loop()
