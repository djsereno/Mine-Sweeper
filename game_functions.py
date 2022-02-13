# Import standard modules
from cgitb import reset
import sys
from typing import Text

# Import non-standard modules
import pygame
import random

# Import local classes and methods
from cell import Cell
from grid import Grid
from timer import Timer
from text_image import Text_Image
from settings import Settings


def checkEvents(grid: Grid, settings: Settings, timer: Timer):
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
            if grid.rect.collidepoint(pos) and not settings.game_over:

                # Start the game if currently inactive
                if not settings.game_active:
                    settings.game_active = 1

                (row, col) = grid.get_index(pos)
                if left:
                    grid.click(settings, row, col)
                elif right:
                    grid.flag(settings, row, col)

            # Restart the game if the user clicks the header once the game is over
            elif settings.game_over and settings.header_rect.collidepoint(pos):
                reset_game(settings, grid, timer)


def update(dt: int, settings: Settings, timer: Timer,
           mine_counter: Text_Image):
    """Updates the game items"""

    # Increment the game timer if game is active
    if settings.game_active:
        timer.increment(dt)

    timer.update()
    mine_counter.prep_text("{0:02}/{1:02}".format(settings.mines_flagged,
                                                  settings.number_mines))


def draw(screen: pygame.Surface, settings: Settings, grid: Grid, timer: Timer,
         mine_counter: Text_Image):
    """Draw things to the window. Called once per frame."""
    screen.fill((0, 0, 0))

    # Draw header
    pygame.draw.rect(screen, settings.header_fill_color, settings.header_rect)
    timer.text.text_image_rect.midright = settings.header_rect.midright
    timer.draw()
    mine_counter.text_image_rect.midleft = settings.header_rect.midleft
    mine_counter.draw()

    # Draw grid
    grid.draw(settings)

    pygame.display.flip()


def reset_game(settings: Settings, grid: Grid, timer: Timer):
    """Start a new game"""
    settings.init_dynamic_variables()
    timer.init_dynamic_variables()
    grid.reset(settings)