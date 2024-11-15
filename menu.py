import pygame
import os
import json
from gameact import Tetris, draw_pause_screen, draw_game_screen
#note
def draw_start_screen(screen, high_score, background_image):
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

"""---------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------"""

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

"""---------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------"""

def draw_ending_screen(screen, player_name, score):
    screen.fill((0, 0, 0))  # Màu nền đen
    font = pygame.font.SysFont('Calibri', 40, True, False)
    ending_text = font.render(f"Name: {player_name}", True, (255, 255, 255))
    screen.blit(ending_text, [50, 100])

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, [50, 200])

    # Draw Restart button
    button_color = (0, 255, 0)
    restart_button_rect = pygame.Rect(50, 300, 150, 50)
    pygame.draw.rect(screen, button_color, restart_button_rect)
    restart_button_text = font.render("Restart", True, (0, 0, 0))
    screen.blit(restart_button_text, (restart_button_rect.x + 10, restart_button_rect.y + 10))

    # Draw Ranking button
    ranking_button_rect = pygame.Rect(50, 370, 150, 50)
    pygame.draw.rect(screen, button_color, ranking_button_rect)
    ranking_button_text = font.render("Ranking", True, (0, 0, 0))
    screen.blit(ranking_button_text, (ranking_button_rect.x + 10, ranking_button_rect.y + 10))

    # Draw End button
    end_button_rect = pygame.Rect(250, 300, 100, 50)
    pygame.draw.rect(screen, button_color, end_button_rect)
    end_button_text = font.render("End", True, (0, 0, 0))
    screen.blit(end_button_text, (end_button_rect.x + 10, end_button_rect.y + 10))

    pygame.display.flip()  # Cập nhật màn hình

    return restart_button_rect, ranking_button_rect, end_button_rect

"""---------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------"""

def load_scores():
    if os.path.exists("player_scores.json"):
        with open("player_scores.json", "r") as file:
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
    with open("player_scores.json", "w") as file:
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

def main():
    pygame.init()
    size = (400, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris")

    # Load the background image
    try:
        background_image = pygame.image.load("tetris_image.jpg")
        background_image = pygame.transform.scale(background_image, size)
    except pygame.error as e:
        print(f"Cannot load background image: {e}")
        return

    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0
    pressing_down = False
    player_name = ""
    input_active = False

    while not done:
        if game.state == "start_screen":
            button_rect = draw_start_screen(screen, game.high_score, background_image)  # Vẽ màn hình chào
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        game.state = "name_input"
                        input_active = True
        elif game.state == "name_input":
            input_box = draw_name_input_screen(screen, player_name)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game.state = "playing"
                        game.score = 0  # Đặt lại điểm số
                        game.reset_field()  # Khởi tạo lại trường chơi
                        game.new_figure()  # Tạo hình khối mới
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode
        elif game.state == "paused":
            resume_button_rect, restart_button_rect, quit_button_rect = draw_pause_screen(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_button_rect.collidepoint(event.pos):
                        game.state = "playing"  # Tiếp tục trò chơi
                    elif restart_button_rect.collidepoint(event.pos):
                        game.state = "name_input"  # Restart the game
                        player_name = ""
                    elif quit_button_rect.collidepoint(event.pos):
                        done = True  # Quit the game
        elif game.state == "gameover":
            restart_button_rect, ranking_button_rect, end_button_rect = draw_ending_screen(screen, player_name, game.score)
            save_score(player_name, game.score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):
                        game.state = "name_input"  # Restart the game
                        player_name = ""
                    elif ranking_button_rect.collidepoint(event.pos):
                        game.state = "ranking"  # Chuyển sang màn hình xếp hạng
                    elif end_button_rect.collidepoint(event.pos):
                        done = True  # Exit the game
        elif game.state == "ranking":
            restart_button_rect, end_button_rect = draw_ranking_screen(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):
                        game.state = "name_input"
                        player_name = ""
                    elif end_button_rect.collidepoint(event.pos):
                        done = True  # Exit the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        game.state = "start_screen"
        else:
            if game.figure is None:
                game.new_figure()
            counter += 1
            if counter > 100000:
                counter = 0

            if counter % (fps // game.level // 2) == 0 or pressing_down:
                if game.state == "playing" :
                    game.go_down()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        game.rotate()
                    if event.key == pygame.K_DOWN:
                        pressing_down = True
                    if event.key == pygame.K_LEFT:
                        game.go_side(-1)
                    if event.key == pygame.K_RIGHT:
                        game.go_side(1)
                    if event.key == pygame.K_SPACE:
                        game.go_space()
                    if event.key == pygame.K_p:  # Phím P để tạm dừng
                        game.state = "paused"
                    if event.key == pygame.K_ESCAPE:
                        game.state = "start_screen"  # Quay lại màn hình chào

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        pressing_down = False

            draw_game_screen(screen, game)

        pygame.display.flip()  # Cập nhật màn hình
        clock.tick(fps)  # Giới hạn FPS

    pygame.quit()

if __name__ == "__main__":
    main()
    #jdskflajdsfkldsj
