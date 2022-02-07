# Import standard modules.
import sys
import random as rand
import copy

# Import non-standard modules.
import pygame
from pygame.locals import *


def checkEvents(grid, settings):
    """Check for key events. Called once per frame."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # Check if user quits
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Check if user clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            (row, col) = get_index(pos, settings)
            
            if left:
                grid.click(row, col)
            elif right:
                grid.flag(row, col)

def draw(screen, settings, grid):
    """Draw things to the window. Called once per frame."""
    screen.fill((0, 0, 0))

    # Draw grid
    grid.draw(screen, settings)

    pygame.display.flip()


def get_index(pos, settings):
    """Returns the (col, row) for a given (x, y)"""
    (x, y) = pos
    width, height = settings.screen_width, settings.screen_height
    num_rows, num_cols = settings.num_rows, settings.num_cols
    row = int(y / height * num_rows)
    col = int(x / width * num_cols)
    return (row, col)