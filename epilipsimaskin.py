import pygame
from time import sleep
import random 
i= 0
b = (0, 0, 0)
w = (255, 255, 255)
pygame.init()
size = width, height = 320, 240
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
larger_font = pygame.font.SysFont("comic sans", 1000) # set font
large_font = pygame.font.SysFont("comic sans", 500) # set font
black = larger_font.render("total", True, b)
white = larger_font.render("total", True, w)
clock = pygame.time.Clock() # define clock
pygame.mouse.set_visible(False) # disable mouse

while 1:
    w = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    b = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    black = large_font.render("Relaxation", True, b)
    if (i < 1*60):
        black = larger_font.render("total", True, b)
 
    if i >= 2*60:
        black = larger_font.render("", True, b)

    screen.fill((w))
    screen.blit(black, (960 - black.get_width() // 2, 540 - black.get_height() // 2))
    pygame.display.flip()

    clock.tick(60)
    i = i + 1
    