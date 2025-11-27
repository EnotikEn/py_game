from random import randint
import pygame
import sys
from pathlib import Path


pygame.init()

game_font = pygame.font.Font(None, 30)

fighter_path = Path("images/ship_resized.png")
rocket_path = Path("images/rocket_resized.png")
alien_path = Path("images/alien_resized.png")

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
color_fill = pygame.Color('grey')
pygame.display.set_caption("Shooter game")

F_STEP = 0.1

fighter_image = pygame.image.load(fighter_path)
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height
fighter_move_left, fighter_move_right = False, False

R_STEP = 0.3

rocket_image = pygame.image.load(rocket_path)
rocket_width, rocket_height = rocket_image.get_size()
rocket_x, rocket_y = None, None
rocket_was_fired = False

A_STEP = 0.05

alien_image = pygame.image.load(alien_path)
alien_width, alien_height = alien_image.get_size()
alien_x, alien_y = randint(0, screen_width - alien_width), 0

game_is_running = True
game_score = 0

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_move_left = True
            if event.key == pygame.K_RIGHT:
                fighter_move_right = True
            if event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
                rocket_y = fighter_y - rocket_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_move_left = False
            if event.key == pygame.K_RIGHT:
                fighter_move_right = False

    if fighter_move_left and fighter_x >= F_STEP:
        fighter_x -= F_STEP

    if fighter_move_right and fighter_x <= screen_width - fighter_width - F_STEP:
        fighter_x += F_STEP

    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False

    alien_y += A_STEP

    if rocket_was_fired:
        rocket_y -= R_STEP

    screen.fill(color_fill)
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))

    if rocket_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    game_score_text = game_font.render(f"Your score is: {game_score}", True, "black")
    screen.blit(game_score_text, (20, 20))

    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        game_is_running = False

    if (rocket_was_fired and
            alien_x < rocket_x < alien_x + alien_width - rocket_width and
            alien_y < rocket_y < alien_y + alien_height - rocket_height):
        rocket_was_fired = False
        alien_x = randint(0, screen_width - alien_width)
        alien_y = 0
        game_score += 1

game_over_text = game_font.render("Game Over", True, 'black')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()
