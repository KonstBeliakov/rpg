import pygame

from utils import *


class Map:
    def __init__(self, game):
        self.game = game

    def draw(self, screen):
        pos = self.game.player.pos
        for i in range(-10, 11):
            x = WINDOW_WIDTH // 2 + ((pos[0] // 100 + i) * 100 - self.game.player.pos[0])
            pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, WINDOW_HEIGHT), 1)

        for i in range(-10, 11):
            y = WINDOW_HEIGHT // 2 + ((pos[1] // 100 + i) * 100 - self.game.player.pos[1])
            pygame.draw.line(screen, (0, 0, 0), (0, y), (WINDOW_WIDTH, y), 1)
