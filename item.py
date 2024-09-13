import pygame

from utils import *

NO_ITEM = 0
GOLD_COIN = 1
SILVER_COIN = 2
COPPER_COIN = 3
BOW = 4
SMALL_HEALTH_POTION = 5
BIG_HEALTH_POTION = 6
UPGRADED_BOW = 7
GOLD_BOW = 8
CROSS_STAFF = 9
UPGRADED_CROSS_STAFF = 10
LIGHT_STAFF = 11
UPGRADED_LIGHT_STAFF = 12


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


def heal(game, amount):
    game.player.hp = min(game.player.hp + amount, game.player.max_hp)


ItemsInfo = {
    NO_ITEM: ItemDescription(name='None', description='None', texturename='copper_coin.png', price=0),
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
                         weapon_type=WeaponType.BOW,
                         price=250,
                         damage=10,
                         bullet_speed=300,
                         atack_delay=0.7
                         ),
    SMALL_HEALTH_POTION: ItemDescription(name='Small health potion',
                                         description='Regenerates 30 HP when used',
                                         texturename='small_health_potion.png',
                                         price=50,
                                         use=lambda game: heal(game, 60)
                                         ),
    BIG_HEALTH_POTION: ItemDescription(name='Big health potion',
                                       description='Regenerates 60 HP when used',
                                       texturename='big_health_potion.png',
                                       price=90,
                                       use=lambda game: heal(game, 60)
                                       ),
    UPGRADED_BOW: ItemDescription(name='Upraded bow',
                                  description='Shootes a little faster and have more damage',
                                  texturename='upgraded_bow.png',
                                  weapon_type=WeaponType.BOW,
                                  price=450,
                                  damage=12,
                                  bullet_speed=300,
                                  atack_delay=0.65
                                  ),
    GOLD_BOW: ItemDescription(name='Golden bow',
                              description='Expensive version of a regular bow',
                              texturename='golden_bow.png',
                              weapon_type=WeaponType.BOW,
                              price=1000,
                              damage=13,
                              bullet_speed=300,
                              atack_delay=0.55
                              ),
    CROSS_STAFF: ItemDescription(name='Cross staff',
                                 description='A staff that shoots in four directions',
                                 texturename='cross_staff.png',
                                 weapon_type=WeaponType.CROSS_STAFF,
                                 price=550,
                                 damage=9,
                                 bullet_speed=300,
                                 atack_delay=0.65
                                 ),
    UPGRADED_CROSS_STAFF: ItemDescription(name='Cross staff',
                                          description='Upgraded version of a staff that shoots in four directions. This version is a lot faster',
                                          texturename='upgraded_cross_staff.png',
                                          weapon_type=WeaponType.CROSS_STAFF,
                                          price=1450,
                                          damage=8,
                                          bullet_speed=450,
                                          atack_delay=0.45
                                          ),
}


class Item:
    def __init__(self, game, item=COPPER_COIN, amount=5):
        self.game = game
        self.type = item
        self.amount = amount

    def __str__(self):
        return f'{ItemsInfo[self.type].name} ({self.amount})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.type == other.type
        return NotImplemented

    @property
    def atack_delay(self):
        return getattr(ItemsInfo[self.type], 'atack_delay', 0.5)

    @property
    def damage(self):
        return getattr(ItemsInfo[self.type], 'damage', 3)

    def use(self):
        if hasattr(ItemsInfo[self.type], 'use'):
            self.amount -= 1
            ItemsInfo[self.type].use(self.game)
