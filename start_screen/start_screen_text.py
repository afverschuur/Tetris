import pygame.font
from classes.textscreen_center import TextScreenCenter

class StartScreenText(TextScreenCenter):
    """ Class representing welcome text on startscreen """

    def __init__(self, game_base, bg_color, start_pos_y) -> None: 
        """ Init """
        super().__init__(game_base, bg_color, start_pos_y)
        self.settings = game_base.settings
        self.stats = game_base.stats

        self.update()

    def update(self):
        self.images.clear()

        # Title of game
        super().render_text(self.settings.title, self.settings.font_title, 140, self.settings.font_color_title)
        self.add_whitespace(20)
        # Highscore
        super().render_text("HALL OF FAME", self.settings.font, 28, self.game_base.settings.font_color)
        super().add_whitespace(20)
        # Top3 of highscores
        for place, (name, highscore) in enumerate(self.stats.highscores):
            self._render_highscore(place+1, name, highscore)
            super().add_whitespace(10)
        super().add_whitespace(40)
        # Message to start 
        super().render_text("Press A button to start game", self.settings.font, 28, self.game_base.settings.yellow)
        
    def _render_highscore(self, place, name, score):
        """ Turn topscore in rendered image """
        name_str = str(name).ljust(8)
        score_str = "{:,}".format(score).rjust(10, " ")
        score_str = f"{place}. {name_str} {score_str}"
        super().render_text(score_str, self.settings.font_monospace, 28, self.game_base.settings.font_color)
