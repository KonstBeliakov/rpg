import pygame

from utils import *


class Alive(Entity):
    def __init__(self, hp, team=ENEMY, pos=(0, 0)):
        super().__init__(pos)
        self.max_hp = hp
        self.hp = hp
        self.team = team

    @property
    def alive(self):
        return self.hp > 0

    def draw(self, screen):
        super().draw(screen)

        hp_bar_size = self.sizeX

        pygame.draw.rect(screen, (150, 150, 150), (self.x - 1, self.y - 11, hp_bar_size + 2, 7))
        pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y - 10, hp_bar_size, 5))

        health_color = (255 * (1 - (max(0, self.hp) / self.max_hp)), 255 * (max(0, self.hp) / self.max_hp), 0)
        pygame.draw.rect(screen, health_color,(self.x, self.y - 10, self.hp * hp_bar_size / self.max_hp, 5))
