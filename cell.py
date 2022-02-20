# Import standard modules

# Import non-standard modules
import pygame

# Import local classes and methods
from settings import Settings


class Cell():
    """A class to represent the cells within the mine sweeper grid"""

    def __init__(self, screen: pygame.Surface, settings: Settings,
                 cell_rect: pygame.Rect, row: int, col: int):
        """Initialize the cell's settings"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Cell properties
        self.row = row
        self.col = col

        # Drawing properties
        self.width = settings.cell_width
        self.height = settings.cell_height
        self.rect = cell_rect

        # Image properties
        self.covered_tile_images = settings.covered_tile_images
        self.flag_tile_images = settings.flag_tile_images
        self.tile_image_rect = self.covered_tile_images[0].get_rect()
        self.tile_image_rect.center = self.rect.center

        self.flag_images = settings.flag_images
        self.flag_image_rect = settings.flag_images[0].get_rect()
        self.flag_image_rect.center = self.rect.center

        # Initialize dynamic cell properties
        self.init_dynamic_variables(settings)

    def init_dynamic_variables(self, settings: Settings):
        """Initializes the cells's dynamic variables"""
        self.clicked = False
        self.flag = 0
        self.mine = False
        self.adjacent_mines = -1
        self.clicked_tile_image = settings.number_images[0]

    def draw(self, settings: Settings, hovered: bool):
        """Draws the cell on the screen"""

        # Tile image
        if self.clicked or settings.game_over:
            self.screen.blit(self.clicked_tile_image, self.tile_image_rect)
        else:
            if hovered:
                if self.flag:
                    self.screen.blit(self.flag_tile_images[1],
                                     self.tile_image_rect)
                else:
                    self.screen.blit(self.covered_tile_images[1],
                                     self.tile_image_rect)
            else:
                if self.flag:
                    self.screen.blit(self.flag_tile_images[0],
                                     self.tile_image_rect)
                else:
                    self.screen.blit(self.covered_tile_images[0],
                                     self.tile_image_rect)

        # Reveal mines or green flags
        if self.mine and settings.game_over:

            # Reveal mines if game lost
            if settings.game_over == -1:
                if self.clicked:
                    self.screen.blit(settings.mine_image_clicked,
                                     self.tile_image_rect)
                else:
                    self.screen.blit(settings.mine_image, self.tile_image_rect)

            # Reveal green flags if game won
            elif settings.game_over == 1:
                self.screen.blit(self.flag_images[2], self.flag_image_rect)

        # Flags
        elif not self.clicked and self.flag != 0 and settings.game_active:

            # Mine flag
            if self.flag == 1:
                self.screen.blit(self.flag_images[0], self.flag_image_rect)

            # Question flag
            elif self.flag == 2:
                self.screen.blit(self.flag_images[1], self.flag_image_rect)
