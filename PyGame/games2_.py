import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
TEAM_COLORS = [RED, BLUE, GREEN, YELLOW]

# Класс для объектов города (зданий)
class Building(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])  # Создание поверхности для здания
        self.image.fill(color)  # Заливка поверхности цветом
        self.rect = self.image.get_rect()  # Получение прямоугольника для позиционирования
        self.dragging = False  # Флаг для перетаскивания здания

# Класс для жителей
class Citizen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])  # Создание поверхности для жителя
        self.image.fill(BLUE)  # Заливка поверхности цветом
        self.rect = self.image.get_rect()  # Получение прямоугольника для позиционирования
        self.rect.x = x  # Начальная позиция по x
        self.rect.y = y  # Начальная позиция по y
        self.direction = random.choice(['left', 'right'])  # Направление движения

    def update(self):
        # Обновление позиции жителя
        if self.direction == 'left':
            self.rect.x -= 1  # Движение влево
            if self.rect.x < 0:
                self.direction = 'right'  # Смена направления при достижении края экрана
        else:
            self.rect.x += 1  # Движение вправо
            if self.rect.x > SCREEN_WIDTH - 20:
                self.direction = 'left'  # Смена направления при достижении края экрана

# Класс для команды
class Team:
    def __init__(self, color):
        self.color = color  # Цвет команды
        self.money = 1000  # Начальное количество денег
        self.buildings = pygame.sprite.Group()  # Группа зданий команды
        self.citizens = pygame.sprite.Group()  # Группа жителей команды

# Создание окна игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Симулятор города')

# Группы спрайтов
all_sprites = pygame.sprite.Group()
buildings = pygame.sprite.Group()
citizens = pygame.sprite.Group()

# Функция для создания зданий
def create_buildings(team):
    for _ in range(5):
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))  # Случайный цвет здания
        width = random.randint(20, 100)  # Случайная ширина здания
        height = random.randint(50, 300)  # Случайная высота здания
        building = Building(color, width, height)  # Создание объекта здания
        building.rect.x = random.randint(0, SCREEN_WIDTH - width)  # Случайное начальное положение по x
        building.rect.y = SCREEN_HEIGHT - height  # Положение по y (внизу экрана)
        all_sprites.add(building)  # Добавление здания в группу всех спрайтов
        buildings.add(building)  # Добавление здания в группу зданий
        team.buildings.add(building)  # Добавление здания в группу зданий команды

# Функция для создания жителей
def create_citizens(team):
    for _ in range(10):
        x = random.randint(0, SCREEN_WIDTH - 20)  # Случайное начальное положение по x
        y = random.randint(0, SCREEN_HEIGHT - 20)  # Случайное начальное положение по y
        citizen = Citizen(x, y)  # Создание объекта жителя
        all_sprites.add(citizen)  # Добавление жителя в группу всех спрайтов
        citizens.add(citizen)  # Добавление жителя в группу жителей
        team.citizens.add(citizen)  # Добавление жителя в группу жителей команды

# Основной игровой цикл
def main():
    # Создание команд
    teams = [Team(color) for color in TEAM_COLORS]
    for team in teams:
        create_buildings(team)  # Создание зданий для каждой команды
        create_citizens(team)  # Создание жителей для каждой команды
    
    current_team_index = 0  # Индекс текущей команды
    current_team = teams[current_team_index]
    day_time = 0  # Время суток

    running = True
    selected_building = None

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    pos = pygame.mouse.get_pos()  # Получение позиции мыши
                    for building in current_team.buildings:
                        if building.rect.collidepoint(pos):
                            selected_building = building  # Выбор здания
                            building.dragging = True  # Установка флага перетаскивания
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # ЛКМ
                    if selected_building:
                        selected_building.dragging = False  # Отключение флага перетаскивания
                        selected_building = None
            elif event.type == pygame.MOUSEMOTION:
                if selected_building and selected_building.dragging:
                    selected_building.rect.x += event.rel[0]  # Перемещение здания по x
                    selected_building.rect.y += event.rel[1]  # Перемещение здания по y
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    current_team_index = (current_team_index + 1) % len(teams)  # Смена текущей команды
                    current_team = teams[current_team_index]

        # Обновление времени суток
        day_time += 1
        if day_time >= 240:  # Пример изменения каждые 4 секунды (60 FPS * 4 сек)
            day_time = 0

        # Установка цвета фона в зависимости от времени суток
        if day_time < 120:
            screen.fill(WHITE)  # День
        else:
            screen.fill(BLACK)  # Ночь

        all_sprites.update()
        all_sprites.draw(screen)

        # Отрисовка информации о деньгах
        font = pygame.font.SysFont(None, 36)
        money_text = font.render(f"Деньги команды {current_team_index + 1}: ${current_team.money}", True, current_team.color)
        screen.blit(money_text, (10, 10))

        # Кнопка для покупки нового здания
        buy_button = pygame.Rect(650, 10, 140, 40)
        pygame.draw.rect(screen, GREEN, buy_button)
        buy_text = font.render("Купить здание", True, BLACK)
        screen.blit(buy_text, (655, 15))

        # Проверка нажатия кнопки покупки
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and buy_button.collidepoint(pygame.mouse.get_pos()):
                if current_team.money >= 100:  # Проверка наличия достаточного количества денег
                    current_team.money -= 100  # Вычитание денег
                    color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
                    width = random.randint(20, 100)
                    height = random.randint(50, 300)
                    building = Building(color, width, height)
                    building.rect.x = random.randint(0, SCREEN_WIDTH - width)
                    building.rect.y = SCREEN_HEIGHT - height
                    all_sprites.add(building)
                    buildings.add(building)
                    current_team.buildings.add(building)

        pygame.display.flip()

        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
