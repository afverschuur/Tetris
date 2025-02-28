from game_assets.block_shapes import BlockShapes

class Settings:
    """ Class with all settings """

    def __init__(self):

        # Game
        self.title = "Tetris"
        self.max_framerate = 60
        self.level_up_treshold = 30

        # Screen settings
        self.bg_color = (100, 100, 100)
        self.screen_height = 1100   # overwritten in case of fullscreen
        self.screen_width = 800     # overwritten in case of fullscreen
        self.init_pos_y = self.screen_height / 6

        # Set fonts
        self.font_color = (255, 255, 255)
        self.font = "assets/fonts/JockeyOne-Regular.ttf"

        # Grid 
        self.cell_size = 30
        self.grid_width = 14 * self.cell_size
        self.grid_height = 24 * self.cell_size
        self.color_empty_cells = (0, 0, 0)

        # Shapes
        self.shapes = BlockShapes().shapes

        # Colors
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        yellow = (255, 255, 0)
        orange = (255, 127, 0)

        self.colors = [red, green, blue, yellow, orange]

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.game_speed = 700

    def increase_speed(self):
        """ Increase speed settings """
        self.game_speed -= 50


        

    