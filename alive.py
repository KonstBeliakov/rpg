from utils import *


class Alive(Entity):
    def __init__(self, hp, team=ENEMY, pos=(0, 0)):
        super().__init__(pos)
        self.hp = hp
        self.team = team

    @property
    def alive(self):
        return self.hp > 0

    def update(self, game):
        super().update(game)