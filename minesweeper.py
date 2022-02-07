# ==============
# MINE SWEEPER
# ==============
# Future updates or improvements:
#   - Add timer and bomb counter
#   - Improve graphical placement of mines, depending if cell is even or odd number of pixels wide
#   - Animate cascades
#   - Artwork for:
#       - Win: Untripped mines 
#       - Lose: Unflagged mines, flagged mines, questioned mine, tripped mine
#       - In Progress: Flag, question

# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from grid import Grid
import game_functions as gf
from settings import Settings


def runPyGame():
    # Initialise PyGame
    pygame.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pygame.time.Clock()

    # Create settings
    settings = Settings()

    # Set up the window.
    width, height = settings.screen_width, settings.screen_height
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mine Sweeper")

    # Initialize grid
    grid = Grid(settings)

    # Main game loop.
    dt = 1 / fps  # dt is the time since last frame.
    while True:
        gf.checkEvents(grid, settings)
        gf.draw(screen, settings, grid)

        dt = fpsClock.tick(fps)


runPyGame()