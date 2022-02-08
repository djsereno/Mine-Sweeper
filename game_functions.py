# Import standard modules
import sys

# Import non-standard modules
import pygame
import random

# Import local classes and methods
from cell import Cell
from grid import Grid
from settings import Settings


def checkEvents(grid: Grid, settings: Settings):
    """Check for key events. Called once per frame."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():

        # Check if user quits
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check if user clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()

            # Check if cursor is within the grid extents
            if grid.rect.collidepoint(pos):
                (row, col) = grid.get_index(pos)

                if left:
                    grid.click(settings, row, col)
                elif right:
                    grid.flag(row, col)


def draw(screen: pygame.Surface, settings: Settings, grid: Grid):
    """Draw things to the window. Called once per frame."""
    screen.fill((0, 0, 0))

    # Draw header

    # Draw grid
    grid.draw(screen, settings)

    pygame.display.flip()