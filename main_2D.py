import pygame
import numpy as np
import time

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode(size=(height, width))

bg = (25, 25, 25)
screen.fill(bg)

n_cell_x, n_cell_y = 25, 25
cell_w, cell_h = width/n_cell_x, height/n_cell_y

gameState = np.zeros((n_cell_x, n_cell_y))

# Automatas
gameState[5, 5] = 1
gameState[5, 6] = 1
gameState[5, 7] = 1

pause = False

while True:
    next_gameState = np.copy(gameState)
    screen.fill(bg)

    # Event register
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause = not pause
        mouseClick = pygame.mouse.get_pressed()
        if mouseClick[0]:
            posX, posY = pygame.mouse.get_pos()
            cellX, cellY = int(np.floor(posX/cell_w)), int(np.floor(posY/cell_h))
            next_gameState[cellX, cellY] = not next_gameState[cellX, cellY]

    for y in range(n_cell_x):
        for x in range(n_cell_y):
            if not pause:
                num_neighbor = gameState[x     % n_cell_x, (y-1) % n_cell_y] + \
                               gameState[(x+1) % n_cell_x, (y-1) % n_cell_y] + \
                               gameState[(x+1) % n_cell_x, y     % n_cell_y] + \
                               gameState[(x+1) % n_cell_x, (y+1) % n_cell_y] + \
                               gameState[x     % n_cell_x, (y+1) % n_cell_y] + \
                               gameState[(x-1) % n_cell_x, (y+1) % n_cell_y] + \
                               gameState[(x-1) % n_cell_x, y     % n_cell_y] + \
                               gameState[(x-1) % n_cell_x, (y-1) % n_cell_y]

                if gameState[x, y] == 0 and num_neighbor == 3:
                    next_gameState[x, y] = 1

                if gameState[x, y] == 1 and (num_neighbor < 2 or num_neighbor > 3):
                    next_gameState[x, y] = 0

            cell = [(x*cell_w, y * cell_h),
                    ((x+1)*cell_w, y*cell_h),
                    ((x+1)*cell_w, (y+1)*cell_h),
                    (x*cell_w, (y+1)*cell_h)]

            if next_gameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), cell, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), cell, 0)

    gameState = np.copy(next_gameState)
    pygame.display.flip()
    time.sleep(0.1)
    pass
