import numpy as np
from queue import PriorityQueue


def Path_init(ghost_row, ghost_col,grid1):
    pathing_grid = np.copy(grid1)
    path_find = False
    n_rows, n_col = np.shape(pathing_grid)
    counter = 0
    path = []
    path_creator = False

    for i in range(n_rows):
        for i2 in range(n_col):
            # free spaces
            if pathing_grid[i][i2] == 0 or pathing_grid[i][i2] == 2:
                pathing_grid[i][i2] = 99
            # wall or other ghost
            elif pathing_grid[i][i2] == 1 or pathing_grid[i][i2] == 5:
                pathing_grid[i][i2]=98
            # ghost (ground 0)
            elif pathing_grid[i][i2] == 3:
                ghost_row, ghost_col = i, i2
                pathing_grid[i][i2] = 0
            #pacman
            elif pathing_grid[i][i2] == 4:
                pathing_grid[i][i2] = -2

    while (path_find == False):
        for i in range(n_rows-1):
            for i2 in range(n_col-1):
                # ghost step
                if pathing_grid[i][i2] == counter:
                    if (pathing_grid[i][i2+1] == -2) or (pathing_grid[i][i2-1] == -2) or (pathing_grid[i+1][i2] == -2) or (pathing_grid[i-1][i2] == -2):

                        if (pathing_grid[i][i2 + 1] == -2):
                            pathing_grid[i][i2 + 1] = counter+2

                        elif (pathing_grid[i][i2-1] == -2):
                            pathing_grid[i][i2 - 1] = counter+2

                        elif (pathing_grid[i+1][i2] == -2):
                            pathing_grid[i + 1][i2] = counter+2

                        elif (pathing_grid[i-1][i2] == -2):
                            pathing_grid[i - 1][i2] = counter+2
                        path_find = True

                    if (pathing_grid[i][i2 + 1] == 99):
                        pathing_grid[i][i2 + 1] = counter + 1

                    if (pathing_grid[i][i2 - 1] == 99):
                        pathing_grid[i][i2 - 1] = counter + 1

                    if (pathing_grid[i + 1][i2] == 99):
                        pathing_grid[i + 1][i2] = counter + 1

                    if (pathing_grid[i - 1][i2] == 99):
                        pathing_grid[i - 1][i2] = counter + 1

        counter = counter + 1

    n_steps = counter + 1


    for i in range(n_rows):
        for i2 in range(n_col):
            if pathing_grid[i][i2] == n_steps:
                path.append([i,i2])
                r,c = i,i2

    while (path_creator == False):
        n_steps = n_steps -1
        if (pathing_grid[r][c + 1] == n_steps) or (pathing_grid[r][c - 1] == n_steps) or (pathing_grid[r + 1][c] == n_steps) or (pathing_grid[r-1][c] == n_steps):
            if (pathing_grid[r][c + 1] == n_steps):
                path.append([r,c+1])
                c=c+1
            elif (pathing_grid[r][c - 1] == n_steps):
                path.append([r, c-1])
                c=c-1

            elif (pathing_grid[r + 1][c] == n_steps):
                path.append([r+1, c])
                r=r+1

            elif (pathing_grid[r-1][c] == n_steps):
                path.append([r-1, c])
                r=r-1
        if n_steps == 0:
            path_creator = True
    path.reverse()
    return path, ghost_row, ghost_col

