import os
from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter
from geometric_lib.square import area as square_area, perimeter as square_perimeter

figure = os.getenv("FIGURE")
value = os.getenv("VALUE")

if figure is None or value is None:
    print("Ошибка: переменные окружения FIGURE и VALUE должны быть заданы")
    exit(1)

value = float(value)

if figure == "circle":
    print("Площадь круга:", circle_area(value))
    print("Периметр круга:", circle_perimeter(value))

elif figure == "square":
    print("Площадь квадрата:", square_area(value))
    print("Периметр квадрата:", square_perimeter(value))

else:
    print("Неизвестная фигура:", figure)

