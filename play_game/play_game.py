import pygame
from pygame.event import Event

from classes.game_loop_interface import GameLoopInterface

from .scoreboard import Scoreboard
from game_assets.tetris_grid import TetrisGrid
from game_assets.block import Block

import random

class PlayGame(GameLoopInterface):

    ######################################
    # INIT
    ######################################

    def __init__(self, game_base) -> None:
        """ Init """
        super().__init__(game_base)

        # Create new EVENT to simulate gravity
        self.GRAVITY_PULL = pygame.USEREVENT + 1

        # Init scoreboard
        self.sb = Scoreboard(game_base)
        
        # Init game assets
        self.grid = TetrisGrid(self.game_base, self.game_base.settings.grid_width, self.game_base.settings.grid_height,
                                self.game_base.settings.cell_size, self.game_base.settings.color_empty_cells)

        # Create new block
        self._new_block()
    
    ######################################
    # CHECK EVENTS
    ######################################

    def check_events(self, event) -> None:

        if self.game_base.stats.game_over:
            self._game_over()

        """ Respond to keyboard events """
        if event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        # Key up events
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)
        # Event of Gravity Pull
        if event.type == self.GRAVITY_PULL:
            if self.grid.is_valid_move(self.block, 1, 0, 0):
                self.block.apply_gravity()
                #self.game_base.soundfx.sound("tick")
            else:
                self._finish_fall()

        if self.game_base.joystick:
            if event.type == pygame.JOYHATMOTION:
                self._check_joystick()
            if event.type == pygame.JOYBUTTONDOWN:
                self._check_joystick_button_down()

    def _finish_fall(self):
        self.grid.set_block(self.block)
        #self.game_base.soundfx.sound("set_block")
        self.grid.check_completed_lines()
        self._new_block()
        self._check_level_up()

    def _check_level_up(self):
        if self.game_base.stats.blocks % self.game_base.settings.level_up_treshold == 0:
            self.game_base.stats.level += 1
            self.game_base.settings.increase_speed()
            #self.game_base.soundfx.sound("level_up")

    def _new_block(self):
        random_shape = random.choice(self.game_base.settings.shapes)
        random_color = random.choice(self.game_base.settings.colors)
        self.block = Block(0, (self.grid.cols//2)-1, random_shape, random_color)
        if not self.grid.is_valid_move(self.block, 1, 0, 0):
            self.game_base.stats.game_over = True
            
    def _game_over(self):
        # If new highscore, switch to New Highscore loop
        #self.game_base.soundfx.sound('game_over', pausemusic=True, wait=True)
        if self.game_base.stats.is_highscore():
            self.game_base.switch_loop_to(self.game_base.new_highscore)
        # Else, switch Loop to Game Over loop
        else:
            self.game_base.switch_loop_to(self.game_base.game_over)

    def _check_keydown_events(self, event):
        """ Respond to keydown events (keyboard)"""
        # RIGHT
        if event.key == pygame.K_RIGHT:
            # Start moving to the right
            if self.grid.is_valid_move(self.block, 0, 1, 0):
                self.block.col += 1
        # LEFT (no elif to hold still when right key and left key are both down)
        if event.key == pygame.K_LEFT:
            # Start moving to the left
            if self.grid.is_valid_move(self.block, 0, -1, 0):
                self.block.col -= 1
        # UP
        elif event.key == pygame.K_UP:
            if self.grid.is_valid_move(self.block, 0, 0, 1):
                self.block.rotate_clockwise()
        # DOWN
        elif event.key == pygame.K_DOWN:
            pygame.time.set_timer(Event(self.GRAVITY_PULL), self.game_base.settings.down_speed)
    
    def _check_keyup_events(self, event):
        """ Respond to keydup events (keyboard)"""
        # DOWN
        if event.key == pygame.K_DOWN:
            pygame.time.set_timer(Event(self.GRAVITY_PULL), self.game_base.settings.game_speed)

    def _check_joystick(self):
        (hat_x, hat_y) = self.game_base.joystick.get_hat(0)
        if hat_x == -1 and self.grid.is_valid_move(self.block, 0, -1, 0):
            self.block.col -= 1
        elif hat_x == 1 and self.grid.is_valid_move(self.block, 0, 1, 0):
            self.block.col += 1
        elif hat_y == -1 and self.grid.is_valid_move(self.block, 1, 0, 0):
            pygame.time.set_timer(Event(self.GRAVITY_PULL), 30)
        elif hat_y != -1 and self.grid.is_valid_move(self.block, 1, 0, 0):
            pygame.time.set_timer(Event(self.GRAVITY_PULL), self.game_base.settings.game_speed)

    def _check_joystick_button_down(self):
        # JOYSTICK Button A: Rotate
        if self.game_base.joystick.get_button(1):
            if self.grid.is_valid_move(self.block, 0, 0, 1):
                self.block.rotate_clockwise()


    ######################################
    # UPDATE ASSETS
    ######################################

    def update_assets(self) -> None:
        """ Update assets """

        # Update scoreboard
        self.sb.update()
            

    ######################################
    # UPDATE SCREEN
    ######################################

    def update_screen(self) -> None:
        """ Redraw assets and flip the screen"""
        # Background
        self.game_base.screen.fill(self.game_base.settings.bg_color)

        self._draw_text_centered("Tetris", 60, 100)
        
        # Draw scoreboard
        self.sb.draw()

        # Draw Tetris Grid
        self.grid.draw(self.block)

    def _draw_text_centered(self, text, size, pos_y):
        text_bitmap = pygame.font.Font(self.game_base.settings.font, size).render(text, True, self.game_base.settings.font_color)
        # Figure out rectangle
        rect = text_bitmap.get_rect()
        # Center in screen
        rect.center = self.game_base.screen_rect.center
        # Set position on y-axis of screen
        rect.top = pos_y
        self.game_base.screen.blit(text_bitmap, rect)

    ######################################
    # HOOKS
    ######################################

    def start(self) -> None:
        self.game_base.settings.init_dynamic_settings()
        self.game_base.stats.reset_stats()
        self.grid.reset_grid()
        # Start simulation gravity by start posting GRAVITY_PULL Events every ... milliseconds
        pygame.time.set_timer(Event(self.GRAVITY_PULL), self.game_base.settings.game_speed)
        #self.game_base.soundfx.music("play_music")

    def stop(self) -> None:
        #self.game_base.soundfx.stop_music()
        pass