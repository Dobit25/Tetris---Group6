import pygame
import random

# Định nghĩa màu sắc
colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

# Lớp hình khối
class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # Hình khối I
        [[4, 5, 9, 10], [2, 6, 5, 9]],  # Hình khối Z
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # Hình khối S
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # Hình khối T
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # Hình khối L
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # Hình khối J
        [[1, 2, 5, 6]],  # Hình khối O
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


# Lớp trò chơi Tetris
class Tetris:
    def __init__(self, height, width):
        self.level = 2
        self.score = 0
        self.state = "start_screen"  # Trạng thái ban đầu
        self.paused = False  # Cờ tạm dừng
        self.field = []
        self.height = height
        self.width = width
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.figure = None
        self.high_score = 0  # Điểm cao nhất
        self.top_scores = []
        self.lines_cleared = 0
        self.reset_field()  # Khởi tạo lại trường chơi

    def restart_game(self):
        self.level = 2 
        self.score = 0
        self.paused = False
        self.lines_cleared = 0
        self.figure = None
        self.reset_field()

    def reset_field(self):
        self.field = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def new_figure(self):
        self.figure = Figure(3, 0)
        if self.intersects():
            self.state = "gameover"

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.lines_cleared += lines  # Cập nhật số dòng đã xóa
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
# Update high score if needed
        if self.score > self.high_score:
            self.high_score = self.score  # Update high score here

        self.new_figure()

    def update_top_scores(self):
        # Thêm điểm hiện tại vào danh sách top scores và giữ top 5
        self.top_scores.append(self.score)
        self.top_scores = sorted(self.top_scores, reverse=True)[:5]
    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

