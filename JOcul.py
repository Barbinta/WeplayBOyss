import random
import pygame
import math
from pygame.locals import *

A = 2
B = False
C = True

movepx = 0
movepy = 0

movebx = 0
moveby = 0

movegy = 0.5

px = 368
py = 400

gx = px
gy = 400

mx = random.randint(32, 768) 
my = random.randint(32, 568)

bx = random.randint(32, 768)
by = random.randint(32, 168)



screen = pygame.display.set_mode((800, 600))

bimg = pygame.image.load ( 'fat.png' )
pimg = pygame.image.load ( 'eat.png' )
ming = pygame.image.load ( 'cookie.png' )

def coll(plx, ply, mnx, mny):
    distance = math.sqrt(( math.pow( plx - mnx, 2 ) ) + math.pow( ply - mny, 2 ) )
    if distance < 36:
        return True
        
def boss(x, y):
    screen.blit(bimg, ( x, y ))

def player(x, y):
    screen.blit(pimg, ( x, y ))

def manc(x, y):
    screen.blit(ming, ( x, y ))

def shoot(x, y):
    global B 
    B = True
    screen.blit(ming, ( x+16, y ))


pygame.display.set_caption('BarBy')
icon = pygame.image.load('pizza.png')
pygame.display.set_icon(icon)


running = True
while running:
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if A == 0 and B == False:
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    gx = px
                    shoot( gx, gy )

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                movepx -= 0.3
            if event.key == K_RIGHT:
                movepx =+ 0.3
            if A != 0:
                if event.key == K_UP:
                    movepy -= 0.3
            if A != 0:
                if event.key == K_DOWN:
                    movepy += 0.3
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                movepx = 0
            if event.key == K_UP or event.key == K_DOWN:
                movepy = 0
        
            
            
    px += movepx
    py += movepy 

    if A == 0:
        screen.fill((255, 255, 0))
        boss( bx, by )
        
        if B == True:
            shoot( gx, gy )
            gy -= movegy
        if C :
            C = False
            px = 368
            py = 400
        if gy == 0:
            B = False
            gy = 400
        if coll(gx, gy, bx, by):
            B = False
            gy = 400
             

        

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

        
         
    player(px, py)
    pygame.display.update()     