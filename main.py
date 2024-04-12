import pygame
import random
import math
import os
from pygame import mixer

pygame.init()
mixer.init()

# imgs
title_img = pygame.image.load(os.path.join("assets", "buttons", "title.svg"))
play_img = pygame.image.load(os.path.join("assets", "buttons", "play.svg"))
arrow_img = pygame.image.load(os.path.join("assets", "buttons", "arrow.svg"))

SCALE = 2

# lets build the backdrop image
backdrop = pygame.image.load(os.path.join("assets", "backgrounds", "backdrop.svg"))


WIDTH = backdrop.get_width() * SCALE
HEIGHT = backdrop.get_height() * SCALE

# screen setup
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HOT CHOCOLATE v0.1 || A WARM AND FUZZY GAME")

# scale backdrop to stretch to SCREEN
size_backdrop = backdrop.get_size()
scale = min(
    SCREEN.get_width() / size_backdrop[0], SCREEN.get_height() / size_backdrop[1]
)
backdrop = pygame.transform.scale(
    backdrop, (round(size_backdrop[0] * scale), round(size_backdrop[1] * scale))
)

# setup font

# functions


def title():
    run = True

    while run:
        # loop through all events
        for event in pygame.event.get():

            # if QUIT/X button pressed...
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # draw

        # SCREEN.fill((255, 255, 255))
        SCREEN.blit(backdrop, (0, 0))
        SCREEN.blit(title_img, (WIDTH / 2 - title_img.get_width() / 2, 0))
        SCREEN.blit(
            play_img,
            (
                WIDTH / 2 - play_img.get_width() / 2,
                HEIGHT / 2 - play_img.get_height() / 2,
            ),
        )

        SCREEN.blit(
            arrow_img,
            (
                WIDTH / 2 - arrow_img.get_width() / 2 - 100,
                HEIGHT / 2 - arrow_img.get_height() / 2 + 100,
            ),
        )

        # check if play

        # update
        pygame.display.update()


# run game
if __name__ == "__main__":
    title()
