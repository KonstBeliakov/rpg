import pygame

from entity import Entity


class ProgressBar(Entity):
    def __init__(self, value=50, max_value=100, pos=(0, 0), size=(300, 5), color=(0, 255, 0), bg_color=(200, 200, 200),
                 outline_color=(150, 150, 150), gradient=None):
        super().__init__(pos, size)
        self.color = color
        self.bg_color = bg_color
        self.outline_color = outline_color
        self.value = max(0, min(value, max_value))
        self.max_value = max_value
        self.gradient = gradient

    def draw(self, screen):
        pygame.draw.rect(screen, self.outline_color, (self.x - 1, self.y - 1, self.sizeX + 2, self.sizeY + 2))
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.sizeX, self.sizeY))

        if self.gradient is None:
            color = self.color
        else:
            c1 = max(0, self.value) / self.max_value
            c2 = 1 - c1
            color = (self.gradient[0][0] * c1 + self.gradient[1][0] * c2,
                     self.gradient[0][1] * c1 + self.gradient[1][1] * c2,
                     self.gradient[0][2] * c1 + self.gradient[1][2] * c2)

        pygame.draw.rect(screen, color, (self.x, self.y, self.value * self.sizeX / self.max_value, self.sizeY))

    def __call__(self, *args, **kwargs):
        self.draw(*args, **kwargs)
