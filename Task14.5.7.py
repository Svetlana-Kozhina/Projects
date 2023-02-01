# Представим, что параметры уравнения хранятся в виде списка. Такое может быть, если аргументы были получены из консоли.

# разбили строку из input и преобразовали к float
# Ввод строки 1 0 -1
# Вывод [1.0, 0.0, -1.0]
# [1, 0, -1] - например


L = list(map(float, input().split()))
def D(a, b, c):
    return b**2 - 4*a*c
def quadratic_equation(a, b, c):
    if D(a, b, c) < 0:
        return 'Уравнение не имеет вещественных корней'
    elif D(a, b, c) == 0:
        return -b/(2*a)
    else:
        return (-b - D(a, b, c)**0.5)/(2*a), (-b + D(a, b, c)**0.5)/(2*a)

print(quadratic_equation(*L))