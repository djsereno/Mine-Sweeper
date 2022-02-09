# Import standard modules
import sys

# Import non-standard modules
import pygame
import random

# Import local classes and methods
from cell import Cell
from grid import Grid
from settings import Settings

class Timer():
    """A class to represent the in game timer"""

    def __init__(self, settings: Settings) -> None:
        self.total_seconds = 0
        self.string = "{0:02}:{1:02}".format(0, 0)
        self.font = pygame.font.SysFont("Consolas", settings.cell_font_size)

    def update(self, dt):
        """Increments the current timer value by dt"""
        self.total_seconds += dt / 1000
        minutes = int(self.total_seconds // 60)
        seconds = int(self.total_seconds % 60)
        self.string = "{0:02}:{1:02}".format(minutes, seconds)

    def draw(self, screen: pygame.Surface, settings: Settings):
        """Draws the timer on screen"""
        text = self.font.render(self.string, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = screen.get_rect().topright
        screen.blit(text, text_rect)