def Distance(grid1):
    pathing_grid = np.copy(grid1)
    path_find = False
    n_rows, n_col = np.shape(pathing_grid)
    counter = 0
    # Grid Converter
    for i in range(n_rows):
        for i2 in range(n_col):
            # free spaces
            if pathing_grid[i][i2] == 2: # empty tile
                pathing_grid[i][i2] = 99
            # wall or other ghost
            elif pathing_grid[i][i2] == 1: # wall
                pathing_grid[i][i2]=98
            # ghost (ground 0)
            elif pathing_grid[i][i2] == 4: # pacman
                pathing_grid[i][i2] = 0
            #pacman
            elif pathing_grid[i][i2] == 0: # pellet
                pathing_grid[i][i2] = -2
    # keeps looping steps, expanding from previous step
    while (path_find == False):
        for i in range(n_rows-1):
            for i2 in range(n_col-1):
                # pacman step
                if pathing_grid[i][i2] == counter:
                    if (pathing_grid[i][i2+1] == -2) or (pathing_grid[i][i2-1] == -2) or (pathing_grid[i+1][i2] == -2) or (pathing_grid[i-1][i2] == -2):

                        if (pathing_grid[i][i2 + 1] == -2):
                            pathing_grid[i][i2 + 1] = counter+2

                        elif (pathing_grid[i][i2-1] == -2):
                            pathing_grid[i][i2 - 1] = counter+2

                        elif (pathing_grid[i+1][i2] == -2):
                            pathing_grid[i + 1][i2] = counter+2

                        elif (pathing_grid[i-1][i2] == -2):
                            pathing_grid[i - 1][i2] = counter+2
                        path_find = True

                    if (pathing_grid[i][i2 + 1] == 99):
                        pathing_grid[i][i2 + 1] = counter + 1

                    if (pathing_grid[i][i2 - 1] == 99):
                        pathing_grid[i][i2 - 1] = counter + 1

                    if (pathing_grid[i + 1][i2] == 99):
                        pathing_grid[i + 1][i2] = counter + 1

                    if (pathing_grid[i - 1][i2] == 99):
                        pathing_grid[i - 1][i2] = counter + 1

        counter = counter + 1

    n_steps = counter + 1
    return n_steps








def Path_init2(ghost_row, ghost_col,grid1):
    pathing_grid = np.copy(grid1)
    path_find = False
    n_rows, n_col = np.shape(pathing_grid)
    counter = 0
    path = []
    path_creator = False

    for i in range(n_rows):
        for i2 in range(n_col):
            # free spaces
            if pathing_grid[i][i2] == 0 or pathing_grid[i][i2] == 2:
                pathing_grid[i][i2] = 99
            # wall or other ghost
            elif pathing_grid[i][i2] == 1 or pathing_grid[i][i2] == 3:
                pathing_grid[i][i2]=98
            # ghost (ground 0)
            elif pathing_grid[i][i2] == 5:
                ghost_row, ghost_col = i, i2
                pathing_grid[i][i2] = 0
            #pacman
            elif pathing_grid[i][i2] == 4:
                pathing_grid[i][i2] = -2

    while (path_find == False):
        for i in range(n_rows-1):
            for i2 in range(n_col-1):
                # ghost step
                if pathing_grid[i][i2] == counter:
                    if (pathing_grid[i][i2+1] == -2) or (pathing_grid[i][i2-1] == -2) or (pathing_grid[i+1][i2] == -2) or (pathing_grid[i-1][i2] == -2):

                        if (pathing_grid[i][i2 + 1] == -2):
                            pathing_grid[i][i2 + 1] = counter+2

                        elif (pathing_grid[i][i2-1] == -2):
                            pathing_grid[i][i2 - 1] = counter+2

                        elif (pathing_grid[i+1][i2] == -2):
                            pathing_grid[i + 1][i2] = counter+2

                        elif (pathing_grid[i-1][i2] == -2):
                            pathing_grid[i - 1][i2] = counter+2
                        path_find = True

                    if (pathing_grid[i][i2 + 1] == 99):
                        pathing_grid[i][i2 + 1] = counter + 1

                    if (pathing_grid[i][i2 - 1] == 99):
                        pathing_grid[i][i2 - 1] = counter + 1

                    if (pathing_grid[i + 1][i2] == 99):
                        pathing_grid[i + 1][i2] = counter + 1

                    if (pathing_grid[i - 1][i2] == 99):
                        pathing_grid[i - 1][i2] = counter + 1

        counter = counter + 1

    n_steps = counter + 1


    for i in range(n_rows):
        for i2 in range(n_col):
            if pathing_grid[i][i2] == n_steps:
                path.append([i,i2])
                r,c = i,i2

    while (path_creator == False):
        n_steps = n_steps -1
        if (pathing_grid[r][c + 1] == n_steps) or (pathing_grid[r][c - 1] == n_steps) or (pathing_grid[r + 1][c] == n_steps) or (pathing_grid[r-1][c] == n_steps):
            if (pathing_grid[r][c + 1] == n_steps):
                path.append([r,c+1])
                c=c+1
            elif (pathing_grid[r][c - 1] == n_steps):
                path.append([r, c-1])
                c=c-1

            elif (pathing_grid[r + 1][c] == n_steps):
                path.append([r+1, c])
                r=r+1

            elif (pathing_grid[r-1][c] == n_steps):
                path.append([r-1, c])
                r=r-1
        if n_steps == 0:
            path_creator = True
    path.reverse()
    return path, ghost_row, ghost_col

