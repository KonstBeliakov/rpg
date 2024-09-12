from random import randrange

from monsters import *
from utils import *
from alive import Alive
from player import Player

WIDTH, HEIGHT = 800, 600


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.over = False

        self.player = Player()
        self.entities = [Slime(50, team=Team.ENEMY) for _ in range(10)]
        for entity in self.entities:
            entity.pos = (randrange(WIDTH), randrange(HEIGHT))

        self.bullets = []
        self.droped_items = []
        self.events = []

    def update(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.over = True
        self.screen.fill((255, 255, 255))

        for entity in self.entities:
            entity.draw(self.screen)

        for i in range(len(self.entities) - 1, -1, -1):
            if isinstance(self.entities[i], Alive) and not self.entities[i].alive:
                self.entities[i].drop_items(self)
                del self.entities[i]

        for bullet in self.bullets:
            bullet.update(self)
            bullet.draw(self.screen)

        for i in range(len(self.bullets) - 1, -1, -1):
            if not self.bullets[i].active:
                del self.bullets[i]

        for item in self.droped_items:
            item.update(self)
            item.draw(self.screen)

        for i in range(len(self.droped_items) - 1, -1, -1):
            if not self.droped_items[i].active:
                del self.droped_items[i]

        self.player.controls(self)
        self.player.update(self)
        self.player.draw(self.screen)

        if not self.player.alive:
            self.over = True
