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
from text import Text


class Timer():
    """A class to represent the in game timer"""

    def __init__(self, screen: pygame.Surface, settings: Settings) -> None:
        """Initialize the timer"""

        # Timer properties
        self.total_seconds = 0
        self.message = "{0:02}:{1:02}".format(0, 0)

        # Timer text image
        self.text = Text(self.message, screen, settings.header_font_type,
                         settings.header_font_size, settings.header_font_color)

    def update(self, dt):
        """Increments the current timer value by dt and updates the timer text"""
        self.total_seconds += dt / 1000
        minutes = int(self.total_seconds // 60)
        seconds = int(self.total_seconds % 60)

        # Update the timer message and text image
        self.message = "{0:02}:{1:02}".format(minutes, seconds)
        self.text.prep_text(self.message)

    def draw(self):
        """Draws the timer on screen"""
        self.text.text_image_rect.topright = self.text.screen_rect.topright
        self.text.draw()
