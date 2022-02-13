BLUE = (0, 20, 130)
GREEN = (40, 115, 20)
RED = (170, 0, 0)
PURPLE = (100, 15, 140)
MAROON = (90, 0, 0)
WHITE = (255, 255, 255)


class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""

        # Grid settings
        self.num_rows = 10
        self.num_cols = 10
        self.border_thick = 1
        self.number_mines = int(self.num_rows * self.num_cols * 0.1)

        # Cell settings
        self.cell_width = 30
        self.cell_height = 30
        self.cell_font_type = "Berlin Sans FB"
        self.cell_font_size = int(self.cell_height * 0.9)

        # Screen settings
        self.header_height = 50
        self.screen_width = self.cell_width * self.num_cols + self.border_thick
        self.screen_height = self.cell_height * self.num_rows + self.border_thick + self.header_height

        # UI settings
        self.header_font_type = "Consolas"
        self.header_font_size = 40
        self.header_font_color = WHITE

        # Color settings
        self.cell_unclicked = (225, 225, 225)
        self.cell_clicked = (145, 145, 145)
        self.cell_game_won = (165, 215, 170)
        self.cell_game_lost = (255, 175, 185)
        self.border_color = (60, 60, 60)
        self.mine_color = (60, 60, 60)
        self.number_color = [BLUE, GREEN, RED, PURPLE, MAROON]
        self.flag_mine = RED
        self.flag_question = BLUE

        self.init_dynamic_variables()

    def init_dynamic_variables(self):
        """Initializes the game's dynamic variables"""
        self.gameover = 0
