# Import standard modules

# Import non-standard modules
import pygame

# Import local classes and methods


class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""

        # Color dictionary
        self.colors = {}
        self.colors["GREEN"] = (105, 189, 69)
        self.colors["RED"] = (170, 0, 0)
        self.colors["WHITE"] = (255, 255, 255)

        # Grid settings
        self.num_rows = 10
        self.num_cols = 10
        self.number_mines = int(self.num_rows * self.num_cols * 0.1)
        self.background_color = (251, 245, 243)

        # Cell settings
        self.cell_width = 40
        self.cell_height = 40
        self.cell_buffer = 8

        # Screen layout settings
        header_height = 70
        grid_height = ((self.cell_height + self.cell_buffer) * self.num_rows +
                       self.cell_buffer)
        grid_width = ((self.cell_width + self.cell_buffer) * self.num_cols +
                      self.cell_buffer)
        self.header_rect = pygame.Rect(0, 0, grid_width, header_height + 1)
        self.grid_rect = pygame.Rect(0, self.header_rect.bottom, grid_width,
                                     grid_height)
        self.screen_width = grid_width
        self.screen_height = header_height + grid_height

        # Header UI settings
        self.header_font = pygame.font.Font(
            "assets/fonts/Arial Rounded MT Bold.TTF", 36)
        self.header_font_color = self.colors["WHITE"]
        self.header_fill = (120, 120, 120)
        self.header_fill_win = self.colors["GREEN"]
        self.header_fill_lose = self.colors["RED"]

        # Flag images
        self.flag_images = []
        for i in range(1, 4):
            filepath = "assets/images/flag_{0:02}.png".format(i)
            self.flag_images.append(pygame.image.load(filepath))
        self.flag_counter_image = pygame.image.load(
            "assets/images/flag_counter.png")
        self.flag_counter_rect = self.flag_counter_image.get_rect()
        self.flag_counter_rect.midright = self.header_rect.center
        self.flag_counter_rect.centerx -= 110

        # Tile images
        self.number_images = []
        for i in range(0, 9):
            filepath = "assets/images/number_tile_{0:02}.png".format(i)
            self.number_images.append(pygame.image.load(filepath))
        self.covered_tile_images = []
        self.covered_tile_images.append(
            pygame.image.load("assets/images/blank_tile.png"))
        self.covered_tile_images.append(
            pygame.image.load("assets/images/blank_tile_hover.png"))
        self.flag_tile_images = []
        self.flag_tile_images.append(
            pygame.image.load("assets/images/flag_tile.png"))
        self.flag_tile_images.append(
            pygame.image.load("assets/images/flag_tile_hover.png"))

        # Mine images
        self.mine_image = pygame.image.load("assets/images/bomb.png")
        self.mine_image_clicked = pygame.image.load(
            "assets/images/bomb_clicked.png")
        self.mine_icon = pygame.image.load("assets/images/bomb_icon.png")

        # Timer images
        self.timer_image = pygame.image.load("assets/images/timer.png")
        self.timer_image_rect: pygame.Rect = self.timer_image.get_rect()
        self.timer_image_rect.centery = self.header_rect.centery
        self.timer_image_rect.left = self.header_rect.centerx + 10

        # Restart screen
        self.dimmer_max_opacity = 125

        # Success image
        self.success_image = pygame.image.load(
            "assets/images/game_over_success.png")
        self.success_image_rect = self.success_image.get_rect()
        self.success_image_rect.center = self.grid_rect.center
        self.success_image_rect.centery -= 50

        # Fail image
        self.failure_image = pygame.image.load(
            "assets/images/game_over_failure.png")
        self.failure_image_rect = self.failure_image.get_rect()
        self.failure_image_rect.center = self.grid_rect.center
        self.failure_image_rect.centery -= 50

        # New Game image
        self.new_game_image = pygame.image.load("assets/images/new_game.png")
        self.new_game_hover_image = pygame.image.load(
            "assets/images/new_game_hover.png")
        self.new_game_image_rect = self.new_game_image.get_rect()
        self.new_game_image_rect.midtop = self.success_image_rect.midbottom
        self.new_game_image_rect.centery -= 30
        self.new_game_button_rect = pygame.rect.Rect(0, 0, 282, 65)
        self.new_game_button_rect.center = self.new_game_image_rect.center

        # Audio settings
        self.sound_hover = pygame.mixer.Sound("assets/sounds/pop_short.wav")
        self.sound_click = pygame.mixer.Sound("assets/sounds/pop_long.wav")
        self.sound_cascade = pygame.mixer.Sound(
            "assets/sounds/pop_multiple.wav")
        self.sound_lose = pygame.mixer.Sound("assets/sounds/game_over.wav")
        self.sound_win = pygame.mixer.Sound("assets/sounds/success.wav")
        self.sound_flag_high = pygame.mixer.Sound(
            "assets/sounds/flag_high.wav")
        self.sound_flag_low = pygame.mixer.Sound("assets/sounds/flag_low.wav")
        self.sound_new_game = pygame.mixer.Sound("assets/sounds/new_game.wav")

        # Initialize dynamic variables
        self.init_dynamic_variables()

    def init_dynamic_variables(self):
        """Initializes the game's dynamic variables"""

        pygame.mixer.stop()
        pygame.mixer.Sound.play(self.sound_new_game)
        self.mines_flagged = 0
        self.dimmer_opacity = 0
        self.image_opacity = 0
        self.endgame_animating = False

        # Tracks if a game is currently in-progress or not (i.e. the timer is running)
        # 0 = inactive, 1 = active
        self.game_active = 0

        # Tracks if a game is won or lost
        # 1 = win, -1 = lose, 0 = game in progress (only if game_active)
        self.game_over = 0

    def initiate_endgame(self, win: bool):
        """Initiates the end game sequence and updates appropriate settings"""
        if win:
            self.game_over = 1
        else:
            self.game_over = -1
        self.game_active = 0
        self.endgame_animating = True
