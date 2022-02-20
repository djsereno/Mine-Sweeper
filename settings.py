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

        # Layout settings
        header_height = 70
        grid_height = (self.cell_height +
                       self.cell_buffer) * self.num_rows + self.cell_buffer
        grid_width = (self.cell_width +
                      self.cell_buffer) * self.num_cols + self.cell_buffer
        self.header_rect = pygame.Rect(0, 0, grid_width, header_height + 1)
        self.grid_rect = pygame.Rect(0, self.header_rect.bottom, grid_width,
                                     grid_height)

        # Flag images
        self.flag_images = []
        for i in range(1, 4):
            filepath = "images/flag_{0:02}.png".format(i)
            self.flag_images.append(pygame.image.load(filepath))
        self.flag_image_width = self.cell_width
        self.flag_image_height = self.cell_height
        
        self.flag_counter_image = pygame.image.load("images/flag_counter.png")
        self.flag_counter_rect = self.flag_counter_image.get_rect()
        self.flag_counter_rect.midright = self.header_rect.center
        self.flag_counter_rect.centerx -= 110

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
        self.mine_icon = pygame.image.load("images/bomb_icon.png")

        # Timer images
        self.timer_image = pygame.image.load("images/timer.png")
        self.timer_image_rect: pygame.Rect = self.timer_image.get_rect()
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

        # Audio settings
        self.sound_hover = pygame.mixer.Sound("sounds/pop_short.wav")
        self.sound_click = pygame.mixer.Sound("sounds/pop_long.wav")
        self.sound_cascade = pygame.mixer.Sound("sounds/pop_multiple.wav")
        self.sound_lose = pygame.mixer.Sound("sounds/game_over.wav")
        self.sound_win = pygame.mixer.Sound("sounds/success.wav")
        self.sound_flag_high = pygame.mixer.Sound("sounds/flag_high.wav")
        self.sound_flag_low = pygame.mixer.Sound("sounds/flag_low.wav")
        self.sound_new_game = pygame.mixer.Sound("sounds/new_game.wav")
        

        self.init_dynamic_variables()

    def init_dynamic_variables(self):
        """Initializes the game's dynamic variables"""

        pygame.mixer.stop()
        pygame.mixer.Sound.play(self.sound_new_game)
        self.mines_flagged = 0

        # game_active tracks if a game is currently in-progress or not
        # 0 = inactive, 1 = active
        self.game_active = 0

        # game_over tracks if a game is won or lost
        # 1 = win, -1 = lose, 0 = game in progress
        self.game_over = 0
