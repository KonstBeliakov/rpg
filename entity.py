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
    def pos(self, pos):
        self.x, self.y = pos

    @property
    def center(self):
        return self.x + self.sizeX // 2, self.y + self.sizeY // 2

    @property
    def size(self):
        return self.sizeX, self.sizeY

    @size.setter
    def size(self, new_size):
        self.sizeX, self.sizeY = new_size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))

    def update(self):
        pass
