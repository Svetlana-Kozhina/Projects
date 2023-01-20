# Необходимо реализовать генератор чисел Фибоначчи, с помощью итератора.

def fib():
    a, b = 0, 1
    yield a # F0
    yield b # F1

    while True:
        a, b = b, a + b
        yield b

for i in fib():
    print(i)

