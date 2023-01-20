# Вложенные функции, замыкания, декораторы

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

q = counter()
print(q())
print(q())
print(q())
