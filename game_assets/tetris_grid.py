import pygame

class TetrisGrid:
    """ Class representing overall grid """
    def __init__(self, screen, width, height, cell_size, empty=0) -> None:
        # Construct grid 
        self.screen = screen
        self._grid = [([empty for _ in range(height//cell_size)]) for _ in range(width//cell_size)]
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.start_x = (screen.get_rect().width - self.width)/2
        self.start_y = (screen.get_rect().height - self.height)/2

    def setCell(self, row, col, value):
        self._grid[row][col] = value

    def getCell(self, row, col):
        return self._grid[row][col]
    
    def draw(self, block=None):
        for row_index, row in enumerate(self._grid):
            for col_index, col_value in enumerate(row):
                if col_value != 0:
                    self._color_cell(col_value, row_index, col_index)
        if block:
            for row_index, row in enumerate(block.pattern):
                for col_index, col_value in enumerate(row):
                    if col_value == 'x':
                        self._color_cell(block.color, block.col + col_index, block.row + row_index)

    def _color_cell(self, color, col_index, row_index,):
        pygame.draw.rect(self.screen, color, pygame.Rect(self.start_x + col_index * self.cell_size, 
                                                              self.start_y + row_index * self.cell_size, self.cell_size - 1, self.cell_size -1)) 
    