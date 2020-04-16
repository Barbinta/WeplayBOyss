import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('BarBy')
icon = pygame.image.load('pizza.png')
pygame.display.set_icon(icon)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((102, 153, 0))   
    pygame.display.update()     