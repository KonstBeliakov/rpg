from entity import Entity

from time import perf_counter


class Bullet(Entity):
    def __init__(self, speed, pos=(0, 0)):
        super().__init__(pos)
        self.size = (10, 10)
        self.speed = speed
        self.last_update = perf_counter()

    @property
    def speed(self):
        return self.speedX, self.speedY

    @speed.setter
    def speed(self, speed):
        self.speedX, self.speedY = speed

    def update(self):
        dt = perf_counter() - self.last_update
        self.x += self.speedX * dt
        self.y += self.speedY * dt
        self.last_update = perf_counter()

