# Import standard modules

# Import non-standard modules
import pygame

# Import local classes and methods


class Text_Image():

    def __init__(self, message: str, screen: pygame.Surface,
                 font: pygame.font.Font, color: pygame.Color):
        """Initialize text attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Text properties
        self.text_color = color
        self.font = font
        self.prep_text(message)

    def prep_text(self, message: str):
        """Turn message into a rendered image"""
        self.text_image = self.font.render(message, True, self.text_color)
        self.text_image_rect = self.text_image.get_rect()

    def draw(self):
        """Draw the text image to the screen"""
        self.screen.blit(self.text_image, self.text_image_rect)
