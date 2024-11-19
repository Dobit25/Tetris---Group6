import json
import pygame
import os
def load_scores():
    # if os.path.exists("player_scores.json"):
    os.chdir(os.path.dirname(__file__))
    with open("player_data.json", "r") as file:
        scores = json.load(file)
        # Create a dictionary to keep track of the scores
        score_dict = {}
        for score in scores:
            player_name = score["Player_name"]
            player_score = score["Score"]
            if player_name in score_dict:
                # If the player already has a score, update it if the new score is higher
                score_dict[player_name] = max(score_dict[player_name], player_score)
            else:
                score_dict[player_name] = player_score
        # Sort the scores and take the top 10
        sorted_scores = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:10]
        return [{"Player_name": player_name, "Score": player_score} for player_name, player_score in sorted_scores]
    return []

def save_score(player_name, score):
    scores = load_scores()
    scores.append({"Player_name": player_name, "Score": score})
    with open("player_data.json", "w") as file:
        json.dump(scores, file, indent=4)

def draw_ranking_screen(screen):
    scores = load_scores()
    scores = scores[:10]  # Display top 10 scores

    screen.fill((230, 247, 255))  # Light background color
    font_title = pygame.font.SysFont('Calibri', 60, True, False)
    font_rank = pygame.font.SysFont('Calibri', 35, True, False)
    font_score = pygame.font.SysFont('Calibri', 30, True, False)
    button_font = pygame.font.SysFont('Calibri', 28, True, False)

    # Draw title with decorative lines
    title_text = font_title.render("RANKING", True, (0, 38, 77))
    title_x = screen.get_width() // 2 - title_text.get_width() // 2
    screen.blit(title_text, (title_x, 50))
    
    # Draw decorative lines
    line_color = (0, 38, 77)
    line_length = 300
    pygame.draw.line(screen, line_color, (title_x - 20, 120), (title_x + title_text.get_width() + 20, 120), 3)
    
    # Create a background rectangle for scores
    scores_rect = pygame.Rect(screen.get_width() // 2 - 250, 150, 500, 400)
    pygame.draw.rect(screen, (255, 255, 255), scores_rect)
    pygame.draw.rect(screen, (0, 38, 77), scores_rect, 2)  # Border

    # Draw scores with alternating background colors
    for index, score in enumerate(scores):
        y_pos = 160 + index * 35

        # Chỉ hiển thị số thay vì emoji
        rank_text = font_rank.render(f"{index + 1}.", True, (0, 38, 77))
            
        # Draw alternating background for better readability
        if index % 2 == 0:
            pygame.draw.rect(screen, (240, 248, 255), (scores_rect.left + 5, y_pos - 5, scores_rect.width - 10, 30))

        # Draw player name and score
        screen.blit(rank_text, (scores_rect.left + 30, y_pos))
        name_text = font_score.render(f"{score['Player_name']}", True, (0, 38, 77))
        screen.blit(name_text, (scores_rect.left + 120, y_pos))
        score_text = font_score.render(f"{score['Score']}", True, (0, 38, 77))
        screen.blit(score_text, (scores_rect.right - 120, y_pos))

    # Draw "Back to Menu" button
    button_color = (0, 38, 77)
    menu_button_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() - 80, 200, 50)
    pygame.draw.rect(screen, button_color, menu_button_rect)
    menu_button_text = button_font.render("Back to Menu", True, (255, 255, 255))
    screen.blit(menu_button_text, (menu_button_rect.centerx - menu_button_text.get_width() // 2, 
                                  menu_button_rect.centery - menu_button_text.get_height() // 2))

    pygame.display.flip()
    return menu_button_rect
