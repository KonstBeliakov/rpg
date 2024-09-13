from itertools import chain
from random import randrange

from entity import Entity
from monsters import *
from shop import Shop
from utils import *
from player import Player
from map import Map


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.over = False

        self.player = Player(self)
        self.entities = [Slime(self) for _ in range(10)] + [Goblin(self) for _ in range(5)] + [Shop(self)]
        for entity in self.entities:
            entity.pos = (randrange(WINDOW_WIDTH), randrange(WINDOW_HEIGHT))

        self.bullets = []
        self.droped_items = []
        self.events = []

        self.map = Map(self)

    @staticmethod
    def delete_not_active(lst: list[Entity]):
        for i in range(len(lst) - 1, -1, -1):
            if not lst[i].active:
                del lst[i]

    def update(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.over = True
        self.screen.fill((255, 255, 255))

        self.map.draw(self.screen)

        for entity in chain(self.entities, self.bullets, self.droped_items):
            entity.update()
            entity.draw(self.screen)

        for i in self.entities, self.bullets, self.droped_items:
            self.delete_not_active(i)

        self.player.controls(self)
        self.player.update()
        self.player.draw(self.screen)

        if not self.player.alive:
            self.over = True
