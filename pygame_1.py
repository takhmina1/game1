import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание игрового окна
WIDTH, HEIGHT = 800, 600  # Ширина и высота окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна с заданными размерами
pygame.display.set_caption("Перемещающийся квадрат")  # Установка заголовка окна

# Установка цветов
WHITE = (255, 255, 255)  # Белый цвет в формате RGB
BLACK = (0, 0, 0)  # Черный цвет в формате RGB

# Начальное положение квадрата
square_x = WIDTH // 2  # Начальная координата X квадрата (в центре окна)
square_y = HEIGHT // 2  # Начальная координата Y квадрата (в центре окна)
square_size = 50  # Размер квадрата (ширина и высота)
square_speed = 5  # Скорость движения квадрата

# Главный игровой цикл
running = True  # Переменная, указывающая, что игра запущена
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если событие - закрытие окна
            running = False  # Выход из игрового цикла

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()  # Получение словаря всех клавиш и их состояния

    # Движение квадрата
    if keys[pygame.K_LEFT] and square_x > 0:  # Если нажата клавиша "влево" и квадрат не заходит за левую границу
        square_x -= square_speed  # Двигаем квадрат влево
    if keys[pygame.K_RIGHT] and square_x < WIDTH - square_size:  # Если нажата клавиша "вправо" и квадрат не заходит за правую границу
        square_x += square_speed  # Двигаем квадрат вправо
    if keys[pygame.K_UP] and square_y > 0:  # Если нажата клавиша "вверх" и квадрат не заходит за верхнюю границу
        square_y -= square_speed  # Двигаем квадрат вверх
    if keys[pygame.K_DOWN] and square_y < HEIGHT - square_size:  # Если нажата клавиша "вниз" и квадрат не заходит за нижнюю границу
        square_y += square_speed  # Двигаем квадрат вниз

    # Заполнение экрана белым цветом
    screen.fill(WHITE)  # Очистка экрана белым цветом

    # Рисование квадрата
    pygame.draw.rect(screen, BLACK, (square_x, square_y, square_size, square_size))  # Рисование черного квадрата

    # Обновление экрана
    pygame.display.flip()  # Обновление содержимого окна

# Завершение игры
pygame.quit()  # Завершение работы Pygame
sys.exit()  # Закрытие программы
