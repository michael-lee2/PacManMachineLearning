from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import numpy as np

a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
gridhard2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
size_grid = np.array(gridhard2)
n_rows, n_col = np.shape(size_grid)
screen_size_x, screen_size_y = 960,1400
tile_height = screen_size_y / n_rows
tile_width = screen_size_x / n_col
blue = (0, 128, 255)
black = (0, 0, 0)
white = (255, 255, 255)

PacMan_Right = []
PacMan_Right.append(
    pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\pacman1.0.png'))
PacMan_Right.append(
    pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\pacman2.0.png'))
PacMan_Right.append(
    pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\pacman3.0.png'))
PacMan_Right[0] = pygame.transform.smoothscale(PacMan_Right[0], (int(tile_width), int(tile_height)))
PacMan_Right[1] = pygame.transform.smoothscale(PacMan_Right[1], (int(tile_width), int(tile_height)))
PacMan_Right[2] = pygame.transform.smoothscale(PacMan_Right[2], (int(tile_width), int(tile_height)))

PacMan_Left = []
PacMan_Left.append(pygame.transform.flip(PacMan_Right[0], True, False))
PacMan_Left.append(pygame.transform.flip(PacMan_Right[1], True, False))
PacMan_Left.append(pygame.transform.flip(PacMan_Right[2], True, False))
PacMan_Left[0] = pygame.transform.smoothscale(PacMan_Left[0], (int(tile_width), int(tile_height)))
PacMan_Left[1] = pygame.transform.smoothscale(PacMan_Left[1], (int(tile_width), int(tile_height)))
PacMan_Left[2] = pygame.transform.smoothscale(PacMan_Left[2], (int(tile_width), int(tile_height)))

PacMan_Up = []
PacMan_Up.append(
    pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\pacman1.0_up.png'))
PacMan_Up.append(
    pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\pacman2.0_up.png'))
PacMan_Up.append(
    pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\pacman3.0_up.png'))
PacMan_Up[0] = pygame.transform.smoothscale(PacMan_Up[0], (int(tile_width), int(tile_height)))
PacMan_Up[1] = pygame.transform.smoothscale(PacMan_Up[1], (int(tile_width), int(tile_height)))
PacMan_Up[2] = pygame.transform.smoothscale(PacMan_Up[2], (int(tile_width), int(tile_height)))

PacMan_Down = []
PacMan_Down.append(pygame.transform.flip(PacMan_Up[0], False, True))
PacMan_Down.append(pygame.transform.flip(PacMan_Up[1], False, True))
PacMan_Down.append(pygame.transform.flip(PacMan_Up[2], False, True))
PacMan_Down[0] = pygame.transform.smoothscale(PacMan_Down[0], (int(tile_width), int(tile_height)))
PacMan_Down[1] = pygame.transform.smoothscale(PacMan_Down[1], (int(tile_width), int(tile_height)))
PacMan_Down[2] = pygame.transform.smoothscale(PacMan_Down[2], (int(tile_width), int(tile_height)))

Kanye = pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\kanye.png')
Kanye = pygame.transform.smoothscale(Kanye, (int(tile_width), int(tile_height)))

Ghost1_Down = pygame.image.load(
    r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\ghost1_down.png')
Ghost1_Down = pygame.transform.smoothscale(Ghost1_Down, (int(tile_width), int(tile_height)))
Ghost1_Right = pygame.image.load(
    r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\ghost1_right.png')
Ghost1_Right = pygame.transform.smoothscale(Ghost1_Right, (int(tile_width), int(tile_height)))
Ghost1_Left = pygame.image.load(
    r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\ghost1_left.png')
Ghost1_Left = pygame.transform.smoothscale(Ghost1_Left, (int(tile_width), int(tile_height)))
Ghost1_Up = pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\ghost1_up.png')
Ghost1_Up = pygame.transform.smoothscale(Ghost1_Up, (int(tile_width), int(tile_height)))

Ghost2_Down = pygame.image.load(
    r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\ghost2_down.png')
Ghost2_Down = pygame.transform.smoothscale(Ghost2_Down, (int(tile_width), int(tile_height)))
Ghost2_Right = pygame.image.load(
    r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\ghost2_right.png')
Ghost2_Right = pygame.transform.smoothscale(Ghost2_Right, (int(tile_width), int(tile_height)))
Ghost2_Left = pygame.image.load(
    r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\ghost2_left.png')
Ghost2_Left = pygame.transform.smoothscale(Ghost2_Left, (int(tile_width), int(tile_height)))
Ghost2_Up = pygame.image.load(r'C:\Users\mlee2\PycharmProjects\PacManMachineLearning\PacMan Animation\ghost2_up.png')
Ghost2_Up = pygame.transform.smoothscale(Ghost2_Up, (int(tile_width), int(tile_height)))


def Sprite(row, column, image, screen):
    screen.blit(image, (column * tile_width, row * tile_height))


# Drawing Grid, removed pellet grid
def LevelCreator(level_grid, screen, counter, direction, pacman_row, pacman_col):
    # ghost_row1 = 0
    # ghost_col1 = 0
    # ghost_row2 = 0
    # ghost_col2 = 0
    perspective = []
    check = True
    pellet_count = 0
    for i in range(n_rows):
        for i2 in range(n_col):
            # Wall
            if level_grid[i][i2] == 1:
                pygame.draw.rect(screen, blue,
                                 pygame.Rect(i2 * tile_width, i * tile_height, tile_width + 1, tile_height + 1))
            elif level_grid[i][i2] == 3:
                pygame.draw.rect(screen, black,
                                 pygame.Rect(i2 * tile_width, i * tile_height, tile_width + 1, tile_height + 1))
                Sprite(i, i2, Kanye, screen)
                ghost_row2, ghost_col2 = i, i2
            # second ghost
            elif level_grid[i][i2] == 5:
                pygame.draw.rect(screen, black,
                                 pygame.Rect(i2 * tile_width, i * tile_height, tile_width + 1, tile_height + 1))
                Sprite(i, i2, Ghost1_Right, screen)
                # ghost_row1, ghost_col1 = i, i2
            # Pac-Man
            elif level_grid[i][i2] == 4:
                pygame.draw.rect(screen, black,
                                 pygame.Rect(i2 * tile_width, i * tile_height, tile_width + 1, tile_height + 1))
                if direction == [0, 0, 1, 0]:
                    Sprite(i, i2, PacMan_Right[counter], screen)

                elif direction == [1, 0, 0, 0]:
                    Sprite(i, i2, PacMan_Left[counter], screen)

                elif direction == [0, 1, 0, 0]:
                    Sprite(i, i2, PacMan_Up[counter], screen)

                elif direction == [0, 0, 0, 1]:
                    Sprite(i, i2, PacMan_Down[counter], screen)

                elif direction == [0, 0, 0, 0]:
                    Sprite(i, i2, PacMan_Right[counter], screen)
            # Pellet
            elif level_grid[i][i2] == 0:
                pygame.draw.rect(screen, black,
                                 pygame.Rect(i2 * tile_width, i * tile_height, tile_width + 1, tile_height + 1))
                pygame.draw.circle(screen, white,
                                   [i2 * tile_width + (0.5 * tile_width), i * tile_height + (0.5 * tile_height)], 1)
                pellet_count = pellet_count + 1
            # Empty Tile
            elif level_grid[i][i2] == 2:
                pygame.draw.rect(screen, black,
                                 pygame.Rect(i2 * tile_width, i * tile_height, tile_width + 1, tile_height + 1))

    # return ghost_row1, ghost_col1, ghost_row2, ghost_col2
    return ghost_row2, ghost_col2, pellet_count







