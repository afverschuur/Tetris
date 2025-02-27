
from game_assets.shape import Shape

class BlockShapes:
    def __init__(self) -> None:
        """ Construct the collection of block shapes """
        pattern_bar = [["....",
                        "....",
                        "xxxx",
                        "...."],

                       ["..x.",
                        "..x.",
                        "..x.",
                        "..x."]]
        
        pattern_L = [[".x.",
                      ".x.",
                      ".xx"],

                     ["...",
                      "xxx",
                      "x.."],

                     ["xx.",
                      ".x.",
                      ".x."],

                     ["..xs",
                      "xxx",
                      "..."]]
        
        pattern_L_reversed =  [[".x.",
                                ".x.",
                                "xx."],

                               ["x..",
                                "xxx",
                                "..."],

                               [".xx",
                                ".x.",
                                ".x."],

                               ["...",
                                "xxx",
                                "..x"]]
        
        pattern_Z = [["...",
                      "xx.",
                      ".xx"],

                     ["..x",
                      ".xx",
                      ".x."]]
        
        pattern_Z_reversed = [["...",
                               ".xx",
                               "xx."],

                              ["x..",
                               "xx.",
                               ".x."]]
                
        pattern_block = [["xx",
                          "xx"]]
        
        pattern_T = [["...",
                      "xxx",
                      ".x."],

                     [".x.",
                      "xx.",
                      ".x."],

                     [".x.",
                      "xxx",
                      "..."],

                     [".x.",
                      ".xx",
                      ".x."]]
        
        self.shapes = [Shape(pattern_bar), Shape(pattern_L), Shape(pattern_L_reversed),
                        Shape(pattern_Z), Shape(pattern_Z_reversed), Shape(pattern_block)]