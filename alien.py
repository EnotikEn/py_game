import pygame
from pathlib import Path
from const_game import SCREEN_WIDTH, ALIEN_STEP
from random import randint


alien_path = Path("images/alien_resized.png")


class Alien:
    def __init__(self):
        self.image = pygame.image.load(alien_path)
        self.width, self.height = self.image.get_size()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0
        self.step = ALIEN_STEP
        self.speed = self.step


    def move_update(self):
        self.y += self.speed


    def move_increase(self):
        self.speed += self.step / 2


    def move_reset(self):
        self.move_increase()
        self.x = randint(0, SCREEN_WIDTH - self.width)
        self.y = 0


    def move_reached_fighter(self, fighter):
        return self.y + self.height > fighter.y



