from graph import *

def triangle(x1, y1, x2, y2, x3, y3):
    """
    выделяем сложное строительство треугольника в отдельную функцию
    """
    polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])

# Задаем точки треугольника
x0, y0 = 0, 0
x1, y1 = 30, 40
x2, y2 = 65, 0

# задаем шаг по оси Х и по У
step_by_y = 100
step_by_x = 90

count_horizontal_triangle = 3
count_vertical_triangle = 5

# задаем цвета
penColor("red")
brushColor("blue")

# рисуем
# проходим по вертикали
for i in range(count_vertical_triangle):
    # проходим по горизонтали
    for j in range(count_horizontal_triangle):
        # Отступ = предыдущий отступ + шаг отступа
        # или так
        shift_y = step_by_y*i
        shift_x = step_by_x*j
        triangle(x0+shift_x, y0+shift_y, x1+shift_x, y1+shift_y, x2+shift_x, y2+shift_y)

run()