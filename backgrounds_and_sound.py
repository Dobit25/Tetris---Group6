import pygame
import random, time
menu_bg = pygame.image.load("menu_bg.png")
menu_bg = pygame.transform.scale(menu_bg, (800, 700)) 
gameplay_bg = pygame.image.load("gameplay_bg.png")
gameplay_bg = pygame.transform.scale(gameplay_bg, (800, 700)) 

is_muted = False  

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

def show_bubbles(screen):
    start_time = time.time()
    screen_rect = screen.get_rect()
    bubbles = pygame.image.load('bubbles.png')  # Load your bubbles image
    bubbles = pygame.transform.scale(bubbles, (40, 40))  # Resize bubbles to be larger

    while time.time() - start_time < 2:
        for _ in range(5):  # Show 5 bubbles at random positions
            x = random.randint(0, screen_rect.width - bubbles.get_width())
            y = random.randint(0, screen_rect.height - bubbles.get_height())
            screen.blit(bubbles, (x, y))
        pygame.display.flip()  # Update the full display Surface to the screen
        pygame.time.delay(100)  # Delay to control the update speed
