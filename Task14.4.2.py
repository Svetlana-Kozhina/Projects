# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора.

def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count += 1
        print(f'Функция {func} была вызвана {count} раз')
    return wrapper

@counter
def say_world(word):
    print(word)

say_world('Оо!!!')

say_world('Оо!!!')