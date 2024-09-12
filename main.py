import pygame

from Player import Player

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

square_size = 50
x, y = WIDTH // 2, HEIGHT // 2

running = True

player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)

    player.move()
    player.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
pygame.quit()