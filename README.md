### Пояснения

1. **Инициализация Pygame**:
   - `pygame.init()` - инициализирует все модули Pygame.
2. **Создание игрового окна**:
   - `pygame.display.set_mode((WIDTH, HEIGHT))` - создает окно с заданными размерами.
   - `pygame.display.set_caption("Перемещающийся квадрат")` - устанавливает заголовок окна.
3. **Установка цветов**:
   - `WHITE = (255, 255, 255)` - определяет белый цвет.
   - `BLACK = (0, 0, 0)` - определяет черный цвет.
4. **Начальное положение квадрата**:
   - `square_x` и `square_y` - начальные координаты квадрата.
   - `square_size` - размер квадрата.
   - `square_speed` - скорость движения квадрата.
5. **Главный игровой цикл**:
   - `while running` - основной цикл игры, который выполняется, пока `running` равно `True`.
   - `pygame.event.get()` - получение списка всех событий.
   - `pygame.key.get_pressed()` - получение состояния всех клавиш.
   - Условия для движения квадрата (`if keys[pygame.K_LEFT]` и т.д.) - проверяют, нажаты ли соответствующие клавиши и находится ли квадрат в пределах окна.
6. **Заполнение экрана и рисование квадрата**:
   - `screen.fill(WHITE)` - заполняет экран белым цветом.
   - `pygame.draw.rect(screen, BLACK, (square_x, square_y, square_size, square_size))` - рисует черный квадрат.
7. **Обновление экрана**:
   - `pygame.display.flip()` - обновляет содержимое окна.
8. **Завершение игры**:
   - `pygame.quit()` - завершает работу Pygame.
   - `sys.exit()` - закрывает программу.

Объяснение:
Инициализация Pygame и создание окна:

pygame.init() - инициализация Pygame.
pygame.display.set_mode((WIDTH, HEIGHT)) - создание игрового окна заданного размера.
pygame.display.set_caption("Игра 'Змейка'") - установка заголовка окна.
Установка цветов:

WHITE, BLACK, GREEN - определение цветов для использования в игре.
Начальные параметры змейки:

snake_x, snake_y - начальные координаты змейки.
snake_size - размер части змейки.
snake_speed - скорость движения змейки.
snake_dx, snake_dy - начальные скорости по осям X и Y.
snake_body - список для хранения координат частей змейки.
Главный игровой цикл:

while running - основной цикл игры, выполняется, пока running равно True.
Обработка событий, включая нажатие клавиш для изменения направления движения змейки.
Обновление положения змейки:

Изменение координат змейки в зависимости от её направления (snake_dx, snake_dy).
Проверка выхода за границы экрана:

Проверка текущих координат змейки на выход за границы окна.
Отрисовка змейки:

Использование pygame.draw.rect() для отрисовки каждой части змейки.
Добавление и удаление частей змейки:

Добавление новой части змейки в конец списка snake_body.
Удаление старой части змейки (первый элемент списка), если длина списка превышает 1.
Обновление экрана и задержка:

pygame.display.flip() - обновление содержимого окна.
pygame.time.Clock().tick(15) - задержка, регулирующая скорость игры.
Завершение игры:

pygame.quit() и sys.exit() - закрытие Pygame и завершение программы.
Этот код создает простую игру "Змейка", где змейка движется по экрану, реагируя на нажатия клавиш и ограничивая свои движения границами окна
