# Lớp hình khối
import random
colors = [
    (255, 128, 102), 
    (70, 223, 177), # xanh la
    (255, 170, 128), # cam nhạt
    (196, 140, 179), # hồng ảnh 2
    (216, 191, 216), # purple, 
    (229, 201, 215), # hồng ảnh 3
    (186, 214, 235), #sky
]
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