def draw_start_screen(screen, high_score):
    screen.fill((0, 0, 0))  # Màu nền đen
    font_title = pygame.font.SysFont('Calibri', 60, True, False)
    font_text = pygame.font.SysFont('Calibri', 40, True, False)

    # Vẽ tiêu đề trò chơi
    title_text = font_title.render("Tetris Game", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, 100))
    screen.blit(title_text, title_rect)

    # Vẽ điểm cao nhất
    highscore_text = font_text.render("Highscore: " + str(high_score), True, (255, 255, 255))
    highscore_rect = highscore_text.get_rect(center=(screen.get_width() // 2, 200))
    screen.blit(highscore_text, highscore_rect)

    # Vẽ nút bắt đầu
    button_color = (0, 128, 255)
    button_rect = pygame.Rect((screen.get_width() // 2 - 100, 300), (200, 60))
    pygame.draw.rect(screen, button_color, button_rect)

    # Vẽ chữ "Start" lên nút
    start_text = font_text.render("Start", True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=button_rect.center)
    screen.blit(start_text, start_text_rect)

    pygame.display.flip()  # Cập nhật màn hình

    return button_rect

def draw_pause_screen(screen):
    # Tô nền đen và thiết lập phông chữ
    screen.fill((0, 0, 0))
    font_title = pygame.font.SysFont('Calibri', 60, True, False)
    font_text = pygame.font.SysFont('Calibri', 40, True, False)

    # Hiển thị chữ "Paused"
    pause_text = font_title.render("Paused", True, (255, 255, 255))
    pause_rect = pause_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    screen.blit(pause_text, pause_rect)

    # Tạo nút "Resume" 
    button_color = (0, 128, 255)
    button_rect = pygame.Rect((screen.get_width() // 2 - 100, screen.get_height() // 2 + 50), (200, 60))
    pygame.draw.rect(screen, button_color, button_rect)

    # Hiển thị chữ "Resume" trên nút
    resume_text = font_text.render("Resume", True, (255, 255, 255))
    resume_text_rect = resume_text.get_rect(center=button_rect.center)
    screen.blit(resume_text, resume_text_rect)

    # Tạo nút "Pause" ở góc trên bên phải
    small_font = pygame.font.SysFont('Calibri', 30, True, False)
    pause_button_rect = pygame.Rect((screen.get_width() - 90, 10), (80, 40))  # Đặt góc phải trên cùng
    pygame.draw.rect(screen, (200, 0, 0), pause_button_rect)

    # Hiển thị chữ "Pause" trên nút góc phải
    pause_button_text = small_font.render("Escape", True, (255, 255, 255))
    pause_button_text_rect = pause_button_text.get_rect(center=pause_button_rect.center)
    screen.blit(pause_button_text, pause_button_text_rect)

    pygame.display.flip() 

    return button_rect, pause_button_rect

# Hàm vẽ màn hình Game Over với các nút Restart và Main Menu
def draw_game_over_popup(screen, score, high_score, lines_cleared, top_scores):
    screen.fill((30, 30, 30))  # Dark background color
    font_title = pygame.font.SysFont('Georgia', 50, True, False)
    font = pygame.font.SysFont('Georgia', 28, True, False)

    # Game Over title
    game_over_text = font_title.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, 50))

    # Display score, high score, and other details
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 120))

    high_score_text = font.render(f"High Score: {high_score}", True, (255, 215, 0))
    screen.blit(high_score_text, (screen.get_width() // 2 - high_score_text.get_width() // 2, 160))

    lines_text = font.render(f"Lines Cleared: {lines_cleared}", True, (173, 216, 230))
    screen.blit(lines_text, (screen.get_width() // 2 - lines_text.get_width() // 2, 200))

    top_scores_text = font.render("Top 5 High Scores:", True, (255, 255, 255))
    screen.blit(top_scores_text, (screen.get_width() // 2 - top_scores_text.get_width() // 2, 240))

    for i, top_score in enumerate(top_scores):
        score_line = font.render(f"{i + 1}. {top_score}", True, (255, 255, 255))
        screen.blit(score_line, (screen.get_width() // 2 - score_line.get_width() // 2, 280 + i * 30))

    # Draw "Restart" button
    restart_button = pygame.Rect(screen.get_width() // 2 - 100, 350, 200, 40)
    pygame.draw.rect(screen, (50, 205, 50), restart_button)  # Green color for the Restart button
    restart_text = font.render("Restart", True, (255, 255, 255))
    screen.blit(restart_text, (restart_button.x + restart_button.width // 2 - restart_text.get_width() // 2, restart_button.y + 5))

    # Draw "Main Menu" button below the Restart button
    menu_button = pygame.Rect(screen.get_width() // 2 - 100, 410, 200, 40)
    pygame.draw.rect(screen, (70, 130, 180), menu_button)  # Blue color for the Main Menu button
    menu_text = font.render("Main Menu", True, (255, 255, 255))
    screen.blit(menu_text, (menu_button.x + menu_button.width // 2 - menu_text.get_width() // 2, menu_button.y + 5))

    pygame.display.flip()  # Update the display
    return restart_button, menu_button

# Khởi tạo trò chơi
pygame.init()
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")

# Vòng lặp chính
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0
pressing_down = False

while not done:
    if game.state == "start_screen":
        button_rect = draw_start_screen(screen, game.high_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    game.state = "playing"
                    game.score = 0  # Đặt lại điểm số
                    game.lines_cleared = 0  
                    game.reset_field()  # Khởi tạo lại trường chơi
                    game.new_figure()  # Tạo hình khối mới
    elif game.state == "paused":
        button_rect, pause_button_rect = draw_pause_screen(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    game.state = "playing"
                if pause_button_rect.collidepoint(event.pos):
                    game.state = "start_screen"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.state = "start_screen"
    elif game.state == "gameover":
        # Vẽ màn hình Game Over với các nút
        restart_button, menu_button = draw_game_over_popup(screen, game.score, game.high_score, game.lines_cleared, game.top_scores)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    game.state = "playing"
                    game.score = 0
                    game.lines_cleared = 0
                    game.reset_field()
                    game.new_figure()
                    game.restart_game()
                    pressing_down = False
                if menu_button.collidepoint(event.pos):
                    game.state = "start_screen"
                    game.score = 0
                    game.lines_cleared = 0
                    game.reset_field()
                    game.new_figure()
                    game.restart_game()
                    pressing_down = False
    else:
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "playing" and not game.paused:
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

        screen.fill((255, 255, 255))

        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, (128, 128, 128), [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, colors[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        if game.figure is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.figure.image():
                        pygame.draw.rect(screen, colors[game.figure.color],
                                         [game.x + game.zoom * (j + game.figure.x) + 1,
                                          game.y + game.zoom * (i + game.figure.y) + 1,
                                          game.zoom - 2, game.zoom - 2])

        font_score = pygame.font.SysFont('Calibri', 25)
        score_text = font_score.render("Score: " + str(game.score), True, (0, 0, 0))
        screen.blit(score_text, [20, 20]) 

        font_lines = pygame.font.SysFont('Calibri', 25)
        lines_text = font_lines.render(f"Lines Cleared: {game.lines_cleared}", True, (0, 0, 0))
        screen.blit(lines_text, [20, 50]) 

        pygame.display.flip()  # Cập nhật màn hình
        clock.tick(fps)  # Giới hạn FPS

pygame.quit()
