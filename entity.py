import pygame


class Entity:
    def __init__(self, pos=(0, 0), size=(50, 50)):
        self.pos = pos
        self.size = size

        self.color = 'black'
        self.__texture = None

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, pos):
        self.x, self.y = pos

    @property
    def center(self):
        return self.x + self.sizeX // 2, self.y + self.sizeY // 2

    @property
    def size(self):
        return self.sizeX, self.sizeY

    @size.setter
    def size(self, new_size):
        self.sizeX, self.sizeY = new_size

    @property
    def texture(self):
        return self.__texture

    @texture.setter
    def texture(self, texture):
        self.__texture = pygame.transform.scale(texture, self.size)

    def draw(self, screen):
        if self.__texture is None:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))
        else:
            screen.blit(self.__texture, self.pos)

    def update(self, game):
        pass
