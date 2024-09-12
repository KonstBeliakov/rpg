from itertools import chain
from random import randrange

from monsters import *
from utils import *
from alive import Alive
from player import Player


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.over = False

        self.player = Player()
        self.entities = [Slime(50, team=Team.ENEMY) for _ in range(10)]
        for entity in self.entities:
            entity.pos = (randrange(WINDOW_WIDTH), randrange(WINDOW_HEIGHT))

        self.bullets = []
        self.droped_items = []
        self.events = []

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

        for entity in chain(self.entities, self.bullets, self.droped_items):
            entity.update(self)
            entity.draw(self.screen)

        for i in range(len(self.entities) - 1, -1, -1):
            if not self.entities[i].active:
                self.entities[i].drop_items(self)
                del self.entities[i]

        self.delete_not_active(self.bullets)
        self.delete_not_active(self.droped_items)

        self.player.controls(self)
        self.player.update(self)
        self.player.draw(self.screen)

        if not self.player.alive:
            self.over = True
