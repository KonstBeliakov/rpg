import pygame

from entity import Entity
from utils import *


class Button(Entity):
    def __init__(self, game, font, text='Button', command=None, pos=(0, 0), size=(50, 50)):
        super().__init__(game, pos=pos, size=size, position=Position.CONSTANT)
        self.color = (30, 30, 30)
        self.bg_color = (60, 60, 60)
        self.pressed_color = (60, 60, 60)
        self.text_color = (200, 200, 200)
        self.pressed_text_color = (250, 250, 250)
        self.text = text
        self.command = command

        self.pressed = False

        self.font = font

    def update(self, game):
        for event in game.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_rect = pygame.Rect(self.pos, self.size)
                if button_rect.collidepoint(event.pos):
                    self.command()
                    self.pressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.pressed = False

    def draw(self, screen):
        if self.pressed:
            pygame.draw.rect(screen, self.pressed_color, (self.x + 2, self.y + 2, self.sizeX + 2, self.sizeY + 2))

            text_surface3 = self.font.render(self.text, True, self.text_color)
            screen.blit(text_surface3, self.pos)
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))
            pygame.draw.rect(screen, self.bg_color, (self.x + 2, self.y + 2, self.sizeX + 2, self.sizeY + 2))

            text_surface3 = self.font.render(self.text, True, self.pressed_text_color)
            screen.blit(text_surface3, (self.x + 2, self.y + 2))

