import random
import pygame
import math
from pygame.locals import *

A = 5
movex = 0
movey = 0
px = 480
py = 200
mx = random.randint(32, 768) 
my = random.randint(32, 568)
bx = random.randint(32, 768)
by = random.randint(32, 768)

screen = pygame.display.set_mode((800, 600))

bimg = pygame.image.load ( 'fat.png' )
pimg = pygame.image.load ( 'eat.png' )
ming = pygame.image.load ( 'cookie.png' )

def coll(plx, ply, mnx, mny):
    distance = math.sqrt(( math.pow( plx - mnx, 2 ) ) + math.pow( ply - mny, 2 ) )
    if distance < 32:
        return True
        
def boss(x, y):
    screen.blit(bimg, ( x, y ))

def player(x, y):
    screen.blit(pimg, ( x, y ))

def manc(x, y):
    screen.blit(ming, ( x, y ))

pygame.display.set_caption('BarBy')
icon = pygame.image.load('pizza.png')
pygame.display.set_icon(icon)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                movex -= 0.3
            if event.key == K_RIGHT:
                movex =+ 0.3
            if event.key == K_UP:
                movey -= 0.3
            if event.key == K_DOWN:
                movey += 0.3
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                movex = 0
            if event.key == K_UP or event.key == K_DOWN:
                movey = 0   
         
    px += movex
    py += movey   

    if px <= 0:
        px = 0 
    elif px >= 736:
        px = 736      
    if py <= 0:
        py = 0 
    elif py >= 536:
        py = 536        

     
    if A != 0:
        screen.fill((102, 153, 0))
        manc(mx, my)
        if coll(px, py, mx, my):
            mx = random.randint(32, 768) 
            my = random.randint(32, 568)
            A -= 1

    if A == 0:
        screen.fill((255, 255, 0))
        boss(bx, by)
        

    
    player(px, py)
    pygame.display.update()     