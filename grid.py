# Import standard modules
import sys

# Import non-standard modules
import pygame, random

# Import local classes and methods
from cell import Cell
from settings import Settings


class Grid():
    """A class to represent the mine sweeper grid"""

    def __init__(self, screen: pygame.Surface, settings: Settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Initialize the grid
        self.num_rows = settings.num_rows
        self.num_cols = settings.num_cols
        self.rect = settings.grid_rect
        self.cells = []
        self.prev_index = [-1, -1]

        # Create the cells within the grid
        for row in range(self.num_rows):
            self.cells.append([])
            for col in range(self.num_cols):

                buffer = settings.cell_buffer
                width = settings.cell_width
                height = settings.cell_height
                x = self.rect.left + col * (width + buffer) + buffer
                y = self.rect.top + row * (height + buffer) + buffer
                cell_rect = pygame.Rect(x, y, width, height)
                cell = Cell(screen, settings, cell_rect, row, col)
                self.cells[row].append(cell)

        # Randomly place the mines within the grid
        self.place_mines(settings)

    def place_mines(self, settings: Settings):
        """Randomly scatters mines throughout the grid"""

        # Place mines throughout the grid
        for i in range(settings.number_mines):
            while True:
                row = random.randint(0, self.num_rows - 1)
                col = random.randint(0, self.num_cols - 1)
                cell: Cell = self.cells[row][col]
                if not cell.mine:
                    cell.mine = True
                    break

        # Update the cell adjacent mine counts
        self.update_mine_counts(settings)

    def update_mine_counts(self, settings: Settings):
        """Counts the adjacent mines for each cell and updates the adjacent_mines property"""

        # Check each cell within the grid
        for row in range(self.num_rows):
            for col in range(self.num_cols):

                cell: Cell = self.cells[row][col]

                # Only update for cells that don't contain mines
                if not cell.mine:
                    num_mines = 0

                    # Check cells in the surrounding 3x3 grid
                    for row_off in range(-1, 2):
                        for col_off in range(-1, 2):
                            new_row = cell.row + row_off
                            new_col = cell.col + col_off

                            # Only check cells within the grid
                            if (new_row >= 0 and new_row < self.num_rows
                                    and new_col >= 0
                                    and new_col < self.num_cols
                                    and self.cells[new_row][new_col].mine):

                                num_mines += 1

                    cell.adjacent_mines = num_mines
                    cell.clicked_tile_image = settings.number_images[num_mines]

    def reset(self, settings):
        """Reset the grid for a new game"""

        # Reinitialize the cells
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell: Cell = self.cells[row][col]
                cell.init_dynamic_variables(settings)

        # Place new mines throughout the grid
        self.place_mines(settings)

    def click(self, settings: Settings, row: int, col: int, play_audio: bool):
        """Sets cell clicked status to True if False and handles cascades as occurs"""

        # Cascade variable used to check if a cascade has been triggered
        # (i.e. a cell with no adjacent mines has been clicked). A different
        # sound effects are used for cascades
        cascade = False
        cell: Cell = self.cells[row][col]

        if not cell.clicked:
            cell.clicked = True

            # Update the mine counter if clicking a flagged cell
            if cell.flag == 1:
                settings.mines_flagged -= 1

            # End the game if clicking a mine
            if cell.mine:
                settings.initiate_endgame(False)
                pygame.mixer.Sound.play(settings.sound_lose)

            # Click surrounding cells if adjacent mines is 0
            elif cell.adjacent_mines == 0:

                # Check cells in the surrounding 3x3 grid
                for row_off in range(-1, 2):
                    for col_off in range(-1, 2):
                        next_row = row + row_off
                        next_col = col + col_off

                        # Only check cells within the grid
                        if next_row >= 0 and next_row < self.num_rows and next_col >= 0 and next_col < self.num_cols:
                            cascade = True
                            self.click(settings, next_row, next_col, False)

            # Play audio
            if play_audio:
                if cascade:
                    pygame.mixer.Sound.play(settings.sound_cascade)
                else:
                    pygame.mixer.Sound.play(settings.sound_click)

            # Check if the game has ended
            self.check_game_over(settings)

    def flag(self, settings: Settings, row: int, col: int, flag: int):
        """Flags the current cell as either a mine or unknown"""

        cell = self.cells[row][col]

        # Change the flag of the cell
        if not cell.clicked:

            # Right clicked (mine flag)
            if flag == 1:
                if cell.flag == 1:
                    cell.flag = 0
                    settings.mines_flagged -= 1
                else:
                    cell.flag = 1
                    settings.mines_flagged += 1

            # Middle clicked (question flag)
            elif flag == 2:
                if cell.flag == 2:
                    cell.flag = 0
                else:
                    if cell.flag == 1:
                        settings.mines_flagged -= 1
                    cell.flag = 2

            # Play sound effects if a flag is being added or removed
            if cell.flag == 0:
                pygame.mixer.Sound.play(settings.sound_flag_low)
            else:
                pygame.mixer.Sound.play(settings.sound_flag_high)

    def check_game_over(self, settings: Settings):
        """Returns True and updates the grid state if the game is over, False otherwise"""
        if settings.game_active:

            # Game is over when all non-mine cells have been clicked
            # or a mine has been clicked
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    cell = self.cells[row][col]

                    # Check if a non-mine cell is still unclicked
                    if not cell.clicked and not cell.mine:
                        return False

            # All mines are unclicked and all non-mines are clicked, game won
            settings.mines_flagged = settings.number_mines
            settings.initiate_endgame(True)
            pygame.mixer.Sound.play(settings.sound_win)
            return True

    def draw(self, settings: Settings, mouse_pos: tuple):
        """Draws the grid on screen"""

        # Get the cell index at the cursor to trigeger sound effects and highlighting
        i, j = None, None
        if self.rect.collidepoint(mouse_pos):
            [i, j] = self.get_index(mouse_pos)

            # Play sound when hovering over a new cell
            if ([i, j] != self.prev_index and [i, j] != [-1, -1]
                    and not settings.game_over
                    and not self.cells[i][j].clicked):

                pygame.mixer.Sound.play(settings.sound_hover)

            self.prev_index = [i, j]

        # Draw cells
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if row == i and col == j:
                    self.cells[row][col].draw(settings, True)
                else:
                    self.cells[row][col].draw(settings, False)

    def get_index(self, mouse_pos: tuple):
        """Returns the (col, row) for a given (x, y)"""

        # Loop through each cell and check for rect collisions
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.cells[row][col].rect.collidepoint(mouse_pos):
                    return (row, col)
        return (-1, -1)
