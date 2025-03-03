import pygame
import sys
from new_highscore.input_line import InputLine
from classes.game_loop_interface import GameLoopInterface
from new_highscore.new_highscore_text import NewHighscoreText

class NewHighscore(GameLoopInterface):
    """ Class to implement text input """

    ######################################
    # INIT
    ######################################

    def __init__(self, game_base) -> None:
        super().__init__(game_base)
        self.line = InputLine(game_base, 8)
        self.screen_text = NewHighscoreText(game_base, self.game_base.settings.bg_color, self.game_base.settings.init_pos_y)

    ######################################
    # CHECK EVENTS
    ######################################

    def check_events(self, event):
        """ Respond to keyboard events """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.line.handle_input('UP')
            elif event.key == pygame.K_DOWN:
                self.line.handle_input('DOWN')
            elif event.key == pygame.K_RIGHT:
                self.line.handle_input('RIGHT')
            elif event.key == pygame.K_LEFT:
                self.line.handle_input('LEFT')
            elif event.key == pygame.K_RETURN:
                self._save_highscore()

        if self.game_base.joystick:
            if event.type == pygame.JOYBUTTONDOWN:
                self._check_joystick_button_down()

    def _check_joystick_button_down(self):
        # JOYSTICK Button A: RIGHT
        if self.game_base.joystick.get_button(1):
            self.line.handle_input('RIGHT')
        # JOYSTICK Button Y: LEFT
        elif self.game_base.joystick.get_button(3):
            self.line.handle_input('LEFT')
        # JOYSTICK Button X: UP
        elif self.game_base.joystick.get_button(2):
            self.line.handle_input('UP')
        # JOYSTICK Button B: DOWN
        elif self.game_base.joystick.get_button(0):
            self.line.handle_input('DOWN')
        # JOYSTICK Button ZR: SAVE
        elif self.game_base.joystick.get_button(8):
            self._save_highscore()


    def _save_highscore(self):
        self.game_base.stats.insert_and_save_highscore(self.line.get_input())
        self.game_base.switch_loop_to(self.game_base.game_over)

    ######################################
    # UPDATE ASSETS
    ######################################

    def update_assets(self) -> None:
        self.screen_text.update()

    ######################################
    # UPDATE SCREEN
    ######################################

    def update_screen(self):
        self.game_base.screen.fill(self.game_base.settings.bg_color)
        self.screen_text.draw()
        self.line.draw(self.game_base.settings.init_pos_y + 330)

    ######################################
    # HOOKS
    ######################################

    def start(self) -> None:
        #self.game_base.soundfx.sound('new_highscore', pausemusic=True, wait=False)
        pass