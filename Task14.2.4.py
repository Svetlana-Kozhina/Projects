# С помощью рекурсивной функции разверните строку.

def reverse_str(n):
    if len(n) == 0:
        return ''
    else:
        return n[-1] + reverse_str(n[:-1])

print(reverse_str("Hello"))