# Замыкание часть 2

def add(a, b):
    return a+b

def counter(func): # передаем название функции, в нашем случае это add
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)
    return inner

