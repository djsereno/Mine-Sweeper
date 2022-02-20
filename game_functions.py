# Import standard modules
import sys

# Import non-standard modules
import pygame
import math

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
                        grid.click(settings, row, col, True)
                    elif right:
                        grid.flag(settings, row, col, 1)
                    elif middle:
                        grid.flag(settings, row, col, 2)

            # Prompt user for new game once the game is over
            elif (settings.game_over 
                and not settings.endgame_animating 
                and settings.new_game_button_rect.collidepoint(pos)):
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

    # Draw header and game over images
    if settings.game_over == 1:
        header_fill = settings.header_fill_win
    elif settings.game_over == -1:
        header_fill = settings.header_fill_lose
    else:
        header_fill = settings.header_fill
    pygame.draw.rect(screen, header_fill, settings.header_rect)

    # Draw timer
    screen.blit(settings.timer_image, settings.timer_image_rect)

    [x0, y0] = settings.timer_image_rect.center
    x0 -= 0.5
    y0 += 3
    arm_len = 11
    x1 = x0 + arm_len * math.cos(timer.seconds / 30 * math.pi - math.pi / 2)
    y1 = y0 + arm_len * math.sin(timer.seconds / 30 * math.pi - math.pi / 2)
    pygame.draw.aaline(screen, (0, 0, 0), [x0, y0], [x1, y1])

    timer.text.text_image_rect.midleft = settings.timer_image_rect.midright
    timer.text.text_image_rect.x += 5
    timer.draw()

    # Draw mine counter
    screen.blit(settings.flag_counter_image, settings.flag_counter_rect)
    mine_counter.text_image_rect.midleft = settings.flag_counter_rect.midright
    mine_counter.draw()

    # Draw grid
    mouse_pos = pygame.mouse.get_pos()
    grid.draw(settings, mouse_pos)

    # Draw game over images
    if settings.game_over:
        
        # Dim the background content
        dimmer = pygame.Surface(settings.grid_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(dimmer, (0, 0, 0, settings.dimmer_opacity), dimmer.get_rect())
        screen.blit(dimmer, settings.grid_rect)
        
        # Gradually increase the dimming
        if settings.dimmer_opacity < settings.dimmer_max_opacity:
            settings.dimmer_opacity += 2

        # Done with dimming. Show game over messages
        else:
            
            # Game over message
            if settings.game_over == 1:
                gameover_image = settings.success_image
                gameover_image_rect = settings.success_image_rect
            elif settings.game_over == -1:
                gameover_image = settings.failure_image
                gameover_image_rect = settings.failure_image_rect

            # New game button, check for mouse hover
            if (settings.new_game_button_rect.collidepoint(mouse_pos) 
                and not settings.endgame_animating):
                new_game_image = settings.new_game_hover_image
            else:
                new_game_image = settings.new_game_image

            gameover_image.set_alpha(settings.image_opacity)
            new_game_image.set_alpha(settings.image_opacity)
            screen.blit(gameover_image, gameover_image_rect)
            screen.blit(new_game_image, settings.new_game_image_rect)

            # Fade in game over images
            if settings.image_opacity < 255:
                settings.image_opacity += 5
            else:
                settings.endgame_animating = False

    pygame.display.flip()


def reset_game(settings: Settings, grid: Grid, timer: Timer):
    """Start a new game"""
    settings.init_dynamic_variables()
    timer.init_dynamic_variables()
    grid.reset(settings)