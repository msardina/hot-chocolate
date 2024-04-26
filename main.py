import pygame
import random
import math
import os
import time
from pygame import mixer

pygame.init()
mixer.init()


# Load an image and scale it to fit the screen
def stretch_to_screen(img, SCREEN):
    size_img = img.get_size()
    scale = min(SCREEN.get_width() / size_img[0], SCREEN.get_height() / size_img[1])
    return pygame.transform.scale(
        img, (round(size_img[0] * scale), round(size_img[1] * scale))
    )


def scale_img(img, scale):
    return pygame.transform.scale(
        img, (img.get_width() * scale, img.get_height() * scale)
    )
def blit_centre(img, centerx, centery, SCREEN):
    newx = centerx - img.get_width() / 2
    newy = centery - img.get_height() / 2
    newpos = (newx, newy)
    SCREEN.blit(img, (newpos))
    
def center2topright(img, centerx, centery):
    newx = centerx - img.get_width() / 2
    newy = centery - img.get_height() / 2
    newpos = (newx, newy)
    return newpos

def get_rect(img, x, y, width, height):
    return pygame.Rect(center2topright(img, x, y)[0], center2topright(img, x, y)[1], width, height)

# load images
player_str = f"{random.randint(1, 7)}p.svg"
player_img = pygame.image.load(os.path.join("assets", "players", player_str))
backdrop_img = pygame.image.load(os.path.join("assets", "backgrounds", "backdrop.svg"))
title_img = pygame.image.load(os.path.join("assets", "buttons", "title.png"))
play_img = pygame.image.load(os.path.join("assets", "buttons", "play.png"))
arrow_img = pygame.image.load(os.path.join("assets", "buttons", "arrow.png"))
droplet_img = pygame.image.load(os.path.join("assets", "objects", "drop.svg"))

title_normal_img = scale_img(title_img, 0.5)
title_zoom_img = scale_img(title_img, 0.56)
arrow_normal_img = scale_img(arrow_img, 0.12)
arrow_zoom_img = scale_img(arrow_img, 0.14)
play_normal_img = scale_img(play_img, 0.21)
play_zoom_img = scale_img(play_img, 0.25)
player_img = scale_img(player_img, 1.3)
droplet_img = scale_img(droplet_img, 2)

#sfx and music loading
hover = pygame.mixer.Sound(os.path.join("sfx", "Hover.wav"))
back_sfx = pygame.mixer.Sound(os.path.join("sfx", "music.mp3"))
back_sfx.play(-1)

# screen sizing
SCALE = 2
WIDTH = backdrop_img.get_width() * SCALE
HEIGHT = backdrop_img.get_height() * SCALE

# screen setup
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HOT CHOCOLATE v0.1 || A WARM AND FUZZY GAME")


# lets re-load backdrop image scaled to screen
backdrop_img = stretch_to_screen(backdrop_img, SCREEN)

#clock
FPS = 60
clock = pygame.time.Clock()


#Setup Font
font = pygame.font.SysFont(None, 50)
title_font = pygame.font.SysFont(None, 100)

#class
class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = get_rect(self.img, self.x, self.y, self.width, self.height)
        
    def draw(self):
        blit_centre(self.img, self.x, self.y, SCREEN)
        
    def move(self):
        pos = pygame.mouse.get_pos()
        self.y = 75
        self.x = pos[0]
        self.rect = get_rect(self.img, self.x, self.y, self.width, self.height)
class Droplet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect = get_rect(self.img, self.x, self.y, self.width, self.height)
        self.collide = False
        
    def draw(self):
        blit_centre(self.img, self.x, self.y, SCREEN)

    def reset(self):
        self.y = HEIGHT - self.height
        self.x = random.randint(0, WIDTH)

    def move(self):
        self.y -= 5
        if self.y < 0:
            self.reset()
        self.rect = get_rect(self.img, self.x, self.y, self.width, self.height)
    

class Button:
    def __init__(self, x, y, img, img_zoom):
        self.pos = (x, y)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.img = img
        self.imgzoom = img_zoom
        self.useimg = self.img
        self.sound = False
        self.click = False
        self.rect = pygame.rect.Rect(self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2, self.img.get_width(), self.img.get_height())
        self.hover = False
        
    def draw(self):
        if self.hover:
            blit_centre(self.imgzoom, self.x, self.y, SCREEN)
            if self.sound == False:
                hover.play()
            self.sound = True
        else:
            blit_centre(self.img, self.x, self.y, SCREEN)
            self.sound = False
        # pygame.draw.rect(SCREEN, (0, 0, 0), self.rect)
        
    def update(self):
        pos = pygame.mouse.get_pos()
        
        self.hover = False
        if self.rect.collidepoint(pos):
            self.hover = True
            
        # if hovering, check if press
        if self.hover:            
            # left button clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False

    def is_clicked(self):
        return self.click
    
#objects
play_btn = Button(WIDTH / 2, HEIGHT / 2, play_normal_img, play_zoom_img)
title_btn = Button(WIDTH / 2, -10 + title_normal_img.get_height() / 2, title_normal_img, title_zoom_img)
arrow_btn = Button(WIDTH / 2 - 150, HEIGHT / 2 + 200 , arrow_normal_img, arrow_zoom_img)
player = Player(pygame.mouse.get_pos()[0], 20, player_img)
drop = Droplet(WIDTH / 2, HEIGHT, droplet_img)
buttons = [title_btn, play_btn, arrow_btn]

def title():
    title = True

    while title:
        # loop through all events
        for event in pygame.event.get():

            # if QUIT/X button pressed...
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # draw screen

        SCREEN.blit(backdrop_img, (0, 0))

        #loop through all buttons and update them and draw them.
        for btn in buttons:
            btn.update()
            btn.draw()

        if play_btn.is_clicked():
            title = False
            
        # update
        pygame.display.update()
        clock.tick(FPS)
        
def game():
    #clear screen
    SCREEN.fill('black')
    
    
    run = True
    score = 0
    timer = 0
    
    while run:
        # loop through all events
        for event in pygame.event.get():

            # if QUIT/X button pressed...
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #Render Text
        score_txt = title_font.render(f'{score}', True, (0, 0, 0))
        
        # draw screen

        SCREEN.blit(backdrop_img, (0, 0))
        player.draw()
        drop.draw()
        SCREEN.blit(score_txt, (0, 0))
        
        #move screen
        drop.move()
        player.move()
        
        #collisions
        if pygame.Rect.colliderect(drop.rect, player.rect):
            score += 50
            print(score)
            drop.reset()
            
        #change score
        if timer == 3:
            score += 1
            timer = 0
        # update
        pygame.display.update()
        clock.tick(FPS)
        timer += 0.50
# run game
if __name__ == "__main__":
    title()
    game()