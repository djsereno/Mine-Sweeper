# Import standard modules.
import sys
import random as rand
import copy

# Import non-standard modules.
import pygame


def checkEvents(grid, settings):
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
                    grid.click(row, col)
                elif right:
                    grid.flag(row, col)


def draw(screen, settings, grid):
    """Draw things to the window. Called once per frame."""
    screen.fill((0, 0, 0))

    # Draw header

    # Draw grid
    grid.draw(screen, settings)

    pygame.display.flip()