import pygame
import copy

class TetrisGrid:
    """ Class representing overall grid """
    def __init__(self, screen, width, height, cell_size, empty=0) -> None:
        # Construct grid 
        self.screen = screen
        self.cols = width//cell_size
        self.rows = height//cell_size
        self._grid = [([empty for _ in range(self.rows)]) for _ in range(self.cols)]
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.start_x = (screen.get_rect().width - self.width)/2
        self.start_y = (screen.get_rect().height - self.height)/2
        self.empty = empty

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

    def _color_cell(self, color, row_index, col_index,):
        pygame.draw.rect(self.screen, color, pygame.Rect(self.start_x + row_index * self.cell_size, 
                                                              self.start_y + col_index * self.cell_size, self.cell_size - 1, self.cell_size -1)) 
        
    def is_valid_move(self, block, row, col, rotation):

        block_tryout = copy.deepcopy(block)
        block_tryout.row += row
        block_tryout.col += col
        if rotation:
            block_tryout.rotate_clockwise()
        
        for row_index, row in enumerate(block_tryout.pattern):
            for col_index, col_value in enumerate(row):
                grid_row_index = block_tryout.row + row_index
                grid_col_index = block_tryout.col + col_index

                if col_value == 'x':
                    # left-border: grid_indices not smaller than 0
                    if grid_row_index < 0 or grid_col_index < 0:
                        return False
                    # right-border: grid_col_index not greater than self.cols
                    if grid_row_index >= self.rows or grid_col_index >= self.cols:
                        return False
                    # or if cell is not empty
                    if self._grid[grid_row_index][grid_col_index] != self.empty:
                        return False
        # otherwise its ok!
        return True
    