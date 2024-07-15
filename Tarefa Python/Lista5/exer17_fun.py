def triangulo_lateral(n):
    i = 1
    while i <= n:
        print('*' * i)
        i += 1

    i = n - 1
    while i > 0:
        print('*' * i)
        i -= 1

n = 4
triangulo_lateral(n)
