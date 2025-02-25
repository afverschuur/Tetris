import pygame

from classes.game_loop_interface import GameLoopInterface

from .scoreboard import Scoreboard
from game_assets.tetris_grid import TetrisGrid
from game_assets.shape import Shape
from game_assets.block import Block

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

        pattern_bar = [[".....",
                        ".....",
                        "xxxxx",
                        ".....",
                        "....."],

                       ["..x..",
                        "..x..",
                        "..x..",
                        "..x..",
                        "..x.."]]
        
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
        
        shape_bar = Shape(pattern_L)
        self.block = Block(5, 5, shape_bar, (255, 0, 255))
    
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
    
    def _check_keydown_events(self, event):
        """ Respond to keydown events (keyboard)"""
        # RIGHT
        if event.key == pygame.K_RIGHT:
            # Start moving to the right
            self.block.col += 1
        # LEFT (no elif to hold still when right key and left key are both down)
        if event.key == pygame.K_LEFT:
            # Start moving to the left
            self.block.col -= 1
        # UP
        elif event.key == pygame.K_UP:
            self.block.rotate()
    
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
        pass