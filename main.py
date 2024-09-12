import pygame

from game import Game

pygame.init()
game = Game()

while not game.over:
    game.update()
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
