import pygame
import os
os.chdir(os.path.dirname(__file__))
menu_bg = pygame.image.load("menu_bg.jpg")
menu_bg = pygame.transform.scale(menu_bg, (400,500))
gameplay_bg = pygame.image.load("gameplay_bg.png")
gameplay_bg = pygame.transform.scale(gameplay_bg, (400,500))

def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("backgrounds_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)
    return pygame.mixer.music