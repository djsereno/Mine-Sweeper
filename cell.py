import pygame as pg
import game_functions as gf


class Cell():
    """A class to represent the cells within the mine sweeper grid"""

    def __init__(self, settings, row, col):
        """Initialize the cell's settings"""
        self.width = settings.cell_width
        self.height = settings.cell_height
        self.row = row
        self.col = col
        self.clicked = False
        self.mine = False
        # self.neighbors = self.getNeighbors(settings)
        self.rect = pg.Rect(self.col * self.width, self.row * self.height,
                            self.width, self.height)

    def getNeighbors(self, settings):
        """Returns a dictionary containing the indices of the neighboring cells.
        Neighbors which fall beyond the grid edge evaluate as None"""
        neighbors = {}
        neighbors['top'] = gf.getIndex(self.row - 1, self.col,
                                       settings.numRows, settings.numCols)
        neighbors['bottom'] = gf.getIndex(self.row + 1, self.col,
                                          settings.numRows, settings.numCols)
        neighbors['left'] = gf.getIndex(self.row, self.col - 1,
                                        settings.numRows, settings.numCols)
        neighbors['right'] = gf.getIndex(self.row, self.col + 1,
                                         settings.numRows, settings.numCols)
        return neighbors

    def draw(self, screen, settings):
        """Draws the cell on the screen"""
        if self.clicked:
            fill = settings.cell_clicked
        else:
            fill = settings.cell_unclicked
        pg.draw.rect(screen, fill, self.rect)