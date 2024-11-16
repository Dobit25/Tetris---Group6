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

    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Calibri', 40, True, False)
    title_text = font.render("Ranking", True, (255, 255, 255))
    screen.blit(title_text, [100, 50])

    for index, score in enumerate(scores):
        rank_text = font.render(f"{index + 1}. {score['Player_name']}: {score['Score']}", True, (255, 255, 255))
        screen.blit(rank_text, [50, 100 + index * 40])

    button_color = (0, 255, 0)
    restart_button_rect = pygame.Rect(50, 450, 150, 50)
    pygame.draw.rect(screen, button_color, restart_button_rect)
    restart_button_text = font.render("Restart", True, (0, 0, 0))
    screen.blit(restart_button_text, (restart_button_rect.x + 10, restart_button_rect.y + 10))

    end_button_rect = pygame.Rect(250, 450, 100, 50)
    pygame.draw.rect(screen, button_color, end_button_rect)
    end_button_text = font.render("End", True, (0, 0, 0))
    screen.blit(end_button_text, (end_button_rect.x + 10, end_button_rect.y + 10))

    pygame.display.flip()
    return restart_button_rect, end_button_rect