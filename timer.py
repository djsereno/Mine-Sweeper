# Import standard modules
import imp
import sys

# Import non-standard modules
import pygame
import random

# Import local classes and methods
from cell import Cell
from grid import Grid
from settings import Settings
from text_image import Text_Image


class Timer():
    """A class to represent the in game timer"""

    def __init__(self, screen: pygame.Surface, settings: Settings) -> None:
        """Initialize the timer"""

        # Timer properties
        self.init_dynamic_variables()

        # Timer text image
        self.text = Text_Image(self.message, screen, settings.header_font_type,
                               settings.header_font_size,
                               settings.header_font_color)

    def increment(self, dt):
        """Increments the current timer value by dt"""
        self.total_seconds += dt / 1000
        self.minutes = int(self.total_seconds // 60)
        self.seconds = int(self.total_seconds % 60)

    def update(self):
        """Updates the timer message and text image"""
        self.message = "{0:02}:{1:02}".format(self.minutes, self.seconds)
        self.text.prep_text(self.message)

    def draw(self):
        """Draws the timer on screen"""
        self.text.draw()

    def init_dynamic_variables(self):
        """Initializes the timers's dynamic variables"""
        self.total_seconds = 0
        self.minutes = 0
        self.seconds = 0
        self.message = "{0:02}:{1:02}".format(0, 0)
