class Shape:
    def __init__(self, patterns) -> None:
        self._patterns = patterns
    
    def get_pattern_rotation(self, number_of_90_degree_rotations):
        index = number_of_90_degree_rotations % len(self._patterns)
        return self._patterns[index]

                        