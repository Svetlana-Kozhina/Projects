# Декораторы. Часть 1
# Декоратор - ф-ция, к-я принимает другую функцию и возращает фукнцию.
# Декораторы нужны, чтобы в ф-ции добавилось новое поведение или новый функционал.

def header(func):

    def inner(*args, **kwargs): #произвольное количество элементов, позиционных и именованных
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner

def table(func):

    def inner(*args, **kwargs): #произвольное количество элементов, позиционных и именованных
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner
@header
@table #say = header(say)
def say(name, surname, age): #расширить функционал ф-ции say за счет вызова ф-ции decorator
    print('hello', name, surname, age)

say('Vasya', 'Ivanov', 30)
