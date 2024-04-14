import pygame
import random
import math
import os
from pygame import mixer

pygame.init()
mixer.init()

# Load an image and scale it to fit the screen
def load_image(img, SCREEN):
    size_img = img.get_size()
    scale = min(
        SCREEN.get_width() / size_img[0], SCREEN.get_height() / size_img[1]
    )
    return pygame.transform.scale(
        img, (round(size_img[0] * scale), round(size_img[1] * scale))
    )

# load images
backdrop_img = pygame.image.load(os.path.join("assets", "backgrounds", "backdrop.svg"))
title_img = pygame.image.load(os.path.join("assets", "buttons", "title.svg"))
play_img = pygame.image.load(os.path.join("assets", "buttons", "play.svg"))
arrow_img = pygame.image.load(os.path.join("assets", "buttons", "arrow.svg"))

# screen sizing
SCALE = 2
WIDTH = backdrop_img.get_width() * SCALE
HEIGHT = backdrop_img.get_height() * SCALE

# screen setup
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HOT CHOCOLATE v0.1 || A WARM AND FUZZY GAME")


# lets re-load backdrop image scaled to screen
backdrop_img = load_image(backdrop_img, SCREEN)


def title():
    run = True

    while run:
        # loop through all events
        for event in pygame.event.get():

            # if QUIT/X button pressed...
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        # draw screen

        SCREEN.blit(backdrop_img, (0, 0))
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

        # check if play button pressed


        # update
        pygame.display.update()


# run game
if __name__ == "__main__":
    title()
