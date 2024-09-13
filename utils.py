import enum

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600


class Team(enum.Enum):
    PLAYER = 1
    ENEMY = 2
    NEUTRAL = 3


class Position(enum.Enum):
    CONSTANT = 1
    RELATIVE_TO_PLAYER = 2


class WeaponType(enum.Enum):
    DEFAULT = 0
    BOW = 1
    CROSS_STAFF = 2
    LIGHT_STAFF = 3


def collision(entity1, entity2):
    if entity1.x < entity2.x + entity2.sizeX and entity2.x < entity1.x + entity1.sizeX and \
            entity1.y < entity2.y + entity2.sizeY and entity2.y < entity1.y + entity1.sizeY:
        return True
    return False


def dist(entity1, entity2):
    x1, y1 = entity1.center
    x2, y2 = entity2.center
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def transform_price(price):
    return f'{round(price / 100, 2)}G'