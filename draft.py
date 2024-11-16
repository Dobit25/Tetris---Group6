import pygame, json

from tetris_gameplay_operation import Tetris
from data_scores import load_scores, save_score, draw_ranking_screen
from start_screen import draw_start_screen, draw_name_input_screen
from gameplay_screen import draw_game_screen
from pause_screen import draw_pause_screen
from ending_screen import draw_game_over_popup
from backgrounds_and_sound import sound, menu_bg, gameplay_bg

def main():
    pygame.init()
    size = (400, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris")

    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0
    pressing_down = False
    player_name = ""
    # input_active = False
    sound()

    while not done:
        if pygame.mixer.music.get_busy() == False:
            sound()

        if game.state == "start_screen":
            button_rect = draw_start_screen(screen, menu_bg)  # Vẽ màn hình chào
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        game.state = "name_input"
                        # input_active = True

        elif game.state == "name_input":
            # input_box = draw_name_input_screen(screen, player_name)
            draw_name_input_screen(screen, player_name)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game.state = "playing"
                        game.score = 0  # Đặt lại điểm số
                        game.reset_field()  # Khởi tạo lại trường chơi
                        game.new_figure()  # Tạo hình khối mới
                        # input_active = False
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
            save_score(player_name, game.score)
            with open('player_data.json', 'r') as file:
                data = json.load(file)
            highest_score = data[0]['Score']
            print(highest_score)

            restart_button, menu_button, ranking_button = draw_game_over_popup(screen, game.score, game.lines_cleared, highest_score, game.top_scores)
            game_over = True
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        game_over = False
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            game.state = "playing"
                            game.score = 0
                            game.lines_cleared = 0
                            game.reset_field()
                            game.new_figure()
                            pressing_down = False
                            game_over = False
                        elif menu_button.collidepoint(event.pos):
                            game.state = "start_screen"
                            game.score = 0
                            game.lines_cleared = 0
                            game.reset_field()
                            game.new_figure()
                            pressing_down = False
                            game_over = False
                        elif ranking_button.collidepoint(event.pos):
                            draw_ranking_screen(screen)
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
                        
                    if event.key == pygame.K_m:  # Kiểm tra nếu phím "M" được nhấn
                        if pygame.mixer.music.get_busy():  # Kiểm tra nếu nhạc đang chạy
                            pygame.mixer.music.pause()  # Tạm dừng nhạc
                        else:
                            pygame.mixer.music.unpause()  # Tiếp tục phát nhạc       
                                     
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

            draw_game_screen(screen, game, gameplay_bg)

        pygame.display.flip() 
        clock.tick(fps)  

    pygame.quit()

if __name__ == "__main__":
    main()
    # with open('player_data.json', 'r') as file:
    #     data = json.load(file)

    # # Lấy điểm từ dictionary đầu tiên
    # first_player_score = data[0]['Score']

    # print(first_player_score)