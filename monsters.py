from alive import Alive
from item import *
from utils import *
from random import randint


class Slime(Alive):
    def __init__(self, game, hp, team=Team.ENEMY, pos=(0, 0)):
        super().__init__(game, hp, team, pos)
        self.hp = 25
        self.max_hp = 25
        self.drop = [Item(COPPER_COIN, randint(1, 3))]
