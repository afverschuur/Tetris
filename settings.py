from game_assets.block_shapes import BlockShapes

class Settings:
    """ Class with all settings """

    def __init__(self):

        # Game
        self.title = "Tetris"
        self.max_framerate = 60
        self.level_up_treshold = 30
        self.down_speed = 30

        # Screen settings
        self.bg_color = (100, 100, 100)
        self.screen_height = 1100   # overwritten in case of fullscreen
        self.screen_width = 800     # overwritten in case of fullscreen
        self.init_pos_y = self.screen_height / 6

        # Grid 
        self.cell_size = 35
        self.grid_width = 14 * self.cell_size
        self.grid_height = 21 * self.cell_size
        self.color_empty_cells = (0, 0, 0)

        # Shapes
        self.shapes = BlockShapes().shapes

        # Colors
        self.red = (241, 9, 49)
        self.green = (70, 189, 48)
        self.blue = (0, 216, 242)
        self.yellow = (255, 217, 36)
        self.orange = (254, 137, 15)
        self.purple = (255, 47, 255)

        self.colors = [self.red, self.green, self.blue, self.yellow, self.orange, self.purple]

        # Set fonts
        self.font_color = (255, 255, 255)
        self.font = "assets/fonts/JockeyOne-Regular.ttf"
        self.font_color_title = self.purple
        self.font_title = "assets/fonts/JockeyOne-Regular.ttf"
        self.font_monospace = "assets/fonts/SpaceMono-Regular.ttf"

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.game_speed = 600

    def increase_speed(self):
        """ Increase speed settings """
        self.game_speed -= 50


        

    