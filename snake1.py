import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание игрового окна
WIDTH, HEIGHT = 800, 600  # Размер окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра 'Змейка'")

# Установка цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Начальное положение змейки и её параметры
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_size = 20
snake_speed = 10
snake_dx = snake_speed  # Начальная скорость по оси X
snake_dy = 0  # Начальная скорость по оси Y
snake_body = [(snake_x, snake_y)]  # Список для хранения частей змейки

# Главный игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Изменение направления движения змейки при нажатии клавиш
            if event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx = -snake_speed
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx = snake_speed
                snake_dy = 0
            elif event.key == pygame.K_UP and snake_dy == 0:
                snake_dx = 0
                snake_dy = -snake_speed
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dx = 0
                snake_dy = snake_speed

    # Обновление положения змейки
    snake_x += snake_dx
    snake_y += snake_dy

    # Проверка выхода за границы экрана
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        running = False

    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка змейки
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], snake_size, snake_size))

    # Добавление новой части змейки
    snake_body.append((snake_x, snake_y))

    # Удаление старой части змейки (если длина списка больше 1)
    if len(snake_body) > 1:
        snake_body.pop(0)

    # Обновление экрана
    pygame.display.flip()

    # Задержка, регулирующая скорость игры
    pygame.time.Clock().tick(15)

# Завершение игры
pygame.quit()
sys.exit()
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание игрового окна
WIDTH, HEIGHT = 800, 600  # Размер окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра 'Змейка'")

# Установка цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Начальное положение змейки и её параметры
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_size = 20
snake_speed = 10
snake_dx = snake_speed  # Начальная скорость по оси X
snake_dy = 0  # Начальная скорость по оси Y
snake_body = [(snake_x, snake_y)]  # Список для хранения частей змейки

# Главный игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Изменение направления движения змейки при нажатии клавиш
            if event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx = -snake_speed
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx = snake_speed
                snake_dy = 0
            elif event.key == pygame.K_UP and snake_dy == 0:
                snake_dx = 0
                snake_dy = -snake_speed
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dx = 0
                snake_dy = snake_speed

    # Обновление положения змейки
    snake_x += snake_dx
    snake_y += snake_dy

    # Проверка выхода за границы экрана
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        running = False

    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка змейки
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], snake_size, snake_size))

    # Добавление новой части змейки
    snake_body.append((snake_x, snake_y))

    # Удаление старой части змейки (если длина списка больше 1)
    if len(snake_body) > 1:
        snake_body.pop(0)

    # Обновление экрана
    pygame.display.flip()

    # Задержка, регулирующая скорость игры
    pygame.time.Clock().tick(15)

# Завершение игры
pygame.quit()
sys.exit()



