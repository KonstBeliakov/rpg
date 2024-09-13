from time import perf_counter

import pygame

from entity import Entity
from item import *
from utils import *
from slot import Slot


class Inventory:
    def __init__(self, game):
        self.game = game
        self.slots = [Slot(game=self.game, inventory=self, number=i, pos=(10 + i * 70, WINDOW_HEIGHT - 80)) for i in range(21)]
        self.selected = 0
        self.hints = []

        self.font_size = 20
        self.font = pygame.font.SysFont("Arial", self.font_size)

        self.slots[0].item = Item(item=BOW, amount=1)
        self.slots[1].item = Item(item=SILVER_COIN, amount=2)
        self.slots[2].item = Item(item=COPPER_COIN, amount=5)

        self.opened = False

    def __iter__(self):
        yield from self.slots

    def __getitem__(self, key):
        return self.slots[key]

    def __setitem__(self, key, value):
        self.slots[key] = value

    def clear(self):
        for slot in self:
            slot.clear()

    def update(self):
        for slot in self:
            slot.update()

        for event in self.game.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if self.opened:
                    for i, slot in enumerate(self.slots):
                        slot.pos = (10 + i * 70, WINDOW_HEIGHT - 80)
                else:
                    for i, slot in enumerate(self.slots):
                        slot.pos = (30 + (i % 7) * 70, 30 + 70 * (i // 7))
                self.opened = not self.opened

    def add(self, item):
        for slot in self.slots:
            if slot.item == item:
                slot.item.amount += item.amount
                self.hints.append([str(slot.item), perf_counter()])
                break
        else:
            for slot in self.slots:
                if slot.empty:
                    slot.item = item
                    self.hints.append([str(slot.item), perf_counter()])
                    break

    def select(self, n):
        self.selected = n
        if not self[self.selected].empty:
            self.hints.append([f'{ItemsInfo[self[self.selected].item.type].name} ({self[self.selected].item.amount})',
                               perf_counter()])

    def draw(self, screen):
        if not self.opened:
            for slot in self.slots[:10]:
                slot.draw(screen)
        else:
            surface = pygame.Surface((WINDOW_WIDTH - 40, WINDOW_HEIGHT - 40), pygame.SRCALPHA)
            surface.fill((0, 0, 0, 128))
            screen.blit(surface, (20, 20))

            for slot in self.slots:
                slot.draw(screen)

            surface = pygame.Surface((250, 500), pygame.SRCALPHA)
            surface.fill((0, 0, 0, 128))
            screen.blit(surface, (30 + 70 * 7, 30))

            screen.blit(ItemsInfo[self[self.selected].item.type].texture, (30 + 10 + 70 * 7, 30))

            selected_item = self[self.selected].item

            text_surface = self.font.render(str(selected_item), True, (0, 0, 0))
            screen.blit(text_surface, (30 + 10 + 70 * 7, 30 + 50 + 20))

            price = ItemsInfo[selected_item.type].price
            text_surface2 = self.font.render(
                f'Price: {transform_price(price * selected_item.amount)} ({transform_price(price)} per item)',
                True, (0, 0, 0))
            screen.blit(text_surface2, (30 + 10 + 70 * 7, 30 + 50 + 20 + 20))

            text_surface3 = self.font.render('Description', True, (0, 0, 0))
            screen.blit(text_surface3, (30 + 10 + 70 * 7, 30 + 50 + 20 + 50))

            text_surface3 = self.font.render(ItemsInfo[selected_item.type].description, True, (0, 0, 0))
            screen.blit(text_surface3, (30 + 10 + 70 * 7, 30 + 50 + 20 + 70))

        for hint in self.hints:
            text_surface = self.font.render(hint[0], True, (0, 0, 0))
            text_surface.set_alpha(int(max(0.0, (1 - (perf_counter() - hint[1]))) * 255))
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2,
                                                      WINDOW_HEIGHT - 120 - (perf_counter() - hint[1]) * 25))
            screen.blit(text_surface, text_rect)
