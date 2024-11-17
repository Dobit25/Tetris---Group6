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
    font_title = pygame.font.SysFont('Calibri', 50, True, False)
    font = pygame.font.SysFont('Calibri', 28, True, False)
    button_font = pygame.font.SysFont('Calibri', 28, True, False)
    title_text = font_title.render("Ranking", True, (0, 38, 77))
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 50))

    for index, score in enumerate(scores):
        rank_text = font.render(f"{index + 1}. {score['Player_name']}: {score['Score']}", True, (0, 38, 77))
        screen.blit(rank_text, (50, 120 + index * 40))

    button_color = (0, 38, 77)  # Blue color
    menu_button_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() - 60, 200, 40)
    pygame.draw.rect(screen, button_color, menu_button_rect)
    menu_button_text = button_font.render("Menu", True, (255, 255, 255))
    screen.blit(menu_button_text, (menu_button_rect.x + menu_button_rect.width // 2 - menu_button_text.get_width() // 2, menu_button_rect.y + 5))

    pygame.display.flip()
    return menu_button_rect
