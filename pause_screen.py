import pygame
from backgrounds_and_sound import toggle_mute
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BORDER_COLOR = (179, 204, 255)
BUBBLE = (230, 247, 255)
OXFORD_BLUE = (0, 38, 77)
GREEN = (0, 255, 0)


                    #####ĐỊNH NGHĨA MÀN HÌNH TẠM DỪNG#####
#Vẽ màn hình tạm dừng
main_window_size = (800, 700)  # Updated size
main_window = pygame.display.set_mode(main_window_size)
# Kích thước màn hình nhỏ
small_window_size = (400, 450)  # Larger popup
border_thickness = 5
# Kích thước bề mặt màu xám
gray_surface = pygame.Surface(main_window_size)
gray_surface.fill((230,238,255))  
gray_surface.set_alpha(7)  # Đặt độ trong suốt

small_window_x = (main_window_size[0] - small_window_size[0]) // 2  # Center horizontally
small_window_y = (main_window_size[1] - small_window_size[1]) // 2  # Center vertically

small_window_surface = pygame.Surface(small_window_size)
small_window_surface.fill(BUBBLE)

border_surface = pygame.Surface((small_window_size[0] + 2 * border_thickness, small_window_size[1] + 2 * border_thickness))  # Cho phép alpha
pygame.draw.rect(border_surface, BORDER_COLOR, (0, 0, *border_surface.get_size()))  # Màu viền (không bo tròn)
border_surface.set_alpha(255)  # Đặt độ trong suốt cho viền
border_surface.set_alpha(255)

##BUTTON
button_rect_resume = pygame.Rect(small_window_x + 100, small_window_y + 100, 210, 50)  # Wider and taller buttons
button_rect_restart = pygame.Rect(small_window_x + 100, small_window_y + 180, 210, 50)
button_rect_menu = pygame.Rect(small_window_x + 100, small_window_y + 260, 210, 50)

button_color = OXFORD_BLUE
# Hàm vẽ nút Mute
                        #####ĐỊNH NGHĨA MÀN HÌNH TẠM DỪNG#####

button_rect_mute = pygame.Rect(small_window_x + 100, small_window_y + 340, 210, 50)  # Tăng kích thước nút cho dễ nhấn

def draw_mute_button(screen, button_states):
    mouse_pos = pygame.mouse.get_pos()
    mute_color = (196, 226, 255) if button_states["button_mute_pressed"] else button_color

    text_content =  "UNMUTE" if pygame.mixer.music.get_volume() == 0 else "MUTE"

    # Tạo font
    normal_font_size = 24
    hover_font_size = 26  # Phóng to chữ khi hover
    font_size = hover_font_size if button_rect_mute.collidepoint(mouse_pos) else normal_font_size
    font = pygame.font.SysFont('Calibri', font_size, True, False)

    # Render text
    button_text_surface_mute = font.render(text_content, True, WHITE)
    text_rect_mute = button_text_surface_mute.get_rect(center=button_rect_mute.center)

    # Vẽ nút MUTE
    if button_rect_mute.collidepoint(mouse_pos):  
        # Hiệu ứng hover (phóng to nút)
        pygame.draw.rect(screen, mute_color, button_rect_mute.inflate(10, 10))
        text_rect_mute = button_text_surface_mute.get_rect(center=button_rect_mute.center)  # Căn chỉnh lại chữ
    else:
        pygame.draw.rect(screen, mute_color, button_rect_mute)

    # Vẽ text lên nút
    screen.blit(button_text_surface_mute, text_rect_mute)

    return button_rect_mute



def draw_pause_button(screen):
    button_rect_pause = pygame.Rect(720, 30, 45, 35)  # Moved to top-right

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

def draw_pause_screen(screen, button_states):
    mouse_pos = pygame.mouse.get_pos()
    main_window.blit(gray_surface, (0, 0))
    main_window.blit(border_surface, (small_window_x - border_thickness, small_window_y - border_thickness))  # Vẽ viền
    main_window.blit(small_window_surface, (small_window_x, small_window_y))

    font1 = pygame.font.SysFont('Calibri', 30, True, False)

    resume_color = (196, 226, 255) if button_states["button_resume_pressed"] else button_color
    restart_color = (196, 226, 255) if button_states["button_restart_pressed"] else button_color
    menu_color = (196, 226, 255) if button_states["button_menu_pressed"] else button_color

    # Vẽ button RESUME
    if button_rect_resume.collidepoint(mouse_pos):
        pygame.draw.rect(screen, resume_color, button_rect_resume.inflate(10, 10))
        font_hover = pygame.font.SysFont('Calibri', 26, True, False)  # Font lớn hơn khi hover
        button_text_surface_resume = font_hover.render("RESUME", True, (255, 255, 255))
    else:
        pygame.draw.rect(screen, resume_color, button_rect_resume)
        font_normal = pygame.font.SysFont('Calibri', 24, True, False)  # Font mặc định
        button_text_surface_resume = font_normal.render("RESUME", True, (255, 255, 255))
    text_rect_resume = button_text_surface_resume.get_rect(center=button_rect_resume.center)
    screen.blit(button_text_surface_resume, text_rect_resume)

    # Vẽ button RESTART
    if button_rect_restart.collidepoint(mouse_pos):
        pygame.draw.rect(screen, restart_color, button_rect_restart.inflate(10, 10))
        font_hover = pygame.font.SysFont('Calibri', 26, True, False)
        button_text_surface_restart = font_hover.render("RESTART", True, (255, 255, 255))
    else:
        pygame.draw.rect(screen, restart_color, button_rect_restart)
        font_normal = pygame.font.SysFont('Calibri', 24, True, False)
        button_text_surface_restart = font_normal.render("RESTART", True, (255, 255, 255))
    text_rect_restart = button_text_surface_restart.get_rect(center=button_rect_restart.center)
    screen.blit(button_text_surface_restart, text_rect_restart)

    # Vẽ button MENU
    if button_rect_menu.collidepoint(mouse_pos):
        pygame.draw.rect(screen, menu_color, button_rect_menu.inflate(10, 10))
        font_hover = pygame.font.SysFont('Calibri', 26, True, False)
        button_text_surface_menu = font_hover.render("MENU", True, (255, 255, 255))
    else:
        pygame.draw.rect(screen, menu_color, button_rect_menu)
        font_normal = pygame.font.SysFont('Calibri', 24, True, False)
        button_text_surface_menu = font_normal.render("MENU", True, (255, 255, 255))
    text_rect_menu = button_text_surface_menu.get_rect(center=button_rect_menu.center)
    screen.blit(button_text_surface_menu, text_rect_menu)

    pause_text = font1.render("PAUSED", True, OXFORD_BLUE)
    screen.blit(pause_text, [small_window_x + small_window_size[0]//2 - pause_text.get_width()//2, small_window_y + 30])

    draw_mute_button(screen,button_states)
    pygame.display.flip()

    return button_rect_resume, button_rect_restart, button_rect_menu
