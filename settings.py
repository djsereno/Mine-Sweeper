import pygame


class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""

        # Color dictionary
        self.colors = {}
        self.colors["BLUE"] = (0, 20, 130)
        self.colors["GREEN"] = (40, 115, 20)
        self.colors["RED"] = (170, 0, 0)
        self.colors["PURPLE"] = (100, 15, 140)
        self.colors["MAROON"] = (90, 0, 0)
        self.colors["WHITE"] = (255, 255, 255)

        # Grid settings
        self.num_rows = 3
        self.num_cols = 10
        self.border_thick = 1
        self.number_mines = int(self.num_rows * self.num_cols * 0.1)

        # Cell settings
        self.cell_width = 40
        self.cell_height = 40
        self.cell_buffer = 8
        self.cell_font_type = "Berlin Sans FB"
        self.cell_font_size = int(self.cell_height * 0.9)

        # Flag images
        self.flag_images = []
        for i in range(1, 4):
            filepath = "images/flag_{0:02}.png".format(i)
            self.flag_images.append(pygame.image.load(filepath))
        self.flag_image_width = self.cell_width
        self.flag_image_height = self.cell_height

        # Tile images
        self.number_images = []
        for i in range(0, 9):
            filepath = "images/number_tile_{0:02}.png".format(i)
            self.number_images.append(pygame.image.load(filepath))
        self.unclicked_tile_image = pygame.image.load("images/blank_tile.png")
        self.hover_tile_image = pygame.image.load(
            "images/blank_tile_hover.png")

        # Mine images
        self.mine_image = pygame.image.load("images/bomb.png")
        self.mine_image_clicked = pygame.image.load("images/bomb_clicked.png")

        # self.flag_image_width = self.cell_width
        # self.flag_image_height = self.cell_height
        # for i in range(len(self.flag_images)):
        # self.flag_images[i] = pygame.transform.scale(
        #     self.flag_images[i],
        #     (self.flag_image_width, self.flag_image_height))

        # Layout settings
        header_height = 70
        grid_height = (self.cell_height +
                       self.cell_buffer) * self.num_rows + self.cell_buffer
        grid_width = (self.cell_width +
                      self.cell_buffer) * self.num_cols + self.cell_buffer
        self.header_rect = pygame.Rect(0, 0, grid_width, header_height + 1)
        self.grid_rect = pygame.Rect(0, self.header_rect.bottom, grid_width,
                                     grid_height)

        # Timer images
        self.timer_images = []
        for i in range(0, 12):
            filepath = "images/timer_{0:02}.png".format(i)
            self.timer_images.append(pygame.image.load(filepath))
        self.timer_image_rect: pygame.Rect = self.timer_images[0].get_rect()
        self.timer_image_rect.centery = self.header_rect.centery
        self.timer_image_rect.left = self.header_rect.centerx + 10

        # Screen settings
        self.screen_width = grid_width
        self.screen_height = header_height + grid_height

        # UI settings
        self.header_font_type = "Arial Rounded MT Bold"
        self.header_font_size = 50
        self.header_font_color = self.colors["WHITE"]
        self.header_fill = (120, 120, 120)
        self.header_fill_win = self.colors["GREEN"]
        self.header_fill_lose = self.colors["RED"]

        # Color settings
        self.background_color = (251, 245, 243)
        self.cell_unclicked = (225, 225, 225)
        self.cell_clicked = (145, 145, 145)
        self.cell_game_won = (165, 215, 170)
        self.cell_game_lost = (255, 175, 185)
        self.border_color = (60, 60, 60)
        self.mine_color = (60, 60, 60)
        self.number_color = [
            self.colors["BLUE"], self.colors["GREEN"], self.colors["RED"],
            self.colors["PURPLE"], self.colors["MAROON"]
        ]
        self.flag_mine = self.colors["RED"]
        self.flag_question = self.colors["BLUE"]

        self.init_dynamic_variables()

    def init_dynamic_variables(self):
        """Initializes the game's dynamic variables"""

        self.mines_flagged = 0

        # game_active tracks if a game is currently in-progress or not
        # 0 = inactive, 1 = active
        self.game_active = 0

        # game_over tracks if a game is won or lost
        # 1 = win, -1 = lose, 0 = game in progress
        self.game_over = 0
