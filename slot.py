import pygame

from utils import *
from item import *
from entity import Entity


class Slot(Entity):
    def __init__(self, game, inventory, number, pos=(0, 0), size=(64, 64), position=Position.CONSTANT):
        super().__init__(game, pos=pos, size=size)
        self.number = number
        self.inventory = inventory
        self.item = None
        self.outer_color = (50, 50, 50)

        self.selected_color = (100, 100, 100)
        self.selected_outer_color = (100, 255, 100)

    def clear(self):
        self.item = None

    @property
    def empty(self):
        return self.item is None

    def update(self):
        if self.item is not None and self.item.amount <= 0:
            self.item = None

        for event in self.game.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_rect = pygame.Rect(self.pos, self.size)
                if button_rect.collidepoint(event.pos):
                    self.inventory.select(self.number)
                    break

    def draw(self, screen):
        if self.inventory.selected == self.number:
            pygame.draw.rect(screen, self.selected_outer_color, (self.x, self.y, self.sizeX, self.sizeY))
            pygame.draw.rect(screen, self.selected_color, (self.x + 4, self.y + 4, self.sizeX - 8, self.sizeY - 8))
        else:
            pygame.draw.rect(screen, self.outer_color, (self.x, self.y, self.sizeX, self.sizeY))
            pygame.draw.rect(screen, self.color, (self.x + 2, self.y + 2, self.sizeX - 4, self.sizeY - 4))

        if not self.empty:
            screen.blit(ItemsInfo[self.item.type].texture, self.pos)