import pygame

from entity import Entity
from item import Item, Items, ItemsInfo
from utils import *


class Slot(Entity):
    def __init__(self, inventory, number, pos=(0, 0), size=(64, 64)):
        super().__init__(pos, size)
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

    def update(self, game):
        for event in game.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_rect = pygame.Rect(self.pos, self.size)
                if button_rect.collidepoint(event.pos):
                    self.inventory.selected = self.number
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


class Inventory:
    def __init__(self):
        self.slots = [Slot(inventory=self, number=i, pos=(10 + i*70, 10)) for i in range(10)]
        self.selected = 0

        self.slots[0].item = Item(item=Items.BOW, amount=1)
        self.slots[1].item = Item(item=Items.SILVER_COIN, amount=2)
        self.slots[2].item = Item(item=Items.COPPER_COIN, amount=5)

    def __iter__(self):
        yield from self.slots

    def __getitem__(self, key):
        return self.slots[key]

    def __setitem__(self, key, value):
        self.slots[key] = value

    def clear(self):
        for slot in self:
            slot.clear()

    def update(self, game):
        for slot in self:
            slot.update(game)

    def draw(self, screen):
        for slot in self:
            slot.draw(screen)
