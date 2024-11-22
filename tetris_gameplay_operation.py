from figures import Figure
from backgrounds_and_sound import sound_effect, show_bubbles
import pygame
size = (800, 700)  # Updated window size
screen = pygame.display.set_mode(size)
class Tetris:
    def __init__(self, height, width):
        self.level = 0.6
        self.score = 0
        self.total_lines_cleared = 0
        self.state = "start_screen"  # Trạng thái ban đầu
        self.field = []
        self.height = height
        self.width = width
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.figure = None

        self.reset_field()  # Khởi tạo lại trường chơi

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
            combo = 0
            for i in range(1, self.height):
                zeros = 0
                for j in range(self.width):
                    if self.field[i][j] == 0:
                        zeros += 1
                if zeros == 0:
                    lines += 1
                    sound_effect()
                    show_bubbles(screen)
                    for i1 in range(i, 1, -1):
                        for j in range(self.width):
                            self.field[i1][j] = self.field[i1 - 1][j]
            if lines > 0:
                self.total_lines_cleared += lines  # Update total lines cleared
                if lines == 1:
                    self.score += 100
                    combo = 0
                elif lines >= 2:
                    combo += 1
                    if lines == 2:
                        self.score += 300
                    elif lines == 3:
                        self.score += 500
                    elif lines == 4:
                        self.score += 800
                if combo > 1:
                    self.score += 50 * (combo - 1)
                if self.level < 2:
                    if self.total_lines_cleared % 10 == 0:  # Check total lines cleareds
                        self.level += 0.3
                        print(self.level)

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

    def falling_speed(self, counter, fps, pressing_down: bool):
        if counter % (fps // self.level // 2) == 0 or pressing_down:
            if self.state == "playing" :
                self.go_down()
