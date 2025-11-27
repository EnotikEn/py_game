import pygame
from const_game import ROCKET_STEP
from pathlib import Path


rocket_path = Path("images/rocket_resized.png")


class Rocket:
    def __init__(self, fighter):
        self.image = pygame.image.load(rocket_path)
        self.width, self.height = self.image.get_size()
        self.x, self.y = 0, 0
        self.step = ROCKET_STEP
        self.was_fired = False
        self.fighter = fighter


    def move_fire(self):
        self.was_fired = True
        self.x = self.fighter.x + self.fighter.width / 2 - self.width / 2
        self.y = self.fighter.y - self.height


    def move_update(self):
        if self.was_fired:
            self.y -= self.step


    def is_out_of_screen(self):
        return self.y + self.height < 0


    def move_reset(self):
        self.was_fired = False


    def is_explode(self, alien):
        return (
            alien.x < self.x < alien.x + alien.width - self.width and
            alien.y < self.y < alien.y + alien.height - self.height
        )



