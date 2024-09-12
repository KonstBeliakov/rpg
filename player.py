import pygame
from entity import Entity
from utils import collision


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.hp = 100

        self.atacked = False

    @property
    def alive(self):
        return self.hp > 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5
        if keys[pygame.K_w]:
            self.y -= 5
        if keys[pygame.K_s]:
            self.y += 5

    def update(self, entities: list[Entity]):
        self.atacked = False
        for entity in entities:
            if collision(self, entity):
                self.hp -= 5
                self.atacked = True

        if self.atacked:
            self.color = 'red'
        else:
            self.color = 'black'
