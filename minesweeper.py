# ==============
# MINE SWEEPER
# ==============
# Author: Derek Sereno
# Images courtesy of https://www.vecteezy.com
# Audio curtesy of https://freesound.org & https://mixkit.co
#
# Future updates or improvements:
#   - Sound fx mute
#   - UI to adjust game difficulty
#   - Animations:
#       - Empty cell cascades
#       - Tripped mine cascades
#       - Flags placed/removed

# Import standard modules

# Import non-standard modules
import pygame

# Import local classes and methods
from grid import Grid
from settings import Settings
from timer import Timer
from text_image import Text_Image
import game_functions as gf


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
    icon = settings.mine_icon
    pygame.display.set_icon(icon)

    # Create game timer and mine counter
    timer = Timer(screen, settings)
    mine_counter = Text_Image("{0:02}/{1:02}".format(0, settings.number_mines),
                              screen, settings.header_font,
                              settings.header_font_color)

    # Initialize grid
    grid = Grid(screen, settings)

    # Main game loop
    dt = 1 / fps  # dt is the time since last frame
    while True:
        gf.checkEvents(grid, settings, timer)
        gf.update(dt, settings, timer, mine_counter)
        gf.draw(screen, settings, grid, timer, mine_counter)
        dt = fpsClock.tick(fps)


runPyGame()