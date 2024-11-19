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
    screen.fill((230, 247, 255))
    font_title = pygame.font.SysFont('Calibri', 60, True, False)
    font = pygame.font.SysFont('Calibri', 35, True, False)
    button_font = pygame.font.SysFont('Calibri', 35, True, False)
    button_color = (0, 38, 77)

    # Draw decorative elements
    pygame.draw.rect(screen, (255, 255, 255), (50, 50, 700, 600))  # White background panel
    pygame.draw.rect(screen, button_color, (50, 50, 700, 600), 3)  # Border

    # Title with underline
    title_text = font_title.render("Enter Your Name", True, button_color)
    title_x = screen.get_width() // 2 - title_text.get_width() // 2
    screen.blit(title_text, (title_x, 100))
    
    # Decorative line under title
    line_y = 170
    pygame.draw.line(screen, button_color, 
                    (title_x - 20, line_y), 
                    (title_x + title_text.get_width() + 20, line_y), 3)

    # Input box with better styling
    input_box = pygame.Rect(screen.get_width() // 2 - 200, 250, 400, 60)
    pygame.draw.rect(screen, (255, 255, 255), input_box)  # White background
    pygame.draw.rect(screen, button_color, input_box, 2)  # Blue border

    # Player name text
    name_text = font.render(player_name, True, button_color)
    # Add blinking cursor effect
    if pygame.time.get_ticks() % 1000 < 500:  # Blink every half second
        cursor = font.render("|", True, button_color)
        screen.blit(cursor, (input_box.x + 10 + name_text.get_width(), input_box.y + 10))

    screen.blit(name_text, (input_box.x + 10, input_box.y + 10))

    # Helper text
    helper_font = pygame.font.SysFont('Calibri', 20, True, False)
    helper_text = helper_font.render("Press ENTER or click Submit to continue", True, (100, 100, 100))
    screen.blit(helper_text, (screen.get_width() // 2 - helper_text.get_width() // 2, input_box.bottom + 20))

    # Draw "Submit" button with hover effect
    submit_button_rect = pygame.Rect(screen.get_width() // 2 - 150, 400, 300, 50)
    mouse_pos = pygame.mouse.get_pos()
    button_color_current = (0, 60, 120) if submit_button_rect.collidepoint(mouse_pos) else button_color
    
    # Button with slight gradient effect
    pygame.draw.rect(screen, button_color_current, submit_button_rect)
    pygame.draw.rect(screen, (0, 20, 40), submit_button_rect, 1)  # Darker border
    
    submit_text = button_font.render("Submit", True, (255, 255, 255))
    screen.blit(submit_text, (submit_button_rect.centerx - submit_text.get_width() // 2, 
                             submit_button_rect.centery - submit_text.get_height() // 2))

    pygame.display.flip()
    return input_box, submit_button_rect

def draw_sound_screen(screen):
    screen.fill((230, 247, 255))
    font_title = pygame.font.SysFont('Calibri', 50, True, False)
    font = pygame.font.SysFont('Calibri', 35, True, False)
    button_font = pygame.font.SysFont('Calibri', 28, True, False)
    button_color = (0, 38, 77)

    # Center everything horizontally
    center_x = screen.get_width() // 2

    # Draw decorative panel
    panel_rect = pygame.Rect(center_x - 300, 50, 600, 500)
    pygame.draw.rect(screen, (255, 255, 255), panel_rect)
    pygame.draw.rect(screen, button_color, panel_rect, 3)

    # Draw title with underline
    title_text = font_title.render("Sound Settings", True, button_color)
    title_x = center_x - title_text.get_width() // 2
    screen.blit(title_text, (title_x, 80))
    pygame.draw.line(screen, button_color, (title_x - 20, 140), (title_x + title_text.get_width() + 20, 140), 3)

    # Volume bar background
    volume_bar_rect = pygame.Rect(center_x - 150, 200, 300, 20)
    pygame.draw.rect(screen, (200, 200, 200), volume_bar_rect)

    # Get current volume and round it to nearest 5%
    current_volume = round(pygame.mixer.music.get_volume() * 20) / 20
    pygame.mixer.music.set_volume(current_volume)  # Apply rounded volume
    
    filled_width = int(volume_bar_rect.width * current_volume)
    volume_filled_rect = pygame.Rect(volume_bar_rect.x, volume_bar_rect.y, filled_width, volume_bar_rect.height)
    pygame.draw.rect(screen, button_color, volume_filled_rect)

    # Volume percentage text with rounded value
    volume_text = font.render(f"{int(current_volume * 100)}%", True, button_color)
    screen.blit(volume_text, (center_x + 170, 190))

    # Draw volume controls
    increase_button_rect = pygame.Rect(center_x - 125, 250, 50, 50)
    pygame.draw.rect(screen, button_color, increase_button_rect)
    increase_button_text = button_font.render("+", True, (255, 255, 255))
    screen.blit(increase_button_text, (increase_button_rect.centerx - 8, increase_button_rect.centery - 12))

    decrease_button_rect = pygame.Rect(center_x + 75, 250, 50, 50)
    pygame.draw.rect(screen, button_color, decrease_button_rect)
    decrease_button_text = button_font.render("-", True, (255, 255, 255))
    screen.blit(decrease_button_text, (decrease_button_rect.centerx - 6, decrease_button_rect.centery - 12))

    # Draw mute toggle button with indicator
    mute_button_rect = pygame.Rect(center_x - 75, 350, 150, 50)
    mute_color = (150, 0, 0) if pygame.mixer.music.get_volume() == 0 else button_color
    pygame.draw.rect(screen, mute_color, mute_button_rect)
    mute_text = "Unmute" if pygame.mixer.music.get_volume() == 0 else "Mute"
    mute_button_text = button_font.render(mute_text, True, (255, 255, 255))
    screen.blit(mute_button_text, (mute_button_rect.centerx - mute_button_text.get_width() // 2, mute_button_rect.centery - 12))

    # Draw back button with hover effect
    back_button_rect = pygame.Rect(center_x - 75, 450, 150, 50)
    mouse_pos = pygame.mouse.get_pos()
    back_color = (0, 60, 120) if back_button_rect.collidepoint(mouse_pos) else button_color
    pygame.draw.rect(screen, back_color, back_button_rect)
    back_button_text = button_font.render("Back", True, (255, 255, 255))
    screen.blit(back_button_text, (back_button_rect.centerx - back_button_text.get_width() // 2, back_button_rect.centery - 12))

    pygame.display.flip()
    return increase_button_rect, decrease_button_rect, mute_button_rect, back_button_rect, volume_bar_rect
