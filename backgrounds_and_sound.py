import pygame
import os

os.chdir(os.path.dirname(__file__))
menu_bg = pygame.image.load("menu_bg.png")
menu_bg = pygame.transform.scale(menu_bg, (400, 500))
gameplay_bg = pygame.image.load("gameplay_bg.png")
gameplay_bg = pygame.transform.scale(gameplay_bg, (400, 500))

is_muted = False  # Global variable to track mute state

def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("backgrounds_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)
    return pygame.mixer.music

def sound_effect():
    pygame.mixer.init()
    sound_effect_channel = pygame.mixer.Channel(1)
    sound_effect_channel.set_volume(0.7)
    sound_effect_channel.play(pygame.mixer.Sound("clear_line_sound.mp3"))

def toggle_mute():
    global is_muted
    if is_muted:
        pygame.mixer.music.set_volume(0.7)
        is_muted = False
    else:
        pygame.mixer.music.set_volume(0.0)
        is_muted = True
