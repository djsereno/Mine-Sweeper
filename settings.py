from pygame import BLEND_MULT


BLUE = (3, 107, 252)
GREEN = (0, 191, 32)
RED = (196, 31, 31)
PURPLE = (116, 34, 199)
MAROON = (128, 0, 0)


class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""

        # Grid settings
        self.num_rows = 15
        self.num_cols = 30
        self.border_thick = 2

        # Cell settings
        self.cell_width = 30
        self.cell_height = 30

        # Screen settings
        self.screen_width = self.cell_width * self.num_cols + self.border_thick
        self.screen_height = self.cell_height * self.num_rows + self.border_thick

        # Color settings
        self.cell_unclicked = (225, 225, 225)
        self.cell_clicked = (145, 145, 145)
        self.border_color = (60, 60, 60)
        self.mine_color = (60, 60, 60)
        self.number_color = [BLUE, GREEN, RED, PURPLE, MAROON]
