class Block:
    def __init__(self, row, col, shape, color) -> None:
        
        self.row = row
        self.col = col
        self.shape = shape
        self.color = color

        # get pattern with 0 rotations
        self.rotations = 0
        self.pattern = self.shape.get_pattern_rotation(0)

    def rotate_clockwise(self):
        self.rotations += 1
        self.pattern = self.shape.get_pattern_rotation(self.rotations)

    def rotate_anti_clockwise(self):
        self.rotations -= 1
        self.pattern = self.shape.get_pattern_rotation(self.rotations)

    def apply_gravity(self):
        self.row += 1