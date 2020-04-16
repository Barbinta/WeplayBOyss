import pygame
from pygame.locals import *

WIDTH=800
HEIGHT=400

MOVESPEED = 0.1
white = (255, 255, 255)
black = (0, 0, 0)
blue  = (0, 51, 153)


class GameObject:
    def __init__(self, game, position):
        self.game=game
        self.postion = position 
        self.velocity = [ 0, 0 ]

    def input (self):
        pass

    def update (self):
        pass

    def draw (self):
        pass

class player(GameObject):

    def input(self, event):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_w :
                    self.velocity[0] = -MOVESPEED
                if event.key == K_s :
                    self.velocity[0] = MOVESPEED
            if event.type == KEYUP :
                if event.key == K_w :
                    self.velocity[1] = 0
                if event.key == K_s :
                    self.velocity[1] = 0

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self):
        pygame.draw.rect ( self.game.window, white,  )   

class Game:

    def __init__(self):
        self.window = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption('Game')
        pygame.time.Clock().tick(60) 

    def run(self):
        while True:

            self.input()
            self.update()
            self.draw()

    def input(self):

        events = pygame.event.get()

        for GameObject in self.gameObjects:
            GameObject.input(events)

    def update(self):
        for GameObject in self.gameObjects:
            GameObject.update()


    def draw(self):
        self.window.fill(BLACK)

        for GameObject in self.GameObjects:
            GameObject.draw()

        pygame.display.update()


def main():

    game = Game()
    game.run()

if __name__ == '__main__':
    main() 