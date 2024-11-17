import pygame, json

from tetris_gameplay_operation import Tetris
from data_scores import load_scores, save_score, draw_ranking_screen
from start_screen import draw_start_screen, draw_name_input_screen, draw_sound_screen
from gameplay_screen import draw_game_screen
from pause_screen import draw_pause_screen, draw_pause_button
from ending_screen import draw_game_over_popup
from backgrounds_and_sound import sound, menu_bg, gameplay_bg, toggle_mute

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
    # button_resume_pressed = False
    # button_restart_pressed = False
    # button_menu_pressed = False
    button_states = {
    "button_resume_pressed": False,
    "button_restart_pressed": False,
    "button_menu_pressed": False
    }

    while not done:
        if pygame.mixer.music.get_busy() == False:
            sound()

        if game.state == "start_screen":
            start_button_rect, ranking_button_rect, sound_button_rect, exit_button_rect = draw_start_screen(screen, menu_bg)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        game.state = "name_input"
                    elif ranking_button_rect.collidepoint(event.pos):
                        game.state = "ranking"
                    elif sound_button_rect.collidepoint(event.pos):
                        game.state = "sound_change"
                    elif exit_button_rect.collidepoint(event.pos):
                        done = True
                        
        elif game.state == "sound_change":
            increase_button_rect, decrease_button_rect, mute_button_rect, back_button_rect = draw_sound_screen(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if increase_button_rect.collidepoint(event.pos):
                        volume = pygame.mixer.music.get_volume()
                        pygame.mixer.music.set_volume(min(volume + 0.2, 1.0))
                    elif decrease_button_rect.collidepoint(event.pos):
                        volume = pygame.mixer.music.get_volume()
                        pygame.mixer.music.set_volume(max(volume - 0.2, 0.0))
                    elif mute_button_rect.collidepoint(event.pos):
                        toggle_mute()
                    elif back_button_rect.collidepoint(event.pos):
                        game.state = "start_screen"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game.state = "start_screen"

        # ... (rest of the code remains unchanged)
        
        elif game.state == "name_input":
            input_box, submit_button_rect = draw_name_input_screen(screen, player_name)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game.state = "playing"
                        game.score = 0  # Reset score
                        game.reset_field()  # Reset field
                        game.new_figure()  # Create new figure
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if submit_button_rect.collidepoint(event.pos):
                        game.state = "playing"
                        game.score = 0  # Reset score
                        game.reset_field()  # Reset field
                        game.new_figure()  # Create new figure

        # ... (rest of the code remains unchanged)


        elif game.state == "paused":
            # Truyền từ điển trạng thái vào hàm nhỏ
            button_rect_resume, button_rect_restart, button_rect_menu = draw_pause_screen(screen, button_states)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game.state = "playing"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect_resume.collidepoint(event.pos):
                        button_states["button_resume_pressed"] = True
                    elif button_rect_restart.collidepoint(event.pos):
                        button_states["button_restart_pressed"] = True
                    elif button_rect_menu.collidepoint(event.pos):
                        button_states["button_menu_pressed"] = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if button_states["button_resume_pressed"]:
                        if button_rect_resume.collidepoint(event.pos):
                            game.state = "playing"
                        button_states["button_resume_pressed"] = False
                    elif button_states["button_restart_pressed"]:
                        if button_rect_restart.collidepoint(event.pos):
                            game.score = 0
                            game.reset_field()
                            game.new_figure()
                            game.state = "playing"
                        button_states["button_restart_pressed"] = False
                    elif button_states["button_menu_pressed"]:
                        if button_rect_menu.collidepoint(event.pos):
                            game.state = "start_screen"
                        button_states["button_menu_pressed"] = False

        elif game.state == "gameover":
            save_score(player_name, game.score)
            with open('player_data.json', 'r') as file:
                data = json.load(file)
            highest_score = data[0]['Score']

            restart_button, menu_button, ranking_button = draw_game_over_popup(screen, game.score, highest_score)
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
                            game.reset_field()
                            game.new_figure()
                            pressing_down = False
                            game_over = False
                        elif menu_button.collidepoint(event.pos):
                            game.state = "start_screen"
                            game.score = 0
                            game.reset_field()
                            game.new_figure()
                            pressing_down = False
                            game_over = False
                            player_name = ""
                        elif ranking_button.collidepoint(event.pos):
                            game.state = "ranking"
                            game.score = 0
                            game.reset_field()
                            game.new_figure()
                            pressing_down = False
                            game_over = False
                            
        elif game.state == "ranking":
            menu_button_rect = draw_ranking_screen(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button_rect.collidepoint(event.pos):
                        game.state = "start_screen"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        game.state = "start_screen"
                        
        else:
            draw_game_screen(screen, game, gameplay_bg)
            draw_pause_button(screen)
            if game.figure is None:
                game.new_figure()
            counter += 1
            if counter > 100000:
                counter = 0

            game.falling_speed(counter, fps, pressing_down)

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_rect_pause = draw_pause_button(screen)
                    if button_rect_pause.collidepoint(event.pos):  # Kiểm tra vị trí chuột
                        game.state = "paused"                     # Chuy
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        pygame.display.flip() 
        clock.tick(fps)  

    pygame.quit()

if __name__ == "__main__":
    main()
    
