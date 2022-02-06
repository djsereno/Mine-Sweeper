# Import standard modules.
import sys
import random as rand
import copy

# Import non-standard modules.
import pygame as pg
from pygame.locals import *


def checkEvents():
    """Check for key events. Called once per frame."""

    # Go through events that are passed to the script by the window.
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()


def draw(screen, settings, grid):
    """Draw things to the window. Called once per frame."""
    screen.fill((0, 0, 0))

    # Draw cells
    for row in range(grid.num_rows):
        for col in range(grid.num_cols):
            cell = grid.cells[row][col]
            rect = cell.rect
            pg.draw.rect(screen, settings.cell_unclicked, rect)

    # Draw borders
    for row in range(grid.num_rows + 1):
        pg.draw.line(screen, settings.border_color,
                     (0, row * settings.cell_height),
                     (settings.screen_width, row * settings.cell_height),
                     settings.border_thick)
    for col in range(grid.num_cols + 1):
        pg.draw.line(screen, settings.border_color,
                     (col * settings.cell_width, 0),
                     (col * settings.cell_width, settings.screen_height),
                     settings.border_thick)

    pg.display.flip()