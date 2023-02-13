from rectangle import Rectangle, Square, Circle

# Далее создаем два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# Вывод площади наших двух прямоугольников

square_1 = Square(5)
square_2 = Square(10)

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

# Площадь круга

circle_1 = Circle(10)
print(circle_1.get_area_circle())