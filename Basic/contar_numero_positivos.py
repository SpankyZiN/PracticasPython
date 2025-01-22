'''
Contar números positivos en una lista:

Planteamiento: Escribe un programa que reciba una lista de números (pueden ser positivos, negativos o cero) y cuente cuántos números positivos hay en la lista.

Ejemplo de entrada: numeros = [-2, 5, 0, -1, 8, 3, -4] #esto es una lista de numeros

Salida esperada (para el ejemplo): Hay 3 números positivos en la lista.

Pista: Usa un ciclo for para recorrer la lista. Dentro del ciclo, usa una sentencia if para verificar si el número actual es mayor que cero. Si lo es, incrementa un contador.
'''

numeros = [-2, 5, 0, -1, 8, 3, -4]
contador_positivos = 0
for numero in numeros:
    if numero > 0:
        contador_positivos += 1
print(f"Hay {contador_positivos} números positivos en la lista.")
