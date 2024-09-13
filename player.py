import pygame
from time import perf_counter
from math import sin, cos, atan2

from alive import Alive
from bullet import Bullet
from inventory import Inventory
from progress_bar import ProgressBar
from utils import *


class Player(Alive):
    def __init__(self, game):
        super().__init__(game, hp=100)

        self.bulletSpeed = 300
        self.atack_delay = 0.7
        self.last_atacked = perf_counter()

        self.atacked = False

        self.info_font = pygame.font.SysFont("Arial", 20)

        self.inventory = Inventory(self.game)

    def controls(self, game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5
        if keys[pygame.K_w]:
            self.y -= 5
        if keys[pygame.K_s]:
            self.y += 5

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] or mouse_buttons[1]:
            self.atack(game)

    def update(self):
        self.inventory.update()

        self.atacked = False
        for entity in self.game.entities:
            if collision(self, entity) and getattr(entity, 'team', None) == Team.ENEMY:
                self.take_damege(1)
                self.atacked = True

        if self.atacked:
            self.color = 'red'
        else:
            self.color = 'black'

        for item in self.game.droped_items:
            if collision(self, item):
                self.inventory.add(item.item)
                item.active = False

    def atack(self, game):
        if perf_counter() - self.last_atacked > getattr(self.inventory.current_item, 'atack_delay', 0.5) and game.entities:
            enemy = min(game.entities, key=lambda entity: dist(self, entity))
            dx = self.center[0] - enemy.center[0]
            dy = self.center[1] - enemy.center[1]
            direction = atan2(dy, dx)
            game.bullets.append(Bullet(game=self.game,
                                       speed=(-self.bulletSpeed * cos(direction),
                                              -self.bulletSpeed * sin(direction)),
                                       team=Team.PLAYER,
                                       pos=self.center,
                                       damage=getattr(self.inventory.current_item, 'damage', 3)))
            self.last_atacked = perf_counter()

    def draw(self, screen):
        super().draw(screen)

        self.inventory.draw(screen)

        ProgressBar(self.hp, self.max_hp, (10, 10), (300, 10), gradient=((50, 255, 50), (255, 50, 50)))(screen)
        ProgressBar(perf_counter() - self.last_atacked, self.atack_delay, (10, 30), (100, 5),
                    gradient=((255, 255, 50), (200, 200, 200)))(screen)
