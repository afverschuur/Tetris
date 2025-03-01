import pygame
import copy

class TetrisGrid:
    """ Class representing overall grid """
    def __init__(self, game_base, width, height, cell_size, empty=0) -> None:
        # Construct grid 
        self.game_base = game_base
        self.cols = width//cell_size
        self.rows = height//cell_size
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.start_x = (self.game_base.settings.screen_width - self.width)/2
        self.start_y = (self.game_base.settings.screen_height - self.height)/2 + 80
        self.empty = empty
        self.reset_grid()
    
    def reset_grid(self):
        self._grid = [([self.empty for _ in range(self.cols)]) for _ in range(self.rows)]

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
                        self._color_cell(block.color, block.row + row_index, block.col + col_index)

    def _color_cell(self, color, row_index, col_index,):
        pygame.draw.rect(self.game_base.screen, color, pygame.Rect(self.start_x + col_index * self.cell_size, 
                                                              self.start_y + row_index * self.cell_size, self.cell_size - 1, self.cell_size -1)) 
        
    def is_valid_move(self, block, row, col, rotation):

        block_tryout = copy.deepcopy(block)
        block_tryout.row += row
        block_tryout.col += col
        if rotation:
            block_tryout.rotate_clockwise()
        
        for row_index, row in enumerate(block_tryout.pattern):
            grid_row_index = block_tryout.row + row_index
            for col_index, col_value in enumerate(row):
                grid_col_index = block_tryout.col + col_index

                if col_value == 'x':
                    # left-border: grid_indices not smaller than 0
                    if grid_row_index < 0 or grid_col_index < 0:
                        return False
                    try:
                        if self._grid[grid_row_index][grid_col_index] != self.empty:
                            return False
                    except IndexError:
                        return False
        # otherwise its ok!
        return True
    
    def set_block(self, block):
        score_row_index = None
        for row_index, row in enumerate(block.pattern):
            for col_index, col_value in enumerate(row):
                if col_value == 'x':
                    self._grid[block.row + row_index][block.col + col_index] = block.color
                    if not score_row_index:
                        score_row_index = block.row + row_index

        self.game_base.stats.add_set_block_score(score_row_index)
        self.game_base.stats.blocks += 1

    def check_completed_lines(self):
        completed_lines = []
        for row_index, row in enumerate(self._grid):
            if len([cell for cell in row if cell == self.empty]) == 0:
                completed_lines.append(row_index)

        self._grid = [row for row_index, row in enumerate(self._grid) if row_index not in completed_lines]

        for _ in completed_lines:
            self._grid.insert(0,[self.empty for _ in range(self.cols)])

        self.game_base.stats.add_completed_lines_score(len(completed_lines))

        self.game_base.stats.lines += len(completed_lines)
        if len(completed_lines) == 4:
            self.game_base.stats.tetris += 1
        
        if completed_lines:
            if len(completed_lines) == 4:
                self.game_base.soundfx.sound("applause")
            else:
                self.game_base.soundfx.sound("completed_line")




    