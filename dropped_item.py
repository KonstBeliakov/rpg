from entity import Entity
from time import perf_counter
from item import *


class DroppedItem(Entity):
    def __init__(self, item, pos=(0, 0)):
        super().__init__(pos=pos, size=(16, 16))
        self.item = item
        self.active = True
        self.texture = ItemsInfo[item.type].texture

    def update(self, game):
        if int(perf_counter() / 0.5) % 2:
            self.y += 0.15
        else:
            self.y -= 0.15
