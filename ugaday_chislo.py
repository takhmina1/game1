import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Угадай число")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифты
font = pygame.font.SysFont("Arial", 36)

# Загаданное число
number = random.randint(1, 100)
attempts = 0

# Ввод текста
input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
message = 'Угадайте число от 1 до 100'

def draw_text(surface, text, position, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(text)
                        attempts += 1
                        if guess < number:
                            message = 'Больше!'
                        elif guess > number:
                            message = 'Меньше!'
                        else:
                            message = f'Вы угадали число за {attempts} попыток!'
                    except ValueError:
                        message = 'Введите число!'
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    win.fill(WHITE)

    draw_text(win, message, (WIDTH // 2 - 200, HEIGHT // 2 - 100), BLACK)
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    win.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(win, color, input_box, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
