from alive import Alive
from entity import Entity

from time import perf_counter

from utils import *


class Bullet(Entity):
    def __init__(self, speed, team=Team.ENEMY, pos=(0, 0)):
        super().__init__(pos)
        self.size = (10, 10)
        self.speed = speed
        self.team = team
        self.last_update = perf_counter()

    @property
    def speed(self):
        return self.speedX, self.speedY

    @speed.setter
    def speed(self, speed):
        self.speedX, self.speedY = speed

    def update(self, game):
        dt = perf_counter() - self.last_update
        self.x += self.speedX * dt
        self.y += self.speedY * dt
        self.last_update = perf_counter()

        for entity in game.entities:
            if isinstance(entity, Alive) and collision(self, entity) and self.team != entity.team:
                entity.take_damege(10)
                self.active = False
                break
