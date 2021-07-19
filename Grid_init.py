
import numpy as np
import random
from os import environ

def RandGhost(level_grid):
    while True:
        n_rows, n_col = np.shape(level_grid)
        r = random.randint(0,n_rows-1)
        c = random.randint(0,n_col-1)
        if level_grid[r][c] == 0:
            level_grid[r][c] = 3
            break


def LocatePacMan(level_grid):
    n_rows, n_col = np.shape(level_grid)
    for i in range(n_rows):
        for i2 in range(n_col):
            if level_grid[i][i2] == 4:
                return i,i2

def PelletCounter(level_grid):
    n_rows, n_col = np.shape(level_grid)
    counter = 0
    for i in range(n_rows):
        for i2 in range(n_col):
            if level_grid[i][i2] == 0:
                counter = counter + 1
    return counter

def LocateGhost2(level_grid):
    n_rows, n_col = np.shape(level_grid)
    for i in range(n_rows):
        for i2 in range(n_col):
            if level_grid[i][i2] == 3:
                return i,i2
#def LocateGhost1(level_grid):
    #n_rows, n_col = np.shape(level_grid)
    #for i in range(n_rows):
      #  for i2 in range(n_col):
         #   if level_grid[i][i2] == 5:
           #     return i,i2


def PelletGrid(level_grid):
    n_rows, n_col = np.shape(level_grid)
    pellet_grid = np.copy(level_grid)
    for i in range(n_rows):
        for i2 in range(n_col):
            if pellet_grid[i][i2] == 3:
                pellet_grid[i][i2] = 0
            elif pellet_grid[i][i2]==4:
                pellet_grid[i][i2] = 2
    return pellet_grid
