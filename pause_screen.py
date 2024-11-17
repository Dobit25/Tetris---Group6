import pygame
## ĐỊNH NGHĨA MÀU
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BORDER_COLOR = (179, 204, 255)
BUBBLE = (230, 247, 255)
OXFORD_BLUE = (0, 38, 77)
GREEN = (0, 255, 0)



# Vẽ nút PAUSE
button_rect_pause = pygame.Rect(320, 20, 35, 25)  # Thêm nút dừng
def draw_pause_button(screen):
    button_rect_pause = pygame.Rect(320, 20, 35, 25)  # Thêm nút dừng

    # Lấy vị trí chuột
    mouse_pos = pygame.mouse.get_pos()
    is_hovered = button_rect_pause.collidepoint(mouse_pos)
    is_clicked = pygame.mouse.get_pressed()[0] and is_hovered  # Kiểm tra nếu nhấn chuột trái
    # Thay đổi màu sắc và kích thước dựa vào trạng thái hover/click
    if is_clicked:
        button_color = (100, 150, 200)  # Màu khi click
        adjusted_rect = button_rect_pause  # Thu nhỏ khi click
    elif is_hovered:
        button_color = (196, 226, 255)  # Màu khi hover
        adjusted_rect = button_rect_pause.inflate(5, 5)  # Phóng to khi hover
    else:
        button_color = BORDER_COLOR  # Màu mặc định
        adjusted_rect = button_rect_pause  # Giữ nguyên kích thước
    # Vẽ nút PAUSE
    pygame.draw.rect(screen, button_color, adjusted_rect)  # Vẽ nút nền
    # Vẽ biểu tượng PAUSE: hai thanh dọc
    bar_width = 5  # Độ rộng của mỗi thanh
    bar_height = 13  # Chiều cao của mỗi thanh
    gap = 7  # Khoảng cách giữa hai thanh
    bar_x1 = adjusted_rect.centerx - bar_width - gap // 2
    bar_x2 = adjusted_rect.centerx + gap // 2
    bar_y = adjusted_rect.centery - bar_height // 2
    # Thanh trái
    pygame.draw.rect(screen, WHITE, (bar_x1, bar_y, bar_width, bar_height))
    # Thanh phải
    pygame.draw.rect(screen, WHITE, (bar_x2, bar_y, bar_width, bar_height))
    return button_rect_pause

    



###ĐỊNH NGHĨA MÀN HÌNH TẠM DỪNG
#Vẽ màn hình tạm dừng
main_window_size = (400,500)
main_window = pygame.display.set_mode(main_window_size)
# Kích thước màn hình nhỏ
small_window_size = (250, 290)
border_thickness = 5
# Kích thước bề mặt màu xám
gray_surface = pygame.Surface(main_window_size)
gray_surface.fill((230,238,255))  
gray_surface.set_alpha(7)  # Đặt độ trong suốt

small_window_surface = pygame.Surface(small_window_size)
small_window_surface.fill(BUBBLE)

border_surface = pygame.Surface((small_window_size[0] + 2 * border_thickness, small_window_size[1] + 2 * border_thickness))  # Cho phép alpha
pygame.draw.rect(border_surface, BORDER_COLOR, (0, 0, *border_surface.get_size()))  # Màu viền (không bo tròn)
border_surface.set_alpha(255)  # Đặt độ trong suốt cho viền
border_surface.set_alpha(255)

##BUTTON
button_rect_resume = pygame.Rect(155, 170, 100, 50)
button_rect_restart = pygame.Rect(155, 240, 100, 50)  # Vị trí và kích thước của button
button_rect_menu = pygame.Rect(155, 310, 100, 50)

# button_resume_pressed = False
# button_restart_pressed = False
# button_menu_pressed = False

button_color = OXFORD_BLUE

def draw_pause_screen(screen, button_states):
    mouse_pos = pygame.mouse.get_pos()
    main_window.blit(gray_surface, (0, 0))
    main_window.blit(border_surface, (80 - border_thickness, 100 - border_thickness))  # Vẽ viền
    main_window.blit(small_window_surface, (80, 100))

    font1 = pygame.font.SysFont('Calibri', 30, True, False)
    font2 = pygame.font.SysFont('Calibri', 20, True, False)

    resume_color = (196, 226, 255) if button_states["button_resume_pressed"] else button_color
    restart_color = (196, 226, 255) if button_states["button_restart_pressed"] else button_color
    menu_color = (196, 226, 255) if button_states["button_menu_pressed"] else button_color

    # Vẽ button RESUME
    pygame.draw.rect(screen, resume_color, button_rect_resume)
    if button_rect_resume.collidepoint(mouse_pos):
        pygame.draw.rect(screen, resume_color, button_rect_resume.inflate(10, 10))
        button_text_surface_resume = font2.render("RESUME", True, (255, 255, 255))
        text_rect_resume = button_text_surface_resume.get_rect(center=button_rect_resume.center)
    else:
        pygame.draw.rect(screen, resume_color, button_rect_resume)
        button_text_surface_resume = font2.render("RESUME", True, (255, 255, 255))
        text_rect_resume = button_text_surface_resume.get_rect(center=button_rect_resume.center)
    screen.blit(button_text_surface_resume, text_rect_resume)

    # Vẽ button RESTART
    pygame.draw.rect(screen, restart_color, button_rect_restart)
    if button_rect_restart.collidepoint(mouse_pos):
        pygame.draw.rect(screen, restart_color, button_rect_restart.inflate(10, 10))
        button_text_surface_restart = font2.render("RESTART", True, (255, 255, 255))
        text_rect_restart = button_text_surface_restart.get_rect(center=button_rect_restart.center)
    else:
        pygame.draw.rect(screen, restart_color, button_rect_restart)
        button_text_surface_restart = font2.render("RESTART", True, (255, 255, 255))
        text_rect_restart = button_text_surface_restart.get_rect(center=button_rect_restart.center)
    screen.blit(button_text_surface_restart, text_rect_restart)

    # Vẽ button MENU
    pygame.draw.rect(screen, menu_color, button_rect_menu)
    if button_rect_menu.collidepoint(mouse_pos):
        pygame.draw.rect(screen, menu_color, button_rect_menu.inflate(10, 10))
        button_text_surface_menu = font2.render("MENU", True, (255, 255, 255))
        text_rect_menu = button_text_surface_menu.get_rect(center=button_rect_menu.center)
    else:
        pygame.draw.rect(screen, menu_color, button_rect_menu)
        button_text_surface_menu = font2.render("MENU", True, (255, 255, 255))
        text_rect_menu = button_text_surface_menu.get_rect(center=button_rect_menu.center)
    screen.blit(button_text_surface_menu, text_rect_menu)

    # Vẽ PAUSED
    pause_text = font1.render("PAUSED", True, OXFORD_BLUE)
    screen.blit(pause_text, [160, 110])

    pygame.display.flip()

    return button_rect_resume, button_rect_restart, button_rect_menu
