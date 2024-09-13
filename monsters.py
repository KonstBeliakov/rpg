from alive import Alive
from item import *
from utils import *
from random import randint


class Slime(Alive):
    def __init__(self, game, team=Team.ENEMY, pos=(0, 0)):
        super().__init__(game, hp=25, team=team, pos=pos, size=(30, 30))
        self.color = (0, 150, 150)
        self.drop = [Item(game, COPPER_COIN, randint(1, 3))]


class Goblin(Alive):
    def __init__(self, game, team=Team.ENEMY, pos=(0, 0)):
        super().__init__(game, hp=100, team=team, pos=pos, size=(50, 50))
        self.color = (0, 200, 0)
        self.drop = [Item(game, COPPER_COIN, randint(1, 5)), Item(game, SILVER_COIN, randint(0, 1))]
