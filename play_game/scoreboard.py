import pygame.font

class Scoreboard:
    """ Class representing scoreboard """

    def __init__(self, game_base) -> None:
        """ Init """
        self.game_base = game_base

        # Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(self.game_base.settings.font, 32)
        self.topmargin = (self.game_base.settings.screen_height - self.game_base.settings.grid_height)/2 + 20

        self.update()

    def update(self):
        """ Update scoreboard """
        self._prep_score()
        self._prep_level()

    def _prep_score(self):
        """ Turn score in rendered image """
        score_color = self.text_color
        if self.game_base.stats.is_highscore():
            score_color = self.game_base.settings.green
        rounded_score = round(self.game_base.stats.score)
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(f"Score: {score_str}", True, score_color, self.game_base.settings.bg_color)

        # Display score at top right
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = (self.game_base.settings.screen_width - self.game_base.settings.grid_width)/2
        self.score_rect.top = self.topmargin

    def _prep_level(self):
        """ Turn level in rendered image """
        level_str = f"Level: {self.game_base.stats.level}"
        self.level_img = self.font.render(level_str, True, self.text_color, self.game_base.settings.bg_color)

        # Display level 
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = (self.game_base.settings.screen_width - self.game_base.settings.grid_width)/2 + self.game_base.settings.grid_width
        self.level_rect.top = self.topmargin

    def draw(self):
        """ Draw scoreboard to screen """
        self.game_base.screen.blit(self.score_img, self.score_rect)
        self.game_base.screen.blit(self.level_img, self.level_rect)
