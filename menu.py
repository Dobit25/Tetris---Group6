import pygame
import os
import json
from gameact import Tetris, draw_pause_screen, draw_game_screen

def draw_start_screen(screen, high_score, background_image):
    screen.blit(background_image, (0, 0))
    font = pygame.font.SysFont('Calibri', 40, True, False)
    title_text = font.render("Tetris Game", True, (255, 255, 255))
    screen.blit(title_text, [100, 100])

    button_color = (0, 255, 0)
    button_rect = pygame.Rect(150, 250, 100, 50)
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = font.render("Start", True, (0, 0, 0))
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    pygame.display.flip()

    return button_rect

def draw_name_input_screen(screen, player_name):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Calibri', 40, True, False)
    prompt_text = font.render("Enter your name:", True, (255, 255, 255))
    screen.blit(prompt_text, [50, 100])

    input_box = pygame.Rect(50, 200, 300, 50)
    pygame.draw.rect(screen, (255, 255, 255), input_box, 2)

    name_text = font.render(player_name, True, (255, 255, 255))
    screen.blit(name_text, (input_box.x + 10, input_box.y + 10))

    pygame.display.flip()

    return input_box

def draw_pause_screen(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Calibri', 40, True, False)
    pause_text = font.render("Paused", True, (255, 255, 255))
    screen.blit(pause_text, [150, 100])

    # Draw Resume button
    resume_button_color = (0, 255, 0)
    resume_button_rect = pygame.Rect(100, 200, 200, 50)
    pygame.draw.rect(screen, resume_button_color, resume_button_rect)
    resume_button_text = font.render("Resume", True, (0, 0, 0))
    screen.blit(resume_button_text, (resume_button_rect.x + 10, resume_button_rect.y + 10))

    # Draw Restart button
    restart_button_color = (255, 0, 0)
    restart_button_rect = pygame.Rect(100, 300, 200, 50)
    pygame.draw.rect(screen, restart_button_color, restart_button_rect)
    restart_button_text = font.render("Restart", True, (0, 0, 0))
    screen.blit(restart_button_text, (restart_button_rect.x + 10, restart_button_rect.y + 10))

    # Draw Quit button
    quit_button_color = (255, 255, 0)
    quit_button_rect = pygame.Rect(100, 400, 200, 50)
    pygame.draw.