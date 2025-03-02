import pygame
from time import sleep

class SoundFX:
    """ Class to implement soundeffects """
    def __init__(self) -> None:
        # Init pygame mixer
        pygame.mixer.init()

        # Load sounds
        self.sounds = dict()
        # self.sounds['game_over'] = pygame.mixer.Sound("assets/sounds/game_over.mp3")
        # self.sounds['set_block'] = pygame.mixer.Sound("assets/sounds/set_block.mp3")
        # self.sounds['completed_line'] = pygame.mixer.Sound("assets/sounds/completed_line.mp3")
        # self.sounds['level_up'] = pygame.mixer.Sound("assets/sounds/level_up.mp3")
        # self.sounds['new_highscore'] = pygame.mixer.Sound("assets/sounds/new_highscore.mp3")
        # self.sounds['applause'] = pygame.mixer.Sound("assets/sounds/applause.mp3")
        
        # Load music
        self.musics = dict()
        # self.musics['play_music'] = pygame.mixer.Sound("assets/sounds/play_music.mp3")

        # Open dedicated channel for music
        self.music_channel = pygame.mixer.Channel(1)
    
    def sound(self, sound, pausemusic=False, wait=False):
        """ Play sound """
        # Pause music before playing sound if True
        if pausemusic:
            self.music_channel.pause()
        pygame.mixer.Sound.play(self.sounds[sound])
        # Wait for sound to end before continuing game
        if wait:
            sleep(self.sounds[sound].get_length())
        # Unpause music before playing sound if True
        if pausemusic:
            self.music_channel.unpause()

    def music(self, music):
        """ Play music (infinite) """
        self.music_channel.play(self.musics[music], -1)

    def stop_music(self):
        self.music_channel.stop()





