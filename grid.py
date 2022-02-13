# Import standard modules
import sys

# Import non-standard modules
import pygame
import random

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

        # Create the cells within the grid
        for row in range(self.num_rows):
            self.cells.append([])
            for col in range(self.num_cols):

                width = settings.cell_width
                height = settings.cell_height
                x = self.rect.left + col * width
                y = self.rect.top + row * height
                cell_rect = pygame.Rect(x, y, width, height)
                cell = Cell(screen, settings, cell_rect, row, col)
                self.cells[row].append(cell)

        # Randomly place the mines within the grid
        self.place_mines(settings)

    def reset(self, settings):
        """Reset the grid for a new game"""

        # Reinitialize the cells
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell: Cell = self.cells[row][col]
                cell.init_dynamic_variables()

        # Place new mines throughout the grid
        self.place_mines(settings)

    def click(self, settings: Settings, row: int, col: int):
        """Sets cell clicked status to True if False and handles cascades as occurs"""
        cell: Cell = self.cells[row][col]
        if not cell.clicked:
            cell.clicked = True

            # Update the mine counter if clicking a flagged cell
            if cell.flag == 1:
                settings.mines_flagged -= 1

            # End the game if clicking a mine
            if cell.mine:
                settings.game_over = -1
                settings.game_active = 0

            # Click surrounding cells if adjacent mines is 0
            elif cell.adjacent_mines == 0:

                # Check cells in the surrounding 3x3 grid
                for row_off in range(-1, 2):
                    for col_off in range(-1, 2):
                        next_row = row + row_off
                        next_col = col + col_off

                        # Only check cells within the grid
                        if next_row >= 0 and next_row < self.num_rows and next_col >= 0 and next_col < self.num_cols:
                            self.click(settings, next_row, next_col)

            # Check if the game has ended
            self.check_game_over(settings)

    def flag(self, settings: Settings, row: int, col: int):
        """Flags the current cell"""
        cell = self.cells[row][col]

        # Alternate the flag of the cell (nothing, unknown, or mine)
        if not cell.clicked:
            cell.flag = (cell.flag + 1) % 3

            # Update the flag counter
            if cell.flag == 1:
                settings.mines_flagged += 1
            elif cell.flag == 2:
                settings.mines_flagged -= 1

    def place_mines(self, settings: Settings):
        """Randomly scatters mines throughout the grid"""

        # Place mines throughout the grid
        for i in range(settings.number_mines):
            while True:
                row = random.randint(0, self.num_rows - 1)
                col = random.randint(0, self.num_cols - 1)
                cell = self.cells[row][col]
                if not cell.mine:
                    cell.mine = True
                    break

        # Update the cell adjacent mine counts
        self.update_mine_counts()

    def update_mine_counts(self):
        """Counts the adjacent mines for each cell and updates the adjacent_mines property"""

        for row in range(self.num_rows):
            for col in range(self.num_cols):

                cell = self.cells[row][col]

                # Only update for cells that don't contain mines
                if not cell.mine:
                    num_mines = 0

                    # Check cells in the surrounding 3x3 grid
                    for row_off in range(-1, 2):
                        for col_off in range(-1, 2):
                            new_row = cell.row + row_off
                            new_col = cell.col + col_off

                            # Only check cells within the grid
                            if new_row >= 0 and new_row < self.num_rows and new_col >= 0 and new_col < self.num_cols:
                                if self.cells[new_row][new_col].mine:
                                    num_mines += 1

                    cell.adjacent_mines = num_mines

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
            settings.game_over = 1
            settings.game_active = 0
            return True

    def draw(self, settings: Settings):
        """Draws the grid on screen"""

        # Draw cells
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col].draw(settings)

        # Draw horizontal borders
        for row in range(self.num_rows + 1):
            pygame.draw.line(
                self.screen, settings.border_color,
                (self.rect.left, self.rect.top + row * settings.cell_height),
                (self.rect.right, self.rect.top + row * settings.cell_height),
                settings.border_thick)

        # Draw vertical borders
        for col in range(self.num_cols + 1):
            pygame.draw.line(self.screen, settings.border_color,
                             (col * settings.cell_width, self.rect.top),
                             (col * settings.cell_width, self.rect.bottom),
                             settings.border_thick)

    def get_index(self, mouse_pos: tuple):
        """Returns the (col, row) for a given (x, y)"""
        (x, y) = mouse_pos
        width, height = self.rect.width, self.rect.height
        num_rows, num_cols = self.num_rows, self.num_cols
        row = int((y - self.rect.top) / height * num_rows)
        col = int(x / width * num_cols)
        return (row, col)