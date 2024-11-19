import pygame
from figures import colors

def draw_game_screen(screen, game, gameplay_background):
    gameplay_background = pygame.transform.scale(gameplay_background, (800, 700))
    screen.blit(gameplay_background, [0, 0])

    # Center the game field
    game.x = 250  # Updated starting x position
    game.y = 50   # Updated starting y position
    game.zoom = 30  # Larger block size

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, (247, 242, 235), [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 35, True, False)  # Larger fonts
    text = font.render("Score: " + str(game.score), True, (0, 0, 0))
    screen.blit(text, [50, 30])
