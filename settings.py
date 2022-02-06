YELLOW = (255, 215, 0)
ORANGE = (255, 165, 0)
RED = (255, 69, 0)
PURPLE = (138, 43, 226)
MAROON = (128, 0, 0)


class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 600

        # Grid settings
        self.num_rows = 20
        self.num_cols = 20
        self.border_thick = 2

        # Cell settings
        self.cell_width = int(self.screen_width / self.num_cols)
        self.cell_height = int(self.screen_height / self.num_rows)
        self.screen_width = self.cell_width * self.num_cols + self.border_thick
        self.screen_height = self.cell_height * self.num_rows + self.border_thick

        # Color settings
        self.cell_unclicked = (225, 225, 225)
        self.cell_clicked = (145, 145, 145)
        self.border_color = (60, 60, 60)
        self.mine_color = (60, 60, 60)
        self.number_color = [YELLOW, ORANGE, RED, PURPLE, MAROON]
