import pygame
def draw_game_over_popup(screen, score, high_score):
    screen.fill((230, 247, 255))  # Background color
    font_title = pygame.font.SysFont('Calibri', 50, True, False)
    font = pygame.font.SysFont('Calibri', 28, True, False)

    # Game Over title
    game_over_text = font_title.render("GAME OVER", True, (0, 38, 77))
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, 100))

    # Display score and high score
    score_text = font.render(f"CURRENT SCORE: {score}", True, (0, 38, 77))
    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 200))

    high_score_text = font.render(f"HIGHEST SCORE: {high_score}", True, (0, 38, 77))
    screen.blit(high_score_text, (screen.get_width() // 2 - high_score_text.get_width() // 2, 250))

    # Button dimensions and positions
    button_width = 300
    button_height = 50
    base_x = screen.get_width() // 2 - button_width // 2

    ranking_button = pygame.Rect(base_x, 350, button_width, button_height)
    restart_button = pygame.Rect(base_x, 420, button_width, button_height)
    menu_button = pygame.Rect(base_x, 490, button_width, button_height)

    # Calculate the vertical center offset for the text
    text_y_offset = (button_height - font.get_height()) // 2

    # Draw "Ranking" button
    pygame.draw.rect(screen, (0, 38, 77), ranking_button)
    ranking_text = font.render("RANKING", True, (255, 255, 255))
    screen.blit(ranking_text, (
        ranking_button.x + ranking_button.width // 2 - ranking_text.get_width() // 2,
        ranking_button.y + text_y_offset
    ))

    # Draw "Restart" button
    pygame.draw.rect(screen, (0, 38, 77), restart_button)
    restart_text = font.render("RESTART", True, (255, 255, 255))
    screen.blit(restart_text, (
        restart_button.x + restart_button.width // 2 - restart_text.get_width() // 2,
        restart_button.y + text_y_offset
    ))

    # Draw "Main Menu" button
    pygame.draw.rect(screen, (0, 38, 77), menu_button)
    menu_text = font.render("MAIN MENU", True, (255, 255, 255))
    screen.blit(menu_text, (
        menu_button.x + menu_button.width // 2 - menu_text.get_width() // 2,
        menu_button.y + text_y_offset
    ))

    pygame.display.flip()  # Update the display
    return restart_button, menu_button, ranking_button
