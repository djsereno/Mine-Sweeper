# Import standard modules
import sys

# Import non-standard modules
import pygame
import random

# Import local classes and methods
from cell import Cell
from grid import Grid
from settings import Settings


class Text():

    def __init__(self, message: str, screen: pygame.Surface, font_type: str,
                 font_size: int, color: pygame.Color):
        """Initialize text attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Text properties
        self.text_color = color
        self.font = pygame.font.SysFont(font_type, font_size)
        self.prep_text(message)

    def prep_text(self, message: str):
        """Turn message into a rendered image"""
        self.text_image = self.font.render(message, True, self.text_color)
        self.text_image_rect = self.text_image.get_rect()

    def draw(self):
        # Draw blank button and then draw the message
        self.screen.blit(self.text_image, self.text_image_rect)
