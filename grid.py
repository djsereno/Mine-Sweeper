from cell import Cell
import pygame as pg


class Grid():
    """A class to represent the mine sweeper grid"""

    def __init__(self, settings):
        self.num_rows = settings.num_rows
        self.num_cols = settings.num_cols
        self.cells = []
        for row in range(self.num_rows):
            self.cells.append([])
            for col in range(self.num_cols):
                cell = Cell(settings, row, col)
                self.cells[row].append(cell)

    def click(self, row, col):
        if not self.cells[row][col].clicked:
            self.cells[row][col].clicked = True

    def draw(self, screen, settings):
        """Draws the grid on screen"""

        # Draw cells
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col].draw(screen, settings)

        # Draw horizontal borders
        for row in range(self.num_rows + 1):
            pg.draw.line(screen, settings.border_color,
                        (0, row * settings.cell_height),
                        (settings.screen_width, row * settings.cell_height),
                        settings.border_thick)
        
        # Draw vertical borders
        for col in range(self.num_cols + 1):
            pg.draw.line(screen, settings.border_color,
                        (col * settings.cell_width, 0),
                        (col * settings.cell_width, settings.screen_height),
                        settings.border_thick)