import pygame
from pygame.event import Event

from classes.game_loop_interface import GameLoopInterface

from .scoreboard import Scoreboard
from game_assets.tetris_grid import TetrisGrid
from game_assets.shape import Shape
from game_assets.block import Block

import random

class PlayGame(GameLoopInterface):

    ######################################
    # INIT
    ######################################

    def __init__(self, game_base) -> None:
        """ Init """
        super().__init__(game_base)

        # Init scoreboard
        self.sb = Scoreboard(game_base)
        
        # Init game assets
        self.grid = TetrisGrid(self.game_base.screen, self.game_base.settings.grid_width, self.game_base.settings.grid_height, 25, (0,0,0))

        self.shapes = []

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
        
        shape_bar = Shape(pattern_bar)
        self.shapes.append(shape_bar)
        shape_L = Shape(pattern_L)
        self.shapes.append(shape_L)
        self.block = Block(5, 5, shape_bar, (255, 0, 255))

        self.GRAVITY = pygame.USEREVENT + 1
    
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
        if event.type == self.GRAVITY:
            if self.grid.is_valid_move(self.block, 1, 0, 0):
                self.block.apply_gravity()
            else:
                self.grid.set_block(self.block)
                self.grid.check_completed_lines()
                self._new_block()

    def _new_block(self):
        shape = random.choice(self.shapes)
        self.block = Block(0, self.grid.cols//2, shape, (255, 30, 70))

    
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
    
    def _check_keyup_events(self, event):
        """ Respond to keydup events (keyboard)"""
        # RIGHT
        if event.key == pygame.K_RIGHT:
            # Stop moving to the right
            pass
        # LEFT
        if event.key == pygame.K_LEFT:
            # Stop moving to the left
            pass

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
        
        # Falling block
        pygame.time.set_timer(Event(self.GRAVITY), 500)