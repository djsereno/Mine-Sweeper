# Import standard modules
import sys

# Import non-standard modules
import pygame
import random

# Import local classes and methods
from settings import Settings


class Cell():
    """A class to represent the cells within the mine sweeper grid"""

    def __init__(self, screen: pygame.Surface, settings: Settings, grid_rect: pygame.Rect, row: int, col: int):
        """Initialize the cell's settings"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()        
        
        # Cell properties
        self.row = row
        self.col = col
        self.clicked = False
        self.flag = 0
        self.mine = False
        self.adjacent_mines = -1
        self.image = None

        # Drawing properties
        self.width = settings.cell_width
        self.height = settings.cell_height
        self.rect = pygame.Rect(self.col * self.width, self.row * self.height + grid_rect.top,
                                self.width, self.height)

    def draw(self, settings: Settings):
        """Draws the cell on the screen"""

        # Background color
        if settings.gameover == -1:
            bg_fill = settings.cell_game_lost
        elif settings.gameover == 1:
            bg_fill = settings.cell_game_won
        elif self.clicked:
            bg_fill = settings.cell_clicked
        else:
            bg_fill = settings.cell_unclicked
        pygame.draw.rect(self.screen, bg_fill, self.rect)

        # Mines or numbers
        if self.clicked or settings.gameover:

            # Mine
            if self.mine:
                # self.image = pygame.image.load('images/bomb_color.png')
                # self.image = pygame.transform.scale(self.image, (self.width, self.width))
                # screen.blit(self.image, self.rect)
                mine_fill = settings.mine_color
                radius = int(self.width * 0.3)
                pygame.draw.circle(self.screen, mine_fill, self.rect.center, radius)
                pygame.draw.circle(self.screen, (0, 0, 0), self.rect.center, radius,
                                   1)

            # Adjacent mines number
            elif self.adjacent_mines > 0:
                num_mines = self.adjacent_mines
                if num_mines <= len(settings.number_color):
                    font_color = settings.number_color[num_mines - 1]
                else:
                    font_color = settings.number_color[-1]

                type = settings.cell_font_type
                size = settings.cell_font_size
                font = pygame.font.SysFont(type, size)
                text = font.render(str(num_mines), True, font_color)
                text_rect = text.get_rect()
                text_rect.center = self.rect.center

                # Adjust font so that it is actually centered
                descent = font.get_descent()
                text_rect.centery += descent / 2
                self.screen.blit(text, text_rect)

        # Flags
        elif not self.clicked and self.flag != 0 and not settings.gameover:
            type = settings.cell_font_type
            size = settings.cell_font_size
            font = pygame.font.SysFont(type, size)

            # Mine flag
            if self.flag == 1:
                font_color = settings.flag_mine
                text = font.render("!!!", True, font_color)
                text_rect = text.get_rect()
                text_rect.center = self.rect.center

            # Question flag
            elif self.flag == 2:
                font_color = settings.flag_question
                text = font.render("?", True, font_color)
                text_rect = text.get_rect()
                text_rect.center = self.rect.center

            self.screen.blit(text, text_rect)
