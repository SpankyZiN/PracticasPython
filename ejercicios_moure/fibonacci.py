'''
* Escribe un programa que imprima los 50 primeros números de la sucesión
* de Fibonacci empezando en 0.
* - La serie Fibonacci se compone por una sucesión de números en
*   la que el siguiente siempre es la suma de los dos anteriores.
*   0, 1, 1, 2, 3, 5, 8, 13...
'''

# x = 0
# z = 1
# for x in range(0,50):
#     y = x + z
#     x = z
#     z = y
#     print(y)


def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(n - 2):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Imprimir los primeros 50 números de Fibonacci
for num in fibonacci(50):
    print(num)
