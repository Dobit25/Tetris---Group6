import pygame

def draw_start_screen(screen, background_image):
    screen.blit(background_image, (0, 0))  # Draw the background image
    font = pygame.font.SysFont('Calibri', 40, True, False)
    button_font = pygame.font.SysFont('Calibri', 30, True, False)
    
    # Removed title text lines
    
    # Button properties
    button_color = (0, 38, 77)  # Blue color
    button_width = 300  # Wider buttons
    button_height = 50  # Taller buttons
    button_margin = 30

    # Adjusted vertical positions
    base_y = 250

    # Draw start button
    start_button_rect = pygame.Rect(250, base_y, button_width, button_height)
    pygame.draw.rect(screen, button_color, start_button_rect)
    start_button_text = button_font.render("Start", True, (255, 255, 255))
    screen.blit(start_button_text, (start_button_rect.x + start_button_rect.width // 2 - start_button_text.get_width() // 2, start_button_rect.y + 5))

    # Draw ranking button
    ranking_button_rect = pygame.Rect(250, base_y + button_height + button_margin, button_width, button_height)
    pygame.draw.rect(screen, button_color, ranking_button_rect)
    ranking_button_text = button_font.render("Ranking", True, (255, 255, 255))
    screen.blit(ranking_button_text, (ranking_button_rect.x + ranking_button_rect.width // 2 - ranking_button_text.get_width() // 2, ranking_button_rect.y + 5))

    # Draw sound button
    sound_button_rect = pygame.Rect(250, base_y + 2 * (button_height + button_margin), button_width, button_height)
    pygame.draw.rect(screen, button_color, sound_button_rect)
    sound_button_text = button_font.render("Sound", True, (255, 255, 255))
    screen.blit(sound_button_text, (sound_button_rect.x + sound_button_rect.width // 2 - sound_button_text.get_width() // 2, sound_button_rect.y + 5))

    # Draw exit button
    exit_button_rect = pygame.Rect(250, base_y + 3 * (button_height + button_margin), button_width, button_height)
    pygame.draw.rect(screen, button_color, exit_button_rect)
    exit_button_text = button_font.render("Exit", True, (255, 255, 255))
    screen.blit(exit_button_text, (exit_button_rect.x + exit_button_rect.width // 2 - exit_button_text.get_width() // 2, exit_button_rect.y + 5))

    pygame.display.flip()  # Update the screen

    return start_button_rect, ranking_button_rect, sound_button_rect, exit_button_rect


def draw_name_input_screen(screen, player_name):
    screen.fill((230, 247, 255))  # Light background color
    font_title = pygame.font.SysFont('Calibri', 50, True, False)
    font = pygame.font.SysFont('Calibri', 28, True, False)
    button_font = pygame.font.SysFont('Calibri', 28, True, False)
    button_color = (0, 38, 77)  # Blue color

    # Title
    title_text = font_title.render("Enter your name:", True, (0, 38, 77))
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 50))

    # Input box
    input_box = pygame.Rect(screen.get_width() // 2 - 150, 200, 300, 50)
    pygame.draw.rect(screen, (255, 255, 255), input_box, 2)

    name_text = font.render(player_name, True, (0, 38, 77))
    screen.blit(name_text, (input_box.x + 10, input_box.y + 10))

    # Draw "Submit" button
    submit_button_rect = pygame.Rect(screen.get_width() // 2 - 100, 300, 200, 40)
    pygame.draw.rect(screen, button_color, submit_button_rect)
    submit_button_text = button_font.render("Submit", True, (255, 255, 255))
    screen.blit(submit_button_text, (submit_button_rect.x + submit_button_rect.width // 2 - submit_button_text.get_width() // 2, submit_button_rect.y + 5))

    pygame.display.flip()  # Update the screen

    return input_box, submit_button_rect

def draw_sound_screen(screen):
    screen.fill((230, 247, 255))
    font = pygame.font.SysFont('Calibri', 40, True, False)
    button_font = pygame.font.SysFont('Calibri', 28, True, False)
    button_color = (0, 38, 77)

    # Center everything horizontally
    center_x = screen.get_width() // 2

    # Draw volume text
    volume_text = font.render("Volume Control", True, button_color)
    screen.blit(volume_text, (center_x - volume_text.get_width() // 2, 100))

    # Draw increase volume button
    increase_button_rect = pygame.Rect(center_x - 125, 200, 50, 50)
    pygame.draw.rect(screen, button_color, increase_button_rect)
    increase_button_text = button_font.render("+", True, (255, 255, 255))
    screen.blit(increase_button_text, (increase_button_rect.centerx - 8, increase_button_rect.centery - 12))

    # Draw decrease volume button
    decrease_button_rect = pygame.Rect(center_x + 75, 200, 50, 50)
    pygame.draw.rect(screen, button_color, decrease_button_rect)
    decrease_button_text = button_font.render("-", True, (255, 255, 255))
    screen.blit(decrease_button_text, (decrease_button_rect.centerx - 6, decrease_button_rect.centery - 12))

    # Draw mute toggle button
    mute_button_rect = pygame.Rect(center_x - 75, 300, 150, 50)
    pygame.draw.rect(screen, button_color, mute_button_rect)
    mute_button_text = button_font.render("Mute", True, (255, 255, 255))
    screen.blit(mute_button_text, (mute_button_rect.centerx - mute_button_text.get_width() // 2, mute_button_rect.centery - 12))

    # Draw back button
    back_button_rect = pygame.Rect(center_x - 75, 400, 150, 50)
    pygame.draw.rect(screen, button_color, back_button_rect)
    back_button_text = button_font.render("Back", True, (255, 255, 255))
    screen.blit(back_button_text, (back_button_rect.centerx - back_button_text.get_width() // 2, back_button_rect.centery - 12))

    pygame.display.flip()
    return increase_button_rect, decrease_button_rect, mute_button_rect, back_button_rect
