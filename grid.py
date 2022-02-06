from cell import Cell


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