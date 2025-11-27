import sys
import pygame
# from random import randint

# clock = pygame.time.Clock()

pygame.init()

screen_width, screen_height = 800, 600
rect_width, rect_height = 100, 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height /2 - rect_height / 2
rect_color = pygame.Color('orange')
fill_color = pygame.Color('grey')

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Rectangle game")

STEP = 10

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and rect_y >= STEP:
                    rect_y -= STEP
                if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                    rect_y += STEP
                if event.key == pygame.K_LEFT and rect_x >= STEP:
                    rect_x -= STEP
                if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width -STEP:
                    rect_x += STEP

    screen.fill(fill_color)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    # screen.fill((randint(0, 255), randint(0,255), randint(0,255)))
    pygame.display.update()

    # clock.tick(1)
