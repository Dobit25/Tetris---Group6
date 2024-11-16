import pygame
def draw_pause_screen(screen):
    screen.fill((0, 0, 0))  # Màu nền đen
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
    pygame.draw.rect(screen, quit_button_color, quit_button_rect)
    quit_button_text = font.render("Quit", True, (0, 0, 0))
    screen.blit(quit_button_text, (quit_button_rect.x + 10, quit_button_rect.y + 10))

    pygame.display.flip()  # Cập nhật màn hình

    return resume_button_rect, restart_button_rect, quit_button_rect