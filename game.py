import pygame
import sys
from fighter import Fighter
from alien import Alien
from rocket import Rocket
from const_game import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_FILL_COLOR, GAME_CAPTION


class Game:
    def __init__(self):
        pygame.display.set_caption(GAME_CAPTION)
        self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen_color = SCREEN_FILL_COLOR
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.game_font = pygame.font.Font(None, 25)
        self.game_score = 0

        self.fighter = Fighter()
        self.alien = Alien()
        self.rocket = Rocket(self.fighter)

        self.game_is_running = True


    def game_run(self):
        while self.game_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.game_mechanics(event)

            self.game_update()
            self.game_draw_screen()

        self.game_over()


    def game_mechanics(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.fighter.move_left()
            if event.key == pygame.K_RIGHT:
                self.fighter.move_right()
            if event.key == pygame.K_SPACE:
                self.rocket.move_fire()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                self.fighter.move_stop()


    def game_update(self):
        self.fighter.move_update()
        self.alien.move_update()
        self.rocket.move_update()

        if self.rocket.is_out_of_screen():
            self.rocket.move_reset()

        if self.rocket.is_explode(self.alien):
            self.alien.move_reset()
            self.rocket.move_reset()
            self.game_score += 1

        if self.alien.move_reached_fighter(self.fighter):
            self.game_is_running = False


    def game_draw_screen(self):
        self.screen.fill(self.screen_color)
        self.screen.blit(self.fighter.image, (self.fighter.x, self.fighter.y))
        self.screen.blit(self.alien.image, (self.alien.x, self.alien.y))
        if self.rocket.was_fired:
            self.screen.blit(self.rocket.image, (self.rocket.x, self.rocket.y))
        self.game_show_score()
        pygame.display.update()


    def game_show_score(self):
        game_score_text = self.game_font.render(f"Your score: {self.game_score}", True, 'black')
        self.screen.blit(game_score_text, (20, 20))


    def game_over(self):
        game_over_text = self.game_font.render("Game Over", True, 'black')
        game_over_rectangle = game_over_text.get_rect()
        game_over_rectangle.center = (self.screen_width / 2, self.screen_height / 2)
        self.screen.blit(game_over_text, game_over_rectangle)
        pygame.display.update()
        pygame.time.wait(2000)