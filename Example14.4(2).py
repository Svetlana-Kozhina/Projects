# Замыкание часть 2

def average_numbers():
    summa = 0
    count = 0
    def inner(number):
        nonlocal summa # Будет браться значение переменной, которая находится в области видимости ф-ции average_numbers
        nonlocal count
        summa = summa + number
        count += 1

        return summa / count
    return inner
