from cell import Cell
import pygame
import random


class Grid():
    """A class to represent the mine sweeper grid"""

    def __init__(self, settings):
        self.num_rows = settings.num_rows
        self.num_cols = settings.num_cols
        self.rect = pygame.Rect(0, settings.header_height, settings.screen_width, settings.screen_height - settings.header_height)
        self.cells = []
        for row in range(self.num_rows):
            self.cells.append([])
            for col in range(self.num_cols):
                cell = Cell(settings, self, row, col)
                self.cells[row].append(cell)
        self.place_mines(settings)
        self.gameover = 0
        
    def click(self, row, col):
        """Sets cell clicked status to True if False and handles cascades as occurs"""
        cell = self.cells[row][col]
        if not cell.clicked:
            cell.clicked = True

            if cell.mine:
                self.gameover = -1

            # Click surrounding cells if adjacent mines is 0
            elif cell.adjacent_mines == 0:

                # Check cells in the surrounding 3x3 grid
                for row_off in range(-1, 2):
                    for col_off in range(-1, 2):
                        next_row = row + row_off
                        next_col = col + col_off

                        # Only check cells within the grid
                        if next_row >= 0 and next_row < self.num_rows and next_col >= 0 and next_col < self.num_cols:
                            self.click(next_row, next_col)

            # Check if the game has ended
            self.check_gameover()

    def flag(self, row, col):
        """Flags the current cell"""
        cell = self.cells[row][col]
        if not cell.clicked:
            cell.flag = (cell.flag + 1) % 3

    def place_mines(self, settings):
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
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col].count_mines(self)

    def check_gameover(self):
        """Returns True and updates the grid state if the game is over, False otherwise"""
        if not self.gameover:

            # Game is over when all non-mine cells have been clicked
            # or a mine has been clicked
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    cell = self.cells[row][col]

                    # Check if a non-mine cell is still unclicked
                    if not cell.clicked and not cell.mine:
                        return False

            # All mines are unclicked and all non-mines are clicked, game won
            self.gameover = 1
            return True

    def draw(self, screen, settings):
        """Draws the grid on screen"""

        # Draw cells
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col].draw(screen, self, settings)

        # Draw horizontal borders
        for row in range(self.num_rows + 1):
            pygame.draw.line(
                screen, settings.border_color, (self.rect.left, self.rect.top + row * settings.cell_height),
                (self.rect.right, self.rect.top + row * settings.cell_height),
                settings.border_thick)

        # Draw vertical borders
        for col in range(self.num_cols + 1):
            pygame.draw.line(
                screen, settings.border_color, (col * settings.cell_width, self.rect.top),
                (col * settings.cell_width, self.rect.bottom),
                settings.border_thick)

    def get_index(self, pos):
        """Returns the (col, row) for a given (x, y)"""
        (x, y) = pos
        width, height = self.rect.width, self.rect.height
        num_rows, num_cols = self.num_rows, self.num_cols
        row = int((y - self.rect.top) / height * num_rows)
        col = int(x / width * num_cols)
        return (row, col)