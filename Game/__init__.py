import sys
import pygame

pygame.init()

size = width, height = 720, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

background = pygame.image.load("../Resources/Images/space.PNG")
backgroundRect = background.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(background, backgroundRect)
    pygame.display.flip()