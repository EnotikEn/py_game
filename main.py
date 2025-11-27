import pygame
from game import Game


pygame.init()

run_game = Game()
run_game.game_run()

pygame.quit()