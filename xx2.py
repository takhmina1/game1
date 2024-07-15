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
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Шрифты
font = pygame.font.SysFont("Arial", 36)

# Уровни сложности
levels = {
    "Легкий": 10,
    "Средний": 7,
    "Сложный": 5
}

# Начальное состояние игры
level = None
number = None
attempts = 0
max_attempts = 0

# Ввод текста
input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
message = 'Выберите уровень сложности'

# Кнопки
button_easy = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 100, 300, 50)
button_medium = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 50)
button_hard = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 100, 300, 50)
button_start = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 200, 300, 50)
button_check = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50)

# Функция для отображения текста
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
            if button_easy.collidepoint(event.pos):
                level = "Легкий"
                max_attempts = levels[level]
                number = random.randint(1, 100)
                attempts = 0
                message = f'Угадайте число от 1 до 100 ({max_attempts} попыток)'
            elif button_medium.collidepoint(event.pos):
                level = "Средний"
                max_attempts = levels[level]
                number = random.randint(1, 100)
                attempts = 0
                message = f'Угадайте число от 1 до 100 ({max_attempts} попыток)'
            elif button_hard.collidepoint(event.pos):
                level = "Сложный"
                max_attempts = levels[level]
                number = random.randint(1, 100)
                attempts = 0
                message = f'Угадайте число от 1 до 100 ({max_attempts} попыток)'
            elif button_start.collidepoint(event.pos):
                if level is not None:
                    active = True
                    color = color_active if active else color_inactive
                    message = f'Угадайте число от 1 до 100 ({max_attempts} попыток)'
            elif button_check.collidepoint(event.pos) and active:
                try:
                    guess = int(text)
                    attempts += 1
                    if guess < number:
                        message = f'Больше! Осталось {max_attempts - attempts} попыток'
                    elif guess > number:
                        message = f'Меньше! Осталось {max_attempts - attempts} попыток'
                    else:
                        message = f'Вы угадали число за {attempts} попыток!'
                        active = False
                        color = color_inactive
                except ValueError:
                    message = 'Введите число!'
                text = ''
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(text)
                        attempts += 1
                        if guess < number:
                            message = f'Больше! Осталось {max_attempts - attempts} попыток'
                        elif guess > number:
                            message = f'Меньше! Осталось {max_attempts - attempts} попыток'
                        else:
                            message = f'Вы угадали число за {attempts} попыток!'
                            active = False
                            color = color_inactive
                    except ValueError:
                        message = 'Введите число!'
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Чередование цветов фона
    win.fill(YELLOW if pygame.time.get_ticks() // 500 % 2 == 0 else GREEN)

    if not active:
        pygame.draw.rect(win, WHITE, button_easy)
        pygame.draw.rect(win, WHITE, button_medium)
        pygame.draw.rect(win, WHITE, button_hard)
        pygame.draw.rect(win, WHITE, button_start)
        
        draw_text(win, 'Легкий', (button_easy.x + 100, button_easy.y + 10), BLACK)
        draw_text(win, 'Средний', (button_medium.x + 100, button_medium.y + 10), BLACK)
        draw_text(win, 'Сложный', (button_hard.x + 100, button_hard.y + 10), BLACK)
        draw_text(win, 'Начать игру', (button_start.x + 50, button_start.y + 10), BLACK)
    else:
        draw_text(win, message, (WIDTH // 2 - 300, HEIGHT // 2 - 100), BLACK)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(win, color, input_box, 2)

        pygame.draw.rect(win, WHITE, button_check)
        draw_text(win, 'Проверить', (button_check.x + 30, button_check.y + 10), BLACK)

    pygame.display.flip()

pygame.quit()
sys.exit()
