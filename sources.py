import pygame
import random

# Định nghĩa màu sắc sử dụng trong trò chơi
colors = [
    (0, 0, 0),        # Màu đen
    (120, 37, 179),   # Màu tím
    (100, 179, 179),  # Màu xanh lá
    (80, 34, 22),     # Màu nâu
    (80, 134, 22),    # Màu xanh lá cây
    (180, 34, 22),    # Màu đỏ
    (180, 34, 122),   # Màu hồng
]

# Lớp đại diện cho hình khối Tetris
class Figure:
    x = 0  # Tọa độ x của khối
    y = 0  # Tọa độ y của khối

    # Danh sách các hình dạng khối Tetris
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],    # Hình I
        [[4, 5, 9, 10], [2, 6, 5, 9]],    # Hình J
        [[6, 7, 9, 10], [1, 5, 6, 10]],   # Hình L
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # Hình T
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # Hình S
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],   # Hình Z
        [[1, 2, 5, 6]],    # Hình O
    ]

    # Khởi tạo hình khối với tọa độ x, y
    def __init__(self, x, y):
        self.x = x  # Tọa độ x
        self.y = y  # Tọa độ y
        self.type = random.randint(0, len(self.figures) - 1)  # Chọn ngẫu nhiên hình dạng
        self.color = random.randint(1, len(colors) - 1)  # Chọn ngẫu nhiên màu sắc
        self.rotation = 0  # Trạng thái xoay ban đầu

    # Trả về hình ảnh hiện tại của khối
    def image(self):
        return self.figures[self.type][self.rotation]

    # Xoay hình khối
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


# Lớp đại diện cho trò chơi Tetris
class Tetris:
    def __init__(self, height, width):
        self.level = 2  # Mức độ trò chơi
        self.score = 0  # Điểm số
        self.state = "start"  # Trạng thái trò chơi
        self.field = []  # Bàn chơi
        self.height = 0  # Chiều cao bàn chơi
        self.width = 0   # Chiều rộng bàn chơi
        self.x = 100     # Tọa độ x của bàn chơi
        self.y = 60      # Tọa độ y của bàn chơi
        self.zoom = 20   # Kích thước của mỗi ô
        self.figure = None  # Hình khối hiện tại

        # Khởi tạo bàn chơi với chiều cao và chiều rộng
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)  # Khởi tạo các ô trong bàn chơi với giá trị 0
            self.field.append(new_line)

    # Tạo một hình khối mới
    def new_figure(self):
        self.figure = Figure(3, 0)

    # Kiểm tra va chạm của hình khối
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True  # Có va chạm
        return intersection

    # Xử lý khi một dòng đầy ô
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1  # Đếm số ô trống
            if zeros == 0:  # Nếu dòng đầy ô
                lines += 1  # Tăng số dòng đã xóa
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]  # Dịch các dòng ở trên xuống
        self.score += lines ** 2  # Cộng điểm theo số dòng đã xóa

    # Di chuyển khối xuống cho đến khi va chạm
    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()  # Cố định vị trí khối

    # Di chuyển khối xuống một ô
    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()  # Cố định vị trí khối

    # Cố định khối vào bàn chơi
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color  # Gán màu cho ô
        self.break_lines()  # Kiểm tra và xử lý các dòng đầy ô
        self.new_figure()  # Tạo hình khối mới
        if self.intersects():  # Kiểm tra va chạm với khối mới
            self.state = "gameover"  # Kết thúc trò chơi

    # Di chuyển khối sang trái hoặc phải
    def go_side(self, dx):
        old_x = self.figure.x  # Lưu tọa độ x cũ
        self.figure.x += dx  # Cập nhật tọa độ x
        if self.intersects():  # Kiểm tra va chạm
            self.figure.x = old_x  # Khôi phục tọa độ x cũ

    # Xoay khối và kiểm tra va chạm
    def rotate(self):
        old_rotation = self.figure.rotation  # Lưu trạng thái xoay cũ
        self.figure.rotate()  # Xoay khối
        if self.intersects():  # Kiểm tra va chạm
            self.figure.rotation = old_rotation  # Khôi phục trạng thái xoay cũ


# Khởi tạo Pygame
pygame.init()

# Định nghĩa màu sắc cho màn hình
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)  # Kích thước màn hình
screen = pygame.display.set_mode(size)  # Tạo cửa sổ trò chơi

pygame.display.set_caption("Tetris")  # Tiêu đề cửa sổ

# Vòng lặp chính của trò chơi
done = False
clock = pygame.time.Clock()  # Đồng hồ để điều khiển tốc độ trò chơi
fps = 25  # Tốc độ khung hình
game = Tetris(20, 10)  # Khởi tạo trò chơi với kích thước bàn chơi
counter = 0

pressing_down = False  # Biến kiểm tra phím xuống có đang nhấn hay không

while not done:
    if game.figure is None:
        game.new_figure()  # Tạo hình khối mới nếu chưa có

    counter += 1
    if counter > 100000:
        counter = 0

    # Di chuyển khối xuống theo tốc độ
    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    # Xử lý sự kiện từ bàn phím
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Thoát trò chơi nếu người dùng đóng cửa sổ
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()  # Xoay khối
            if event.key == pygame.K_DOWN:
                pressing_down = True  # Bắt đầu nhấn phím xuống
            if event.key == pygame.K_LEFT:
                game.go_side(-1)  # Di chuyển khối sang trái
            if event.key == pygame.K_RIGHT:
                game.go_side(1)  # Di chuyển khối sang phải
            if event.key == pygame.K_SPACE:
                game.go_space()  # Thả khối xuống
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)  # Khởi động lại trò chơi

        if event.type == pygame.KEYUP:  # Khi phím được nhả ra
            if event.key == pygame.K_DOWN:
                pressing_down = False  # Ngừng nhấn phím xuống

    screen.fill(WHITE)  # Làm mới màn hình với màu trắng

    # Vẽ bàn chơi
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    # Vẽ hình khối hiện tại
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    # Hiển thị điểm số
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)  # Điểm số
    text_game_over = font1.render("Game Over", True, (255, 125, 0))  # Thông báo game over
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))  # Hướng dẫn nhấn ESC để khởi động lại

    # Hiển thị điểm số và thông báo game over nếu có
    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()  # Cập nhật màn hình
    clock.tick(fps)  # Giới hạn tốc độ khung hình

pygame.quit()  # Thoát Pygame khi trò chơi kết thúc

