'''
Números primos del 1 al 20 (Desafiante):

Planteamiento: Escribe un programa que imprima todos los números primos que existen entre el 1 y el 20 (inclusive).

Recordatorio: Un número primo es un número natural mayor que 1 que no tiene divisores positivos aparte de 1 y él mismo.

Pista: Este ejercicio requiere un poco más de lógica. Necesitarás un ciclo for para iterar del 2 al 20 (el 1 no es primo).
Dentro de este ciclo, necesitarás otro ciclo for anidado para verificar si el número actual tiene algún
divisor entre 2 y él mismo -
1. Si no tiene ningún divisor, entonces es primo.
'''


for num in range(2,120):
    es_primo = True
    for i in range(2, int(num / 2) + 1 ):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El numero {num} es primo")

