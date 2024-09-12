import pygame

GOLD_COIN = 1
SILVER_COIN = 2
COPPER_COIN = 3
BOW = 4


class ItemDescription:
    def __init__(self, name, description, texturename, price, **kwargs):
        self.name = name
        self.description = description
        self.texturename = texturename
        self.texture = pygame.image.load(f'textures/{self.texturename}')
        self.texture = pygame.transform.scale(self.texture, (64, 64))
        self.price = price

        for key, value in kwargs.items():
            self.__dict__[key] = value


ItemsInfo = {
    GOLD_COIN: ItemDescription(name='Gold Coin',
                                     description='The main currency for which you can buy upgrades and items',
                                     texturename='gold_coin.png',
                                     price=100
                                     ),
    SILVER_COIN: ItemDescription(name='Silver Coin',
                                     description='The main currency for which you can buy upgrades and items',
                                     texturename='silver_coin.png',
                                     price=10
                                     ),
    COPPER_COIN: ItemDescription(name='Copper Coin',
                                     description='The main currency for which you can buy upgrades and items',
                                     texturename='copper_coin.png',
                                     price=1
                                     ),
    BOW: ItemDescription(name='Bow',
                                     description='Regular bow with low fire rate and damage',
                                     texturename='bow.png',
                                     price=250,
                                     damage=10,
                                     bullet_speed=300,
                                     reload_time=0.7
                                     ),
}


class Item:
    def __init__(self, item=COPPER_COIN, amount=5):
        self.type = item
        self.amount = amount

    def __str__(self):
        return f'{ItemsInfo[self.type].name} ({self.amount})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.type == other.type
        return NotImplemented
