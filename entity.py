import random

import pygame


class Entity:
    def __init__(self, pos=(0, 0)):
        self.pos = pos

        self.sizeX = 50
        self.sizeY = 50

        self.color = 'black'

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, new_pos):
        self.x, self.y = new_pos

    @property
    def size(self):
        return self.sizeX, self.sizeY

    @size.setter
    def size(self, new_size):
        self.sizeX, self.sizeY = new_size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))
