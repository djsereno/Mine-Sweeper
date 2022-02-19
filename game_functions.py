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
                if row != -1 and col != -1:
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
    screen.fill(settings.background_color)

    # Draw header
    if settings.game_over == 1:
        header_fill = settings.header_fill_win
    elif settings.game_over == -1:
        header_fill = settings.header_fill_lose
    else:
        header_fill = settings.header_fill

    pygame.draw.rect(screen, header_fill, settings.header_rect)

    # Draw timer
    index = timer.seconds % 12
    screen.blit(settings.timer_images[index], settings.timer_image_rect)
    timer.text.text_image_rect.midleft = settings.timer_image_rect.midright
    timer.text.text_image_rect.x += 10
    timer.draw()

    # Draw mine counter
    rect = pygame.Rect(0, 0, settings.flag_image_width,
                       settings.flag_image_height)
    rect.midright = settings.header_rect.center
    rect.centerx -= 10
    screen.blit(settings.flag_images[0], rect)
    mine_counter.text_image_rect.midright = rect.midleft
    mine_counter.draw()

    # Draw grid
    mouse_pos = pygame.mouse.get_pos()
    grid.draw(settings, mouse_pos)

    pygame.display.flip()


def reset_game(settings: Settings, grid: Grid, timer: Timer):
    """Start a new game"""
    settings.init_dynamic_variables()
    timer.init_dynamic_variables()
    grid.reset(settings)