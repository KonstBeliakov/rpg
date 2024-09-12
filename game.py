import pygame
from random import randrange

from utils import *
from alive import Alive
from entity import Entity
from player import Player

WIDTH, HEIGHT = 800, 600


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.over = False

        self.player = Player()
        self.entities = [Alive(50, team=ENEMY) for _ in range(10)]
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

        for i in range(len(self.entities) - 1, -1, -1):
            if isinstance(self.entities[i], Alive) and not self.entities[i].alive:
                del self.entities[i]

        for bullet in self.bullets:
            bullet.update(self)
            bullet.draw(self.screen)

        for i in range(len(self.bullets) - 1, -1, -1):
            if not self.bullets[i].active:
                del self.bullets[i]

        self.player.controls(self)
        self.player.update(self)
        self.player.draw(self.screen)

        if not self.player.alive:
            self.over = True
