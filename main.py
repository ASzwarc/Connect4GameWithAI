import GameController
import pygame

# TODO Create AI interface and child classes with different AI logic

if __name__ == '__main__':
    pygame.init()
    game = GameController.GameController()
    game.main_game_loop()
