import pygame.font
from classes.textscreen_center import TextScreenCenter

class NewHighscoreText(TextScreenCenter):
    """ Class representing text for New Highscore loop """

    def __init__(self, game_base, bg_color, start_pos_y) -> None: 
        """ Init """
        super().__init__(game_base, bg_color, start_pos_y)
        self.game_base = game_base
        self.settings = game_base.settings
        self.stats = game_base.stats

        self.update()

    def update(self):
        self.images.clear()

        # NEW HIGHSCORE!
        super().render_text("NEW HIGHSCORE!", self.settings.font, 80, self.settings.purple)
        super().add_whitespace(20)

        # Score
        rounded_score = round(self.game_base.stats.score)
        score_str = "{:,}".format(rounded_score)
        super().render_text(score_str, self.settings.font, 80, self.settings.font_color)
        super().add_whitespace(40)

        super().render_text("Enter your name:", self.settings.font, 28, self.game_base.settings.font_color)
        super().add_whitespace(250)

        # Message to start 
        super().render_text("Use buttons and ZR to complete", self.settings.font, 28, self.game_base.settings.yellow)
        

