{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pygame\n",
    "import random\n",
    "\n",
    "# Định nghĩa màu sắc\n",
    "colors = [\n",
    "    (0, 0, 0),\n",
    "    (120, 37, 179),\n",
    "    (100, 179, 179),\n",
    "    (80, 34, 22),\n",
    "    (80, 134, 22),\n",
    "    (180, 34, 22),\n",
    "    (180, 34, 122),\n",
    "]\n",
    "\n",
    "# Lớp hình khối\n",
    "class Figure:\n",
    "    x = 0\n",
    "    y = 0\n",
    "\n",
    "    figures = [\n",
    "        [[1, 5, 9, 13], [4, 5, 6, 7]],  # Hình khối I\n",
    "        [[4, 5, 9, 10], [2, 6, 5, 9]],  # Hình khối Z\n",
    "        [[6, 7, 9, 10], [1, 5, 6, 10]],  # Hình khối S\n",
    "        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # Hình khối T\n",
    "        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # Hình khối L\n",
    "        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # Hình khối J\n",
    "        [[1, 2, 5, 6]],  # Hình khối O\n",
    "    ]\n",
    "\n",
    "    def __init__(self, x, y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.type = random.randint(0, len(self.figures) - 1)\n",
    "        self.color = random.randint(1, len(colors) - 1)\n",
    "        self.rotation = 0\n",
    "\n",
    "    def image(self):\n",
    "        return self.figures[self.type][self.rotation]\n",
    "\n",
    "    def rotate(self):\n",
    "        self.rotation = (self.rotation + 1) % len(self.figures[self.type])\n",
    "\n",
    "\n",
    "# Lớp trò chơi Tetris\n",
    "class Tetris:\n",
    "    def __init__(self, height, width):\n",
    "        self.level = 2\n",
    "        self.score = 0\n",
    "        self.state = \"start_screen\"  # Trạng thái ban đầu\n",
    "        self.paused = False  # Cờ tạm dừng\n",
    "        self.field = []\n",
    "        self.height = height\n",
    "        self.width = width\n",
    "        self.x = 100\n",
    "        self.y = 60\n",
    "        self.zoom = 20\n",
    "        self.figure = None\n",
    "        self.high_score = 0  # Điểm cao nhất\n",
    "        self.top_scores = []\n",
    "        self.lines_cleared = 0\n",
    "        self.reset_field()  # Khởi tạo lại trường chơi\n",
    "\n",
    "    def restart_game(self):\n",
    "        self.level = 2 \n",
    "        self.score = 0\n",
    "        self.paused = False\n",
    "        self.lines_cleared = 0\n",
    "        self.figure = None\n",
    "        self.reset_field()\n",
    "\n",
    "    def reset_field(self):\n",
    "        self.field = [[0 for _ in range(self.width)] for _ in range(self.height)]\n",
    "\n",
    "    def new_figure(self):\n",
    "        self.figure = Figure(3, 0)\n",
    "        if self.intersects():\n",
    "            self.state = \"gameover\"\n",
    "\n",
    "    def intersects(self):\n",
    "        intersection = False\n",
    "        for i in range(4):\n",
    "            for j in range(4):\n",
    "                if i * 4 + j in self.figure.image():\n",
    "                    if i + self.figure.y > self.height - 1 or \\\n",
    "                            j + self.figure.x > self.width - 1 or \\\n",
    "                            j + self.figure.x < 0 or \\\n",
    "                            self.field[i + self.figure.y][j + self.figure.x] > 0:\n",
    "                        intersection = True\n",
    "        return intersection\n",
    "\n",
    "    def break_lines(self):\n",
    "        lines = 0\n",
    "        for i in range(1, self.height):\n",
    "            zeros = 0\n",
    "            for j in range(self.width):\n",
    "                if self.field[i][j] == 0:\n",
    "                    zeros += 1\n",
    "            if zeros == 0:\n",
    "                lines += 1\n",
    "                for i1 in range(i, 1, -1):\n",
    "                    for j in range(self.width):\n",
    "                        self.field[i1][j] = self.field[i1 - 1][j]\n",
    "        self.lines_cleared += lines  # Cập nhật số dòng đã xóa\n",
    "        self.score += lines ** 2\n",
    "\n",
    "    def go_space(self):\n",
    "        while not self.intersects():\n",
    "            self.figure.y += 1\n",
    "        self.figure.y -= 1\n",
    "        self.freeze()\n",
    "\n",
    "    def go_down(self):\n",
    "        self.figure.y += 1\n",
    "        if self.intersects():\n",
    "            self.figure.y -= 1\n",
    "            self.freeze()\n",
    "\n",
    "    def freeze(self):\n",
    "        for i in range(4):\n",
    "            for j in range(4):\n",
    "                if i * 4 + j in self.figure.image():\n",
    "                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color\n",
    "        self.break_lines()\n",
    "        self.new_figure()\n",
    "# Update high score if needed\n",
    "        if self.score > self.high_score:\n",
    "            self.high_score = self.score  # Update high score here\n",
    "\n",
    "        self.new_figure()\n",
    "\n",
    "    def update_top_scores(self):\n",
    "        # Thêm điểm hiện tại vào danh sách top scores và giữ top 5\n",
    "        self.top_scores.append(self.score)\n",
    "        self.top_scores = sorted(self.top_scores, reverse=True)[:5]\n",
    "    def go_side(self, dx):\n",
    "        old_x = self.figure.x\n",
    "        self.figure.x += dx\n",
    "        if self.intersects():\n",
    "            self.figure.x = old_x\n",
    "\n",
    "    def rotate(self):\n",
    "        old_rotation = self.figure.rotation\n",
    "        self.figure.rotate()\n",
    "        if self.intersects():\n",
    "            self.figure.rotation = old_rotation\n",
    "\n",
    "def draw_start_screen(screen, high_score):\n",
    "    screen.fill((0, 0, 0))  # Màu nền đen\n",
    "    font_title = pygame.font.SysFont('Calibri', 60, True, False)\n",
    "    font_text = pygame.font.SysFont('Calibri', 40, True, False)\n",
    "\n",
    "    # Vẽ tiêu đề trò chơi\n",
    "    title_text = font_title.render(\"Tetris Game\", True, (255, 255, 255))\n",
    "    title_rect = title_text.get_rect(center=(screen.get_width() // 2, 100))\n",
    "    screen.blit(title_text, title_rect)\n",
    "\n",
    "    # Vẽ điểm cao nhất\n",
    "    highscore_text = font_text.render(\"Highscore: \" + str(high_score), True, (255, 255, 255))\n",
    "    highscore_rect = highscore_text.get_rect(center=(screen.get_width() // 2, 200))\n",
    "    screen.blit(highscore_text, highscore_rect)\n",
    "\n",
    "    # Vẽ nút bắt đầu\n",
    "    button_color = (0, 128, 255)\n",
    "    button_rect = pygame.Rect((screen.get_width() // 2 - 100, 300), (200, 60))\n",
    "    pygame.draw.rect(screen, button_color, button_rect)\n",
    "\n",
    "    # Vẽ chữ \"Start\" lên nút\n",
    "    start_text = font_text.render(\"Start\", True, (255, 255, 255))\n",
    "    start_text_rect = start_text.get_rect(center=button_rect.center)\n",
    "    screen.blit(start_text, start_text_rect)\n",
    "\n",
    "    pygame.display.flip()  # Cập nhật màn hình\n",
    "\n",
    "    return button_rect\n",
    "\n",
    "def draw_pause_screen(screen):\n",
    "    # Tô nền đen và thiết lập phông chữ\n",
    "    screen.fill((0, 0, 0))\n",
    "    font_title = pygame.font.SysFont('Calibri', 60, True, False)\n",
    "    font_text = pygame.font.SysFont('Calibri', 40, True, False)\n",
    "\n",
    "    # Hiển thị chữ \"Paused\"\n",
    "    pause_text = font_title.render(\"Paused\", True, (255, 255, 255))\n",
    "    pause_rect = pause_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))\n",
    "    screen.blit(pause_text, pause_rect)\n",
    "\n",
    "    # Tạo nút \"Resume\" \n",
    "    button_color = (0, 128, 255)\n",
    "    button_rect = pygame.Rect((screen.get_width() // 2 - 100, screen.get_height() // 2 + 50), (200, 60))\n",
    "    pygame.draw.rect(screen, button_color, button_rect)\n",
    "\n",
    "    # Hiển thị chữ \"Resume\" trên nút\n",
    "    resume_text = font_text.render(\"Resume\", True, (255, 255, 255))\n",
    "    resume_text_rect = resume_text.get_rect(center=button_rect.center)\n",
    "    screen.blit(resume_text, resume_text_rect)\n",
    "\n",
    "    # Tạo nút \"Pause\" ở góc trên bên phải\n",
    "    small_font = pygame.font.SysFont('Calibri', 30, True, False)\n",
    "    pause_button_rect = pygame.Rect((screen.get_width() - 90, 10), (80, 40))  # Đặt góc phải trên cùng\n",
    "    pygame.draw.rect(screen, (200, 0, 0), pause_button_rect)\n",
    "\n",
    "    # Hiển thị chữ \"Pause\" trên nút góc phải\n",
    "    pause_button_text = small_font.render(\"Escape\", True, (255, 255, 255))\n",
    "    pause_button_text_rect = pause_button_text.get_rect(center=pause_button_rect.center)\n",
    "    screen.blit(pause_button_text, pause_button_text_rect)\n",
    "\n",
    "    pygame.display.flip() \n",
    "\n",
    "    return button_rect, pause_button_rect\n",
    "\n",
    "# Hàm vẽ màn hình Game Over với các nút Restart và Main Menu\n",
    "def draw_game_over_popup(screen, score, high_score, lines_cleared, top_scores):\n",
    "    screen.fill((30, 30, 30))  # Dark background color\n",
    "    font_title = pygame.font.SysFont('Georgia', 50, True, False)\n",
    "    font = pygame.font.SysFont('Georgia', 28, True, False)\n",
    "\n",
    "    # Game Over title\n",
    "    game_over_text = font_title.render(\"GAME OVER\", True, (255, 0, 0))\n",
    "    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, 50))\n",
    "\n",
    "    # Display score, high score, and other details\n",
    "    score_text = font.render(f\"Score: {score}\", True, (255, 255, 255))\n",
    "    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 120))\n",
    "\n",
    "    high_score_text = font.render(f\"High Score: {high_score}\", True, (255, 215, 0))\n",
    "    screen.blit(high_score_text, (screen.get_width() // 2 - high_score_text.get_width() // 2, 160))\n",
    "\n",
    "    lines_text = font.render(f\"Lines Cleared: {lines_cleared}\", True, (173, 216, 230))\n",
    "    screen.blit(lines_text, (screen.get_width() // 2 - lines_text.get_width() // 2, 200))\n",
    "\n",
    "    top_scores_text = font.render(\"Top 5 High Scores:\", True, (255, 255, 255))\n",
    "    screen.blit(top_scores_text, (screen.get_width() // 2 - top_scores_text.get_width() // 2, 240))\n",
    "\n",
    "    for i, top_score in enumerate(top_scores):\n",
    "        score_line = font.render(f\"{i + 1}. {top_score}\", True, (255, 255, 255))\n",
    "        screen.blit(score_line, (screen.get_width() // 2 - score_line.get_width() // 2, 280 + i * 30))\n",
    "\n",
    "    # Draw \"Restart\" button\n",
    "    restart_button = pygame.Rect(screen.get_width() // 2 - 100, 350, 200, 40)\n",
    "    pygame.draw.rect(screen, (50, 205, 50), restart_button)  # Green color for the Restart button\n",
    "    restart_text = font.render(\"Restart\", True, (255, 255, 255))\n",
    "    screen.blit(restart_text, (restart_button.x + restart_button.width // 2 - restart_text.get_width() // 2, restart_button.y + 5))\n",
    "\n",
    "    # Draw \"Main Menu\" button below the Restart button\n",
    "    menu_button = pygame.Rect(screen.get_width() // 2 - 100, 410, 200, 40)\n",
    "    pygame.draw.rect(screen, (70, 130, 180), menu_button)  # Blue color for the Main Menu button\n",
    "    menu_text = font.render(\"Main Menu\", True, (255, 255, 255))\n",
    "    screen.blit(menu_text, (menu_button.x + menu_button.width // 2 - menu_text.get_width() // 2, menu_button.y + 5))\n",
    "\n",
    "    pygame.display.flip()  # Update the display\n",
    "    return restart_button, menu_button\n",
    "\n",
    "# Khởi tạo trò chơi\n",
    "pygame.init()\n",
    "size = (400, 500)\n",
    "screen = pygame.display.set_mode(size)\n",
    "pygame.display.set_caption(\"Tetris\")\n",
    "\n",
    "# Vòng lặp chính\n",
    "done = False\n",
    "clock = pygame.time.Clock()\n",
    "fps = 25\n",
    "game = Tetris(20, 10)\n",
    "counter = 0\n",
    "pressing_down = False\n",
    "\n",
    "while not done:\n",
    "    if game.state == \"start_screen\":\n",
    "        button_rect = draw_start_screen(screen, game.high_score)\n",
    "        for event in pygame.event.get():\n",
    "            if event.type == pygame.QUIT:\n",
    "                done = True\n",
    "            if event.type == pygame.MOUSEBUTTONDOWN:\n",
    "                if button_rect.collidepoint(event.pos):\n",
    "                    game.state = \"playing\"\n",
    "                    game.score = 0  # Đặt lại điểm số\n",
    "                    game.lines_cleared = 0  \n",
    "                    game.reset_field()  # Khởi tạo lại trường chơi\n",
    "                    game.new_figure()  # Tạo hình khối mới\n",
    "    elif game.state == \"paused\":\n",
    "        button_rect, pause_button_rect = draw_pause_screen(screen)\n",
    "        for event in pygame.event.get():\n",
    "            if event.type == pygame.QUIT:\n",
    "                done = True\n",
    "            if event.type == pygame.MOUSEBUTTONDOWN:\n",
    "                if button_rect.collidepoint(event.pos):\n",
    "                    game.state = \"playing\"\n",
    "                if pause_button_rect.collidepoint(event.pos):\n",
    "                    game.state = \"start_screen\"\n",
    "            if event.type == pygame.KEYDOWN:\n",
    "                if event.key == pygame.K_ESCAPE:\n",
    "                    game.state = \"start_screen\"\n",
    "    elif game.state == \"gameover\":\n",
    "        # Vẽ màn hình Game Over với các nút\n",
    "        restart_button, menu_button = draw_game_over_popup(screen, game.score, game.high_score, game.lines_cleared, game.top_scores)\n",
    "\n",
    "        for event in pygame.event.get():\n",
    "            if event.type == pygame.QUIT:\n",
    "                done = True\n",
    "            \n",
    "            if event.type == pygame.MOUSEBUTTONDOWN:\n",
    "                if restart_button.collidepoint(event.pos):\n",
    "                    game.state = \"playing\"\n",
    "                    game.score = 0\n",
    "                    game.lines_cleared = 0\n",
    "                    game.reset_field()\n",
    "                    game.new_figure()\n",
    "                    game.restart_game()\n",
    "                    pressing_down = False\n",
    "                if menu_button.collidepoint(event.pos):\n",
    "                    game.state = \"start_screen\"\n",
    "                    game.score = 0\n",
    "                    game.lines_cleared = 0\n",
    "                    game.reset_field()\n",
    "                    game.new_figure()\n",
    "                    game.restart_game()\n",
    "                    pressing_down = False\n",
    "    else:\n",
    "        if game.figure is None:\n",
    "            game.new_figure()\n",
    "        counter += 1\n",
    "        if counter > 100000:\n",
    "            counter = 0\n",
    "\n",
    "        if counter % (fps // game.level // 2) == 0 or pressing_down:\n",
    "            if game.state == \"playing\" and not game.paused:\n",
    "                game.go_down()\n",
    "\n",
    "        for event in pygame.event.get():\n",
    "            if event.type == pygame.QUIT:\n",
    "                done = True\n",
    "            if event.type == pygame.KEYDOWN:\n",
    "                if event.key == pygame.K_UP:\n",
    "                    game.rotate()\n",
    "                if event.key == pygame.K_DOWN:\n",
    "                    pressing_down = True\n",
    "                if event.key == pygame.K_LEFT:\n",
    "                    game.go_side(-1)\n",
    "                if event.key == pygame.K_RIGHT:\n",
    "                    game.go_side(1)\n",
    "                if event.key == pygame.K_SPACE:\n",
    "                    game.go_space()\n",
    "                if event.key == pygame.K_p:  # Phím P để tạm dừng\n",
    "                    game.state = \"paused\"\n",
    "                if event.key == pygame.K_ESCAPE:\n",
    "                    game.state = \"start_screen\"  # Quay lại màn hình chào\n",
    "\n",
    "            if event.type == pygame.KEYUP:\n",
    "                if event.key == pygame.K_DOWN:\n",
    "                    pressing_down = False\n",
    "\n",
    "        screen.fill((255, 255, 255))\n",
    "\n",
    "        for i in range(game.height):\n",
    "            for j in range(game.width):\n",
    "                pygame.draw.rect(screen, (128, 128, 128), [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)\n",
    "                if game.field[i][j] > 0:\n",
    "                    pygame.draw.rect(screen, colors[game.field[i][j]],\n",
    "                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])\n",
    "\n",
    "        if game.figure is not None:\n",
    "            for i in range(4):\n",
    "                for j in range(4):\n",
    "                    p = i * 4 + j\n",
    "                    if p in game.figure.image():\n",
    "                        pygame.draw.rect(screen, colors[game.figure.color],\n",
    "                                         [game.x + game.zoom * (j + game.figure.x) + 1,\n",
    "                                          game.y + game.zoom * (i + game.figure.y) + 1,\n",
    "                                          game.zoom - 2, game.zoom - 2])\n",
    "\n",
    "        font_score = pygame.font.SysFont('Calibri', 25)\n",
    "        score_text = font_score.render(\"Score: \" + str(game.score), True, (0, 0, 0))\n",
    "        screen.blit(score_text, [20, 20]) \n",
    "\n",
    "        font_lines = pygame.font.SysFont('Calibri', 25)\n",
    "        lines_text = font_lines.render(f\"Lines Cleared: {game.lines_cleared}\", True, (0, 0, 0))\n",
    "        screen.blit(lines_text, [20, 50]) \n",
    "\n",
    "        pygame.display.flip()  # Cập nhật màn hình\n",
    "        clock.tick(fps)  # Giới hạn FPS\n",
    "\n",
    "pygame.quit()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}