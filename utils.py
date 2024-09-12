from entity import Entity


def collision(entity1: Entity, entity2: Entity):
    if entity1.x < entity2.x + entity2.sizeX and entity2.x < entity1.x + entity1.sizeX and \
            entity1.y < entity2.y + entity2.sizeY and entity2.y < entity1.y + entity1.sizeY:
        return True
    return False
