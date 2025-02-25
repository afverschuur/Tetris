import pygame

class Settings:
    """ Class with all settings """

    def __init__(self):

        # Game
        self.title = "Tetris"

        # Screen settings
        self.bg_color = (0,0,0)
        self.screen_height = 1100   # overwritten in case of fullscreen
        self.screen_width = 800     # overwritten in case of fullscreen
        self.init_pos_y = self.screen_height / 6

        # Set fonts
        self.font_color = (255, 255, 255)
        self.font = "assets/fonts/JockeyOne-Regular.ttf"

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        pass

    def increase_speed(self):
        """ Increase speed settings """
        pass


        

    