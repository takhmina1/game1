# # import pygame
# # import sys

# # # Инициализация Pygame
# # pygame.init()

# # # Настройки окна
# # WIDTH, HEIGHT = 800, 600
# # win = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("Простая игра на Pygame")

# # # Основной игровой цикл
# # running = True
# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #     # Отрисовка фона
# #     win.fill((0, 0, 0))  # Черный фон

# #     # Обновление экрана
# #     pygame.display.flip()
# #     pygame.time.Clock().tick(30)

# # pygame.quit()
# # sys.exit()





# # pip install pygame

# import pygame
# import sys
# import random

# pygame.init()

# WIDTH, HEIGHT = 800, 600

# win = pygame.display.set_mode((WIDTH, HEIGHT))

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# font = game.font.Font(None, 74)
# small_font = pygame.font.Font(None, 36)


# number_to_guess = random.randint(1, 100)
# attempts = 0
# message = "ugadayte chislo ot 1 do 100"


# running = True
# input_active = False
# user_input = ""


# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT():
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if input_active:
#                 if event.key == pygame.K_RETURN:
#                     if user_input.isdigit():
#                         guess = int(user_input)
#                         attempts += 1
#                         if guess < number_to_guess:
#                             message = "Bolse!"
#                         elif guess > number_to_guess:
#                             message = "Menshe!"
#                         else:
#                             message = f"Pravilno! vi ugadali za {attempts} popitok. "
#                             number_to_guess = random.randint(1, 100)
#                             attemps = 0

#                         user_input = ""
#             elif event.key == pygame.K_BACKSPASE:
#                 user_input = user_input[:-1]
#             else:
#                 user_input += event.






import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Угадай число на Pygame")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Шрифты
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Загаданное число
number_to_guess = random.randint(1, 100)
attempts = 0
message = "Угадайте число от 1 до 100"

# Основной игровой цикл
running = True
input_active = False
user_input = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    if user_input.isdigit():
                        guess = int(user_input)
                        attempts += 1
                        if guess < number_to_guess:
                            message = "Больше!"
                        elif guess > number_to_guess:
                            message = "Меньше!"
                        else:
                            message = f"Правильно! Вы угадали за {attempts} попыток."
                            number_to_guess = random.randint(1, 100)
                            attempts = 0
                        user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

    # Отрисовка
    win.fill(WHITE)
    prompt_text = font.render(message, True, BLACK)
    win.blit(prompt_text, (50, 100))

    input_box = pygame.Rect(50, 250, 700, 50)
    pygame.draw.rect(win, BLACK, input_box, 2)
    
    input_text = font.render(user_input, True, BLACK)
    win.blit(input_text, (input_box.x + 10, input_box.y + 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
