import pygame
from time import perf_counter
from math import sin, cos, atan2

from alive import Alive
from bullet import Bullet
from utils import *


class Player(Alive):
    def __init__(self):
        super().__init__(hp=100)

        self.bulletSpeed = 300
        self.atack_delay = 1.3
        self.last_atacked = perf_counter()

        self.atacked = False

        self.info_font = pygame.font.SysFont("Arial", 20)

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

    def update(self, game):
        self.atacked = False
        for entity in game.entities:
            if collision(self, entity):
                self.hp -= 1
                self.atacked = True

        if self.atacked:
            self.color = 'red'
        else:
            self.color = 'black'

    def atack(self, game):
        if perf_counter() - self.last_atacked > self.atack_delay:
            enemy = min(game.entities, key=lambda entity: dist(self, entity))
            dx = self.center[0] - enemy.center[0]
            dy = self.center[1] - enemy.center[1]
            direction = atan2(dy, dx)
            game.bullets.append(Bullet(speed=(-self.bulletSpeed * cos(direction),
                                              -self.bulletSpeed * sin(direction)),
                                       team=PLAYER,
                                       pos=self.center))
            self.last_atacked = perf_counter()

    def draw(self, screen):
        super().draw(screen)

        screen.blit(self.info_font.render(f"Hp: {self.hp}", True, (0, 0, 0)), (10, 10))
