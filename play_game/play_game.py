import pygame
from pygame.event import Event

from classes.game_loop_interface import GameLoopInterface

from .scoreboard import Scoreboard
from game_assets.tetris_grid import TetrisGrid
from game_assets.block import Block

import random
import sys

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
            else:
                self._finish_fall()

    def _finish_fall(self):
        self.grid.set_block(self.block)
        self.grid.check_completed_lines()
        self._new_block()

    def _new_block(self):
        random_shape = random.choice(self.game_base.settings.shapes)
        random_color = random.choice(self.game_base.settings.colors)
        self.block = Block(0, self.grid.cols//2, random_shape, random_color)
        if not self.grid.is_valid_move(self.block, 1, 0, 0):
            print("GAME OVER")
            sys.exit()

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
            pygame.time.set_timer(Event(self.GRAVITY_PULL), 30)
    
    def _check_keyup_events(self, event):
        """ Respond to keydup events (keyboard)"""
        # DOWN
        if event.key == pygame.K_DOWN:
            pygame.time.set_timer(Event(self.GRAVITY_PULL), 500)


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
        
        # Draw scoreboard
        self.sb.draw()

        # Draw Tetris Grid
        self.grid.draw(self.block)

    ######################################
    # HOOKS
    ######################################

    def start(self) -> None:
        
        # Start simulation gravity by start posting GRAVITY_PULL Events every ... milliseconds
        pygame.time.set_timer(Event(self.GRAVITY_PULL), 500)