import threading
from time import perf_counter

import pygame

from dropped_item import DroppedItem
from progress_bar import ProgressBar
from utils import *


class Alive(Entity):
    def __init__(self, hp, team=Team.ENEMY, pos=(0, 0)):
        super().__init__(pos)
        self.max_hp = hp
        self.hp = hp
        self.team = team
        self.drop = []

    @property
    def alive(self):
        return self.hp > 0

    @property
    def active(self):
        return self.hp > 0 or perf_counter() - self.death_time < 1

    @active.setter
    def active(self, active):
        self.__active = active

    def take_damege(self, damage):
        if self.alive:
            self.hp -= damage
            if not self.alive:
                self.color = tuple(list(self.color)[:3] + [255])
                self.death_time = perf_counter()

                def temp():
                    self.active = False

                t1 = threading.Timer(interval=0.7, function=temp)
                self.active = False

    def draw(self, screen):
        super().draw(screen)

        if self.alive:
            progress_bar = ProgressBar(self.hp, self.max_hp, (self.x, self.y - 10), (self.sizeX, 5),
                                       gradient=((20, 255, 20), (255, 20, 20)))
            progress_bar.draw(screen)
        else:
            self.color = tuple(list(self.color)[:3] + [255 * (max(0, 1 - (perf_counter() - self.death_time)))])

    def drop_items(self, game):
        for item in self.drop:
            game.droped_items.append(DroppedItem(item, self.pos))
