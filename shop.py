from time import perf_counter
import pygame

from entity import Entity
from utils import *
from item import *
from button import Button


class Shop(Entity):
    def __init__(self, game, pos=(0, 0)):
        super().__init__(game, pos=pos, size=(200, 100), position=Position.RELATIVE_TO_PLAYER)
        self.opened = False
        self.color = (100, 100, 255)

        self.deals = [
            [Item(game, COPPER_COIN, 11), Item(game, SILVER_COIN, 9)],
            [Item(game, GOLD_COIN, 1), Item(game, SILVER_COIN, 9)],
            [Item(game, SILVER_COIN, 50), Item(game, UPGRADED_BOW, 1)],
            [Item(game, SILVER_COIN, 110), Item(game, GOLD_BOW, 1)],
            [Item(game, SILVER_COIN, 6), Item(game, SMALL_HEALTH_POTION, 1)],
            [Item(game, SILVER_COIN, 9), Item(game, BIG_HEALTH_POTION, 1)]
        ]

        self.font_size = 20
        self.font = pygame.font.SysFont("Arial", self.font_size)

        self.buttons = [Button(game, self.font, text='trade',
                               pos=(30, 30 + 60 * i), size=(70, 50)) for i in range(len(self.deals))]
        for i in range(len(self.buttons)):
            self.set_button_command(i)

    def update(self):
        for event in self.game.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and dist(self, self.game.player) < 200:
                self.opened = not self.opened
        if dist(self, self.game.player) > 200:
            self.opened = False

        for button in self.buttons:
            button.update(self.game)

    def draw(self, screen, player_pos=(0, 0)):
        super().draw(screen, player_pos)

        if self.opened:
            surface = pygame.Surface((WINDOW_WIDTH - 40, WINDOW_HEIGHT - 40), pygame.SRCALPHA)
            surface.fill((0, 0, 0, 128))
            screen.blit(surface, (20, 20))

            for i, deal in enumerate(self.deals):
                screen.blit(ItemsInfo[deal[0].type].texture, (110, 30 + i * 60))

                text_surface3 = self.font.render(f'x{deal[0].amount} ->', True, (0, 0, 0))
                screen.blit(text_surface3, (110 + 70, 30 + i * 60))

                screen.blit(ItemsInfo[deal[1].type].texture, (110 + 110, 30 + i * 60))

                text_surface3 = self.font.render(f'x{deal[1].amount}', True, (0, 0, 0))
                screen.blit(text_surface3, (110 + 170, 30 + i * 60))

                self.buttons[i].draw(screen)

    def set_button_command(self, n):
        self.buttons[n].command = lambda: self.trade(n)

    def trade(self, number):
        print(f'Button {number} is pressed!')
        if self.game.player.inventory.remove(self.deals[number][0]):
            self.game.player.inventory.add(self.deals[number][1])
        else:
            self.game.player.inventory.hints.append(['Not enough items', perf_counter()])
