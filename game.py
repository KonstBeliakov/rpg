import pygame
from random import randrange

from entity import Entity
from player import Player

WIDTH, HEIGHT = 800, 600


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.over = False

        self.player = Player()
        self.entities = [Entity() for _ in range(10)]
        for entity in self.entities:
            entity.pos = (randrange(WIDTH), randrange(HEIGHT))

        self.bullets = []

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.over = True
        self.screen.fill((255, 255, 255))

        for entity in self.entities:
            entity.draw(self.screen)

        for bullet in self.bullets:
            bullet.update(self)
            bullet.draw(self.screen)

        self.player.controls(self)
        self.player.update(self)
        self.player.draw(self.screen)

        if not self.player.alive:
            self.over = True
