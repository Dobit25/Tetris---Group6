import pygame
def draw_start_screen(screen, background_image):
    screen.blit(background_image, (0, 0))  # Draw the background image
    font = pygame.font.SysFont('Calibri', 40, True, False)
    title_text = font.render("Tetris Game", True, (255, 255, 255))  # Tiêu đề
    screen.blit(title_text, [100, 100])

    # Draw start button in the middle
    button_color = (0, 255, 0)
    button_rect = pygame.Rect(150, 250, 100, 50)
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = font.render("Start", True, (0, 0, 0))
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    pygame.display.flip()  # Cập nhật màn hình

    return button_rect

def draw_name_input_screen(screen, player_name):
    screen.fill((0, 0, 0))  # Màu nền đen
    font = pygame.font.SysFont('Calibri', 40, True, False)
    prompt_text = font.render("Enter your name:", True, (255, 255, 255))
    screen.blit(prompt_text, [50, 100])

    input_box = pygame.Rect(50, 200, 300, 50)
    pygame.draw.rect(screen, (255, 255, 255), input_box, 2)

    name_text = font.render(player_name, True, (255, 255, 255))
    screen.blit(name_text, (input_box.x + 10, input_box.y + 10))

    pygame.display.flip()  # Cập nhật màn hình

    return input_box